
import streamlit as st

# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="Bahria Assistant AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- SESSION STATE ----------------

if "active_page" not in st.session_state:
    st.session_state.active_page = "Home"


# ---------------- NAVIGATION CALLBACK ----------------

def navigate_to(page):
    st.session_state.active_page = page


# ---------------- CUSTOM CSS ----------------


# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

/* Main application background */
.stApp {
    background-color: #f5f7fb;
}

/* Main content */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Main heading */
.main-title {
    font-size: 38px;
    font-weight: 800;
    color: #173b67 !important;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 17px;
    color: #64748b !important;
}

/* Welcome banner */
.hero {
    background: linear-gradient(120deg, #173b67, #2563a6);
    padding: 35px;
    border-radius: 18px;
    color: white !important;
    margin-top: 20px;
    margin-bottom: 25px;
}

.hero h2,
.hero p {
    color: white !important;
}

.hero h2 {
    font-size: 29px;
}

.hero p {
    font-size: 16px;
}

/* Feature cards */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #ffffff !important;
    border-radius: 15px;
    border: 1px solid #e2e8f0;
    color: #173b67 !important;
}

/* Card text */
div[data-testid="stVerticalBlockBorderWrapper"] h1,
div[data-testid="stVerticalBlockBorderWrapper"] h2,
div[data-testid="stVerticalBlockBorderWrapper"] h3,
div[data-testid="stVerticalBlockBorderWrapper"] p,
div[data-testid="stVerticalBlockBorderWrapper"] span {
    color: #173b67 !important;
}

/* General text */
.stApp p,
.stApp label,
.stApp .stMarkdown {
    color: #26384d;
}

/* Buttons */
.stButton > button {
    background-color: #ffffff;
    border-radius: 9px;
    font-weight: 600;
    min-height: 42px;
    border: 1px solid #2563a6;
    color: #173b67 !important;
}

.stButton > button:hover {
    background-color: #173b67 !important;
    color: #ffffff !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #edf2f8 !important;
}

section[data-testid="stSidebar"] * {
    color: #173b67;
}

