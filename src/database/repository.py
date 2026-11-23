
from sqlalchemy import text
from src.database.connection import engine

# 1. Insert a new elective
def add_elective(
    course_code,
    course_name,
    credit_hours,
    prerequisites=None,
    semester=None
):
    query = text("""
        INSERT INTO electives (
            course_code,
            course_name,
            credit_hours,
            prerequisites,
            semester
        )
        VALUES (
            :course_code,
            :course_name,
            :credit_hours,
            CAST(:prerequisites AS TEXT[]),
            :semester
        )
        RETURNING elective_id;
    """)

    with engine.begin() as connection:
        result = connection.execute(
            query,
            {
                "course_code": course_code,
                "course_name": course_name,
                "credit_hours": credit_hours,
                "prerequisites": prerequisites or [],
                "semester": semester
            }
        )

        return result.scalar_one()


# 2. Retrieve all electives
def get_all_electives():
    query = text("""
        SELECT *
        FROM electives
        ORDER BY elective_id;
    """)

    with engine.connect() as connection:
        result = connection.execute(query)

        return [dict(row) for row in result.mappings().all()]


# 3. Delete an elective using its ID
def delete_elective(elective_id):
    query = text("""
        DELETE FROM electives
        WHERE elective_id = :elective_id;
    """)

    with engine.begin() as connection:
        connection.execute(
            query,
            {"elective_id": elective_id}
        )

###############################################################

def save_student_results(session_id, results):
    """
    Replace the saved results for this Streamlit session.
    """

    if not results:
        raise ValueError("No student results to save.")

    insert_query = text("""
        INSERT INTO student_results (
            session_id,
            course_code,
            subject_name,
            marks,
            grade,
            credit_hours,
            grade_points,
            product,
            is_passed
        )
        VALUES (
            :session_id,
            :course_code,
            :subject_name,
            :marks,
            :grade,
            :credit_hours,
            :grade_points,
            :product,
            :is_passed
        )
    """)

    records = []

    for result in results:
        records.append({
            "session_id": session_id,
            "course_code": result["course_code"],
            "subject_name": result["subject_name"],
            "marks": None,
            "grade": result["grade"],
            "credit_hours": result["credit_hours"],
            "grade_points": result["grade_points"],
            "product": result["product"],
            "is_passed": result["is_passed"]
        })

    with engine.begin() as connection:

        # Remove the previous pasted results for this session
        connection.execute(
            text("""
                DELETE FROM student_results
                WHERE session_id = :session_id
            """),
            {"session_id": session_id}
        )

        # Save the latest reviewed results
        connection.execute(insert_query, records)


def get_elective_eligibility(session_id):
    """
    Compare the student's passed courses with elective prerequisites.
    """

    with engine.connect() as connection:

        elective_query = text("""
            SELECT
                elective_id,
                course_code,
                course_name,
                credit_hours,
                prerequisites
            FROM electives
            ORDER BY elective_id
        """)

        result_query = text("""
            SELECT course_code, is_passed
            FROM student_results
            WHERE session_id = :session_id
        """)

        electives = connection.execute(elective_query).mappings().all()

        student_results = connection.execute(
            result_query,
            {"session_id": session_id}
        ).mappings().all()

    # Group student results by course code.
    # Repeated attempts with conflicting statuses need verification.
    student_courses = {}

    for result in student_results:
        code = result["course_code"].strip().upper()
        student_courses.setdefault(code, []).append(result["is_passed"])

    eligibility = []

    for elective in electives:

        prerequisites = elective["prerequisites"] or []

        passed = []
        failed = []
        missing = []
        verification = []

        for prerequisite in prerequisites:

            prerequisite = prerequisite.strip().upper()
            attempts = student_courses.get(prerequisite)

            if not attempts:
                missing.append(prerequisite)

            elif len(set(attempts)) > 1 or None in attempts:
                verification.append(prerequisite)

            elif attempts[0] is True:
                passed.append(prerequisite)

            else:
                failed.append(prerequisite)

        if verification:
            status = "Needs verification"

        elif failed:
            status = "Not eligible"

        elif missing:
            status = "Prerequisite not found"

        else:
            status = "Eligible"

        eligibility.append({
            "course_code": elective["course_code"],
            "course_name": elective["course_name"],
            "credit_hours": elective["credit_hours"],
            "prerequisites": prerequisites,
            "status": status,
            "missing": missing,
            "failed": failed,
            "verification": verification
        })

    return eligibility
