import streamlit as st
import pandas as pd
import uuid
import logging

from src.rag.rag_chain import get_rag_chain
from src.advisor.marksheet_parser import parse_lms_results
from src.database.repository import (
    save_student_results,
    get_elective_eligibility
)


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Bahria AI Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "active_page" not in st.session_state:
    st.session_state.active_page = "Home"

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "university_chat" not in st.session_state:
    st.session_state.university_chat = []

if "parsed_results" not in st.session_state:
    st.session_state.parsed_results = None

if "eligibility_results" not in st.session_state:
    st.session_state.eligibility_results = None


# --------------------------------------------------
# CACHED RAG CHAIN
# --------------------------------------------------

@st.cache_resource
def load_rag_chain():
    return get_rag_chain()


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #F3F5EF;
    color: #29352B;
}

/* Main content spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #263329;
}

/* Sidebar branding */
.sidebar-brand {
    color: #DCE8CE !important;
    font-size: 25px;
    font-weight: 800;
    letter-spacing: 1px;
    padding: 15px 5px 25px 5px;
}

/* Sidebar text */
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] label {
    color: #E5EBDD;
}

/* Sidebar buttons */
section[data-testid="stSidebar"] button {
    border-radius: 8px;
    border: 1px solid #526B3D;
}

/* Main header */
.main-header {
    background: linear-gradient(135deg, #263C2B, #526B3D);
    color: white;
    padding: 28px;
    border-radius: 15px;
    margin-bottom: 25px;
}

.main-header h1 {
    color: white !important;
    margin-bottom: 8px;
}

.main-header p {
    color: #E5EBDD !important;
    margin-bottom: 0;
}

/* Service cards */
.service-card {
    background-color: white;
    border: 1px solid #DCE4D4;
    border-radius: 14px;
    padding: 25px;
    min-height: 180px;
}

.service-card h3 {
    color: #354B35;
}

.service-card p {
    color: #64715F;
}

/* Footer */
.app-footer {
    background-color: #263329;
    color: #E5EBDD;
    padding: 17px;
    text-align: center;
    border-radius: 10px;
    margin-top: 40px;
    font-size: 14px;
}

/* Buttons */
.stButton > button {
    background-color: #526B3D;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 8px 18px;
}

.stButton > button:hover {
    background-color: #354B35;
    color: white;
    border: none;
}

/* Input fields */
.stTextInput input,
.stTextArea textarea {
    border-radius: 8px;
}

/* Headings */
h1, h2, h3 {
    color: #354B35;
}

/* Hide Streamlit menu and footer */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------

def show_header(title, subtitle):
    st.markdown(f"""
    <div class="main-header">
        <h1>{title}</h1>
        <p>{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)


def show_footer():
    st.markdown("""
    <div class="app-footer">
        BAHRIA_AI &nbsp; | &nbsp; University Assistant
    </div>
    """, unsafe_allow_html=True)


def determine_pass_status(grade):
    """
    D and above are passing grades.
    F is failing.
    Unknown grades need verification.
    """

    if pd.isna(grade):
        return None

    grade = str(grade).strip().upper()

    passing_grades = {
        "A+", "A", "A-", "B+", "B", "B-",
        "C+", "C", "C-", "D"
    }

    if grade == "F":
        return False

    if grade in passing_grades:
        return True

    return None


# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------

with st.sidebar:

    st.markdown(
        '<div class="sidebar-brand"> BAHRIA AI</div>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.caption("MAIN MENU")

    if st.button("🏠  Home", use_container_width=True):
        st.session_state.active_page = "Home"
        st.rerun()

    if st.button("🤖  University AI", use_container_width=True):
        st.session_state.active_page = "University AI"
        st.rerun()

    if st.button("📚  Elective Guide", use_container_width=True):
        st.session_state.active_page = "Elective Guide"
        st.rerun()

    st.markdown("---")

    st.caption("SYSTEM INFORMATION")

    st.markdown("""
    <div style="
        background-color:#354438;
        padding:12px;
        border-radius:8px;
        color:#DCE8CE;
        font-size:13px;
    ">
        <p>● Gemini integration configured</p>
        <p>● Supabase database configured</p>
        <p>● Bahria AI Assistant</p>
    </div>
    """, unsafe_allow_html=True)


# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

if st.session_state.active_page == "Home":

    show_header(
        "BAHRIA UNIVERSITY ASSISTANT",
        "Your intelligent university companion"
    )

    st.markdown("## Welcome to Bahria AI")

    st.write(
        "A simple platform designed to help Bahria University "
        "students find academic information and understand elective eligibility."
    )

    st.markdown("## Explore our services")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="service-card">
            <h3>🤖 University AI</h3>
            <p>
                Ask questions about university rules, policies,
                academic procedures and the student handbook.
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "Open University AI",
            key="home_university_ai",
            use_container_width=True
        ):
            st.session_state.active_page = "University AI"
            st.rerun()

    with col2:

        st.markdown("""
        <div class="service-card">
            <h3>📚 Elective Guide</h3>
            <p>
                Paste your LMS results, review your courses
                and check which electives you are eligible to take.
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "Open Elective Guide",
            key="home_elective_guide",
            use_container_width=True
        ):
            st.session_state.active_page = "Elective Guide"
            st.rerun()

    show_footer()


# --------------------------------------------------
# UNIVERSITY AI PAGE
# --------------------------------------------------

elif st.session_state.active_page == "University AI":

    show_header(
        "UNIVERSITY AI",
        "Ask questions about Bahria University"
    )

    st.write(
        "Ask questions about university policies, academic rules "
        "and procedures. Answers are generated using the university documents."
    )

    # Display previous messages
    for message in st.session_state.university_chat:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

            if message.get("sources"):
                with st.expander("View document references"):
                    for source in message["sources"]:
                        page = source.metadata.get("page", "Unknown")
                        filename = source.metadata.get(
                            "source",
                            "University document"
                        )

                        st.write(f"📄 {filename} — Page {page}")

    # Chat input
    question = st.chat_input("Ask your university-related question...")

    if question:

        st.session_state.university_chat.append({
            "role": "user",
            "content": question
        })

        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):

            with st.spinner("Searching university documents..."):

                try:
                    rag_chain = load_rag_chain()
                    result = rag_chain(question)

                    answer = result["answer"]
                    sources = result.get("sources", [])

                    st.markdown(answer)

                    if sources:

                        with st.expander("View document references"):

                            seen_sources = set()

                            for source in sources:

                                page = source.metadata.get(
                                    "page",
                                    "Unknown"
                                )

                                filename = source.metadata.get(
                                    "source",
                                    "University document"
                                )

                                source_key = (filename, page)

                                if source_key not in seen_sources:
                                    st.write(
                                        f"📄 {filename} — Page {page}"
                                    )
                                    seen_sources.add(source_key)

                    st.session_state.university_chat.append({
                        "role": "assistant",
                        "content": answer,
                        "sources": sources
                    })

                except Exception as e:

                    logger.exception("University AI error")

                    error_message = (
                        "Sorry, I could not process your question. "
                        "Please try again."
                    )

                    st.error(error_message)

                    st.session_state.university_chat.append({
                        "role": "assistant",
                        "content": error_message
                    })

        st.rerun()

    if st.button("Clear conversation"):

        st.session_state.university_chat = []
        st.rerun()

    show_footer()


