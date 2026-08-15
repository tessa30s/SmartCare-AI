import streamlit as st

st.set_page_config(
    page_title="SmartCare AI",
    page_icon="🏥",
    layout="wide"
)

# --------------------------------------------------
# PAGE DEFINITIONS
# --------------------------------------------------

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

# --------------------------------------------------
# NAVIGATION
# --------------------------------------------------

pg = st.navigation([
    home,
    login,
    dashboard,
    prediction,
    results,
    history
])

# --------------------------------------------------
# RUN APP
# --------------------------------------------------

pg.run()