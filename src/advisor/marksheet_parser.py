
import csv
import re
from io import StringIO


def check_passing_grade(grade):
    """
    D and all recognized grades except F are passing.
    Unknown grades return None.
    """

    grade = str(grade).strip().upper()

    passing_grades = {
        "A+", "A", "A-",
        "B+", "B", "B-",
        "C+", "C", "C-",
        "D" , "D+", "D-"
    }

    if grade == "F":
        return False

    if grade in passing_grades:
        return True

    return None


def clean_number(value):
    """
    Convert a numeric string into a float.
    Return None if the value is empty or invalid.
    """

    value = str(value).strip()

    if not value or value.upper() == "N/A":
        return None

    try:
        return float(value)
    except ValueError:
        return None


def parse_lms_results(raw_text):
    """
    Parse LMS results copied as either:
    1. Markdown pipe table
    2. Tab-separated table

    Returns a list of dictionaries.
    """

    if not raw_text or not raw_text.strip():
        raise ValueError("Please paste your LMS results first.")

    lines = [
        line.strip()
        for line in raw_text.strip().splitlines()
        if line.strip()
    ]

    # Detect table format
    if any("|" in line for line in lines):
        rows = []

        for line in lines:
            if "|" not in line:
                continue

            # Remove outer pipes and split columns
            cells = [
                cell.strip()
                for cell in line.strip().strip("|").split("|")
            ]

            # Ignore Markdown separator rows
            if all(
                re.fullmatch(r":?-{3,}:?", cell.replace(" ", ""))
                for cell in cells
            ):
                continue

            rows.append(cells)

    else:
        # Handle tab-separated copied LMS results
        rows = list(csv.reader(StringIO(raw_text), delimiter="\t"))

        rows = [
            [cell.strip() for cell in row]
            for row in rows
            if any(cell.strip() for cell in row)
        ]

    if len(rows) < 2:
        raise ValueError("No valid result rows found.")

    # Normalize column names
    headers = [
        header.strip().lower().replace("_", " ")
        for header in rows[0]
    ]

    # Find column positions
    required_columns = {
        "code": ["code", "course code"],
        "title": ["title", "course title", "subject name"],
        "credit_hours": ["credit hours", "credit hour", "credits"],
        "grade": ["grade"],
        "grade_points": ["grade points", "grade point"],
        "product": ["product"]
    }

    column_indexes = {}

    for field, possible_names in required_columns.items():

        for name in possible_names:
            if name in headers:
                column_indexes[field] = headers.index(name)
                break

    # Check required columns
    required_fields = ["code", "title", "credit_hours", "grade"]

    missing_fields = [
        field for field in required_fields
        if field not in column_indexes
    ]

    if missing_fields:
        raise ValueError(
            f"Missing required columns: {', '.join(missing_fields)}"
        )

    results = []

    # Process each course row
    for row in rows[1:]:

        if len(row) < len(headers):
            continue

        # Skip repeated header rows
        row_values = [
            cell.strip().lower()
            for cell in row
        ]

        if "code" in row_values and "grade" in row_values:
            continue

        course_code = row[column_indexes["code"]].strip().upper()
        course_name = row[column_indexes["title"]].strip()
        grade = row[column_indexes["grade"]].strip().upper()

        # Skip accidental column headings
        if course_code in ["CODE", "COURSE CODE"]:
            continue

        if grade == "GRADE":
            continue

        # Ignore invalid or empty rows
        if not course_code or not course_name or not grade:
            continue

        credit_hours = clean_number(
            row[column_indexes["credit_hours"]]
        )

        grade_points = None
        if "grade_points" in column_indexes:
            grade_points = clean_number(
                row[column_indexes["grade_points"]]
            )

        product = None
        if "product" in column_indexes:
            product = clean_number(
                row[column_indexes["product"]]
            )

        results.append({
            "course_code": course_code,
            "subject_name": course_name,
            "credit_hours": credit_hours,
            "grade": grade,
            "grade_points": grade_points,
            "product": product,
            "is_passed": check_passing_grade(grade)
        })

    if not results:
        raise ValueError("No valid courses could be extracted.")

    return results