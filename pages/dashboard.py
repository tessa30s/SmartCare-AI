import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Dashboard | SmartCare AI",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# LOGIN PROTECTION
# --------------------------------------------------

if not st.session_state.get("logged_in", False):
    st.warning("Please log in to access the dashboard.")

    if st.button("🔐 Go to Login"):
        st.switch_page("pages/login.py")

    st.stop()

# --------------------------------------------------
# CUSTOM STYLING
# --------------------------------------------------

st.markdown("""
<style>

.dashboard-header {
    padding: 25px 30px;
    border-radius: 18px;
    background: linear-gradient(
        135deg,
        #5B21B6,
        #7C3AED
    );
    color: white;
    margin-bottom: 30px;
}

.dashboard-header h1 {
    margin-bottom: 5px;
}

.dashboard-header p {
    margin: 0;
    font-size: 17px;
}

.metric-card {
    padding: 22px;
    border-radius: 16px;
    background: #F8F5FF;
    border: 1px solid #E9D5FF;
    text-align: center;
}

.metric-card h2 {
    color: #5B21B6;
}

.action-card {
    padding: 25px;
    border-radius: 18px;
    background: white;
    border: 1px solid #E5E7EB;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

username = st.session_state.get("username", "User")

st.markdown(
    f"""
    <div class="dashboard-header">

    <h1>Welcome back, {username}! 👋</h1>

    <p>
    SmartCare AI — Healthcare Intelligence Dashboard
    </p>

    </div>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# METRICS
# --------------------------------------------------

st.subheader("📊 SmartCare Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <h2>1,000</h2>
        <p>Training Records</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h2>89.5%</h2>
        <p>Model Accuracy</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <h2>100%</h2>
        <p>Readmission Recall</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <h2>94.14%</h2>
        <p>ROC-AUC</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --------------------------------------------------
# QUICK ACTIONS
# --------------------------------------------------

st.subheader("⚡ Quick Actions")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="action-card">

    ### 🩺 New Prediction

    Enter patient information and use the SmartCare
    machine learning model to estimate 30-day
    readmission risk.

    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "🔮 Start New Prediction",
        use_container_width=True
    ):
        st.switch_page("pages/prediction.py")

with col2:

    st.markdown("""
    <div class="action-card">

    ### 📋 Prediction History

    Review previous SmartCare AI predictions
    and their results.

    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "📋 View History",
        use_container_width=True
    ):
        st.switch_page("pages/history.py")

# --------------------------------------------------
# MODEL INFORMATION
# --------------------------------------------------

st.divider()

st.subheader("🤖 SmartCare AI Model")

st.write(
    "The current SmartCare AI system uses a Random Forest "
    "classification model to predict whether a patient "
    "will be readmitted within 30 days."
)

st.info(
    "The model achieved 89.5% accuracy, 100% recall, "
    "82.93% F1-score and 94.14% ROC-AUC on the test dataset."
)

# --------------------------------------------------
# LOGOUT
# --------------------------------------------------

st.divider()

if st.button("🚪 Logout"):

    st.session_state["logged_in"] = False
    st.session_state["username"] = None

    st.switch_page("pages/home.py")