# --------------------------------------------------
# ELECTIVE GUIDE PAGE
# --------------------------------------------------

elif st.session_state.active_page == "Elective Guide":

    show_header(
        "ELECTIVE GUIDE",
        "Check your elective eligibility using your LMS results"
    )

    st.write(
        "Copy your academic results from LMS and paste them below. "
        "Review the extracted information before saving."
    )

    st.info(
        "Only passing grades are considered completed prerequisites. "
        "Grade D is considered a pass."
    )

    # Step 1: Paste LMS results
    st.markdown("### Step 1 — Paste your LMS results")

    raw_text = st.text_area(
        "LMS Results",
        height=220,
        placeholder="Paste your copied LMS result table here..."
    )

    if st.button("Parse Results", use_container_width=True):

        if not raw_text.strip():

            st.warning("Please paste your LMS results first.")

        else:

            try:

                records = parse_lms_results(raw_text)

                if not records:
                    st.warning("No course records were found.")

                else:

                    st.session_state.parsed_results = records
                    st.session_state.eligibility_results = None

                    st.success(
                        f"Successfully extracted {len(records)} courses."
                    )

                    st.rerun()

            except Exception:

                logger.exception("LMS parsing error")
                st.error(
                    "Could not parse your LMS results. "
                    "Please check the copied table format."
                )

    # Step 2: Review extracted results
    if st.session_state.parsed_results is not None:

        st.markdown("---")
        st.markdown("### Step 2 — Review your extracted results")

        df = pd.DataFrame(st.session_state.parsed_results)

        display_columns = [
            "course_code",
            "subject_name",
            "credit_hours",
            "grade",
            "grade_points",
            "product"
        ]

        # Keep only columns available in parsed records
        display_columns = [
            column for column in display_columns
            if column in df.columns
        ]

        edited_df = st.data_editor(
            df[display_columns],
            use_container_width=True,
            hide_index=True,
            num_rows="dynamic",
            key="lms_results_editor"
        )

        st.caption(
            "Check your course codes and grades carefully before saving."
        )

        # Step 3: Save results and check eligibility
        st.markdown("---")
        st.markdown("### Step 3 — Save and check eligibility")

        if st.button(
            "Save Results and Check Eligibility",
            use_container_width=True
        ):

            try:

                records = edited_df.to_dict(orient="records")

                # Recalculate pass status using the edited grades
                for record in records:

                    record["grade"] = (
                        str(record.get("grade", "")).strip().upper()
                    )

                    record["is_passed"] = determine_pass_status(
                        record["grade"]
                    )

                save_student_results(
                    st.session_state.session_id,
                    records
                )

                eligibility = get_elective_eligibility(
                    st.session_state.session_id
                )

                st.session_state.eligibility_results = eligibility

                st.success("Your results have been saved successfully.")

                st.rerun()

            except Exception:

                logger.exception("Elective eligibility error")

                st.error(
                    "Something went wrong while saving results "
                    "or checking eligibility."
                )

    # Step 4: Display eligibility
    if st.session_state.eligibility_results is not None:

        st.markdown("---")
        st.markdown("### Your Elective Eligibility")

        eligibility = st.session_state.eligibility_results

        if not eligibility:

            st.info("No elective records were returned.")

        else:

            eligible_count = sum(
                1 for item in eligibility
                if item.get("status") == "Eligible"
            )

            not_eligible_count = sum(
                1 for item in eligibility
                if item.get("status") == "Not eligible"
            )

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Eligible Electives", eligible_count)

            with col2:
                st.metric("Not Eligible", not_eligible_count)

            for item in eligibility:

                status = item.get("status", "Unknown")

                with st.expander(
                    f"{item.get('course_code', '')} — "
                    f"{item.get('course_name', '')} | {status}"
                ):

                    st.write(
                        f"**Credit Hours:** "
                        f"{item.get('credit_hours', 'N/A')}"
                    )

                    st.write(
                        f"**Prerequisites:** "
                        f"{item.get('prerequisites', 'None')}"
                    )

                    if item.get("failed"):
                        st.error(
                            "Failed prerequisites: "
                            + ", ".join(item["failed"])
                        )

                    if item.get("missing"):
                        st.warning(
                            "Prerequisites not found: "
                            + ", ".join(item["missing"])
                        )

                    if item.get("verification"):
                        st.warning(
                            "Needs verification: "
                            + ", ".join(item["verification"])
                        )

                    if status == "Eligible":
                        st.success("You meet the prerequisite requirements.")

                    elif status == "Not eligible":
                        st.error("You do not currently meet the requirements.")

                    elif status == "Prerequisite not found":
                        st.warning(
                            "Some prerequisite courses were not found "
                            "in your submitted results."
                        )

                    elif status == "Needs verification":
                        st.warning(
                            "Some course information needs to be checked."
                        )

    show_footer()