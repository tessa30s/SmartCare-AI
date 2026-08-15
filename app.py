import streamlit as st

st.set_page_config(
    page_title="SmartCare AI",
    page_icon="🏥",
    layout="wide"
)

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

pg = st.navigation([
    home,
    login,
    dashboard
])

pg.run()