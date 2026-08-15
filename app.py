import streamlit as st


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="SmartCare AI",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==================================================
# GLOBAL SMARTCARE THEME
# ==================================================

st.html("""
<style>

.stApp {
    background:
        radial-gradient(
            circle at 80% 10%,
            rgba(76, 29, 149, 0.16),
            transparent 30%
        ),
        radial-gradient(
            circle at 20% 90%,
            rgba(37, 99, 235, 0.10),
            transparent 28%
        ),
        #060B18;

    color: #F8FAFC;
}


.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* ==================================================
   SIDEBAR
================================================== */

section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #080F21 0%,
            #0A1225 55%,
            #080D1B 100%
        );

    border-right: 1px solid #202D4A;
}


section[data-testid="stSidebar"] > div {
    padding: 1.2rem 1rem;
}


/* ==================================================
   BRAND
================================================== */

.smartcare-brand {
    padding: 10px 8px 28px 8px;
    text-align: center;
}

.brand-icon {
    font-size: 42px;
    margin-bottom: 5px;
}

.brand-name {
    font-size: 25px;
    font-weight: 800;
    color: #F8FAFC;
    letter-spacing: -0.5px;
}

.brand-name span {
    color: #A855F7;
}

.brand-subtitle {
    color: #64748B;
    font-size: 11px;
    margin-top: 4px;
    letter-spacing: 1.2px;
    text-transform: uppercase;
}


/* ==================================================
   SIDEBAR NAVIGATION
================================================== */

section[data-testid="stSidebar"] .stPageLink {
    border-radius: 12px;
    margin: 5px 0;
    transition: all 0.2s ease;
}

section[data-testid="stSidebar"] .stPageLink:hover {
    background: rgba(124, 58, 237, 0.14);
}

section[data-testid="stSidebar"] .stPageLink a {
    color: #CBD5E1;
    font-size: 15px;
    font-weight: 500;
}


/* ==================================================
   HELP CARD
================================================== */

.help-card {
    margin-top: 80px;
    padding: 20px;
    border-radius: 18px;

    background:
        linear-gradient(
            145deg,
            rgba(30, 41, 74, 0.8),
            rgba(15, 23, 42, 0.9)
        );

    border: 1px solid #253454;
}

.help-icon {
    font-size: 27px;
    margin-bottom: 8px;
}

.help-title {
    color: #F8FAFC;
    font-size: 17px;
    font-weight: 700;
    margin-bottom: 8px;
}

.help-text {
    color: #94A3B8;
    font-size: 13px;
    line-height: 1.6;
}


/* ==================================================
   SIDEBAR FOOTER
================================================== */

.sidebar-footer {
    margin-top: 35px;
    padding: 10px;
    text-align: center;
    color: #475569;
    font-size: 11px;
}


/* ==================================================
   STREAMLIT BUTTONS
================================================== */

.stButton > button {
    border-radius: 12px;
    border: 1px solid #374151;
    background: #111827;
    color: #F8FAFC;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    border-color: #8B5CF6;
    color: white;
    background: #1A1330;
}


/* ==================================================
   HIDE DEFAULT ELEMENTS
================================================== */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}


/* ==================================================
   SIDEBAR COLLAPSE BUTTON
================================================== */

button[data-testid="stBaseButton-headerNoPadding"] {
    color: #CBD5E1;
}

</style>
""")


# ==================================================
# PAGE DEFINITIONS
# ==================================================

home = st.Page(
    "pages/home.py",
    title="Home",
    icon="🏠"
)

login = st.Page(
    "pages/login.py",
    title="Login",
    icon="🔐"
)

dashboard = st.Page(
    "pages/dashboard.py",
    title="Dashboard",
    icon="📊"
)

prediction = st.Page(
    "pages/prediction.py",
    title="New Prediction",
    icon="🩺"
)

results = st.Page(
    "pages/results.py",
    title="Results",
    icon="🔍"
)

history = st.Page(
    "pages/history.py",
    title="History",
    icon="📋"
)


# ==================================================
# NAVIGATION
# ==================================================

pg = st.navigation(
    [
        home,
        login,
        dashboard,
        prediction,
        results,
        history
    ],
    position="hidden"
)


# ==================================================
# CUSTOM SIDEBAR
# ==================================================

with st.sidebar:

    # ------------------------------
    # BRAND
    # ------------------------------

    st.html("""
    <div class="smartcare-brand">

        <div class="brand-icon">
            🏥
        </div>

        <div class="brand-name">
            SmartCare <span>AI</span>
        </div>

        <div class="brand-subtitle">
            Healthcare Intelligence
        </div>

    </div>
    """)


    # ------------------------------
    # NAVIGATION
    # ------------------------------

    st.page_link(
        home,
        label="Home",
        icon="🏠"
    )

    st.page_link(
        login,
        label="Login",
        icon="🔐"
    )

    st.page_link(
        dashboard,
        label="Dashboard",
        icon="📊"
    )

    st.page_link(
        prediction,
        label="New Prediction",
        icon="🩺"
    )

    st.page_link(
        results,
        label="Results",
        icon="🔍"
    )

    st.page_link(
        history,
        label="History",
        icon="📋"
    )


    # ------------------------------
    # HELP CARD
    # ------------------------------

    st.html("""
    <div class="help-card">

        <div class="help-icon">
            💜
        </div>

        <div class="help-title">
            Need help?
        </div>

        <div class="help-text">
            Explore SmartCare AI to make
            smarter healthcare decisions
            using machine learning.
        </div>

    </div>
    """)


    # ------------------------------
    # FOOTER
    # ------------------------------

    st.html("""
    <div class="sidebar-footer">

        SmartCare AI<br>
        © 2026 • Healthcare Intelligence

    </div>
    """)


# ==================================================
# RUN CURRENT PAGE
# ==================================================

pg.run()