/* Footer */
.footer {
    text-align: center;
    color: #64748b !important;
    padding: 25px;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ----------------

pages = [
    "Home",
    "University AI",
    "Elective Guide",
    "Timetable",
    "Academic Advisor"
]

with st.sidebar:

    st.title("🎓 Bahria Assisitant AI")

    st.caption("Your University Companion")

    st.divider()

    st.subheader("Navigation")

    st.radio(
        "Select a service",
        pages,
        key="active_page",
        label_visibility="collapsed"
    )

    st.divider()

    st.markdown("### 💡 Quick Information")

    st.info(
        "Your AI-powered platform for "
        "university information and academic guidance."
    )

    st.markdown("---")

    st.caption("Bahria Assistant AI | Version 1.0")


# ---------------- HEADER ----------------

st.markdown(
    '<div class="main-title">🎓 Bahria Assistant AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Your intelligent university companion.'
    '</div>',
    unsafe_allow_html=True
)


# ---------------- HOME PAGE ----------------

if st.session_state.active_page == "Home":

    st.markdown("""
    <div class="hero">
        <h2>Welcome to Bahria Assistant AI 👋</h2>
        <p>
            Your personal AI-powered university assistant.
            Find academic information, explore elective subjects,
            check timetables and get academic guidance.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🚀 Explore University Services")

    st.write("Select a service to get started.")

    # First row
    col1, col2 = st.columns(2)

    with col1:

        with st.container(border=True):

            st.markdown("## 💬 University AI")

            st.write(
                "Ask questions about university policies, "
                "handbooks, academic rules and regulations."
            )

            st.button(
                "Explore University AI →",
                key="university_btn",
                use_container_width=True,
                on_click=navigate_to,
                args=("University AI",)
            )

    with col2:

        with st.container(border=True):

            st.markdown("## 📚 Elective Guide")

            st.write(
                "Explore available elective subjects "
                "and understand their course information."
            )

            st.button(
                "Explore Electives →",
                key="elective_btn",
                use_container_width=True,
                on_click=navigate_to,
                args=("Elective Guide",)
            )

    st.write("")

    # Second row
    col3, col4 = st.columns(2)

    with col3:

        with st.container(border=True):

            st.markdown("## 📅 Timetable Assistant")

            st.write(
                "Find class schedules and access "
                "important timetable information."
            )

            st.button(
                "View Timetable →",
                key="timetable_btn",
                use_container_width=True,
                on_click=navigate_to,
                args=("Timetable",)
            )

    with col4:

        with st.container(border=True):

            st.markdown("## 🧠 Academic Advisor")

            st.write(
                "Get academic guidance and explore "
                "elective recommendations based on your grades."
            )

            st.button(
                "Get Guidance →",
                key="advisor_btn",
                use_container_width=True,
                on_click=navigate_to,
                args=("Academic Advisor",)
            )

    st.divider()

    st.subheader("✨ Quick Question")

    st.write(
        "Have a university-related question? "
        "Start by exploring the University AI section."
    )

    st.button(
        "Open University AI",
        key="quick_ai_btn",
        type="primary",
        on_click=navigate_to,
        args=("University AI",)
    )


# ---------------- UNIVERSITY AI PAGE ----------------

elif st.session_state.active_page == "University AI":

    st.title("💬 University AI")

    st.write(
        "Ask questions about Bahria University "
        "using official university documents."
    )

    question = st.text_input(
        "Enter your question",
        placeholder="e.g. What are the attendance requirements?"
    )

    if st.button("Ask AI", type="primary"):

        if question.strip():

            st.info(
                "Your question is ready. "
                "The RAG and Gemini response pipeline "
                "will be connected in the next development phase."
            )

        else:

            st.warning("Please enter a question.")


# ---------------- ELECTIVE GUIDE PAGE ----------------

elif st.session_state.active_page == "Elective Guide":

    st.title("📚 Elective Subject Guide")

    st.write(
        "Explore elective subjects offered by your department."
    )

    department = st.selectbox(
        "Select Department",
        [
            "Computer Science",
            "Software Engineering",
            "AI",
            "Other"
        ]
    )

    semester = st.selectbox(
        "Select Semester",
        list(range(1, 9))
    )

    st.info(
        f"Selected Department: {department} | "
        f"Semester: {semester}"
    )

    st.caption(
        "Elective subject data will be connected in a future module."
    )


# ---------------- TIMETABLE PAGE ----------------

elif st.session_state.active_page == "Timetable":

    st.title("📅 Timetable Assistant")

    st.write(
        "Access your university class schedule."
    )

    semester = st.selectbox(
        "Select Semester",
        list(range(1, 9))
    )

    st.info(
        f"Selected Semester: {semester}"
    )

    st.caption(
        "Timetable document processing will be connected here."
    )


# ---------------- ACADEMIC ADVISOR PAGE ----------------

elif st.session_state.active_page == "Academic Advisor":

    st.title("🧠 Academic Advisor")

    st.write(
        "Get academic guidance and elective recommendations."
    )

    cgpa = st.number_input(
        "Enter your CGPA",
        min_value=0.0,
        max_value=4.0,
        value=3.0,
        step=0.1
    )

    interest = st.selectbox(
        "Select your area of interest",
        [
            "Machine Learning",
            "Data Science",
            "Artificial Intelligence",
            "Software Development",
            "Cyber Security"
        ]
    )

    if st.button("Get Recommendations", type="primary"):

        st.info(
            f"Your CGPA: {cgpa} | Interest: {interest}"
        )

        st.caption(
            "The academic recommendation engine "
            "will be integrated in a future development phase."
        )


# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer">
    <hr>
    Bahria Assistant AI © 2026 |
    Built to make university life easier 🎓
</div>
""", unsafe_allow_html=True)
