import streamlit as st
import pandas as pd


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Dashboard | SmartCare AI",
    page_icon="📊",
    layout="wide"
)


# ==================================================
# LOGIN PROTECTION
# ==================================================

if not st.session_state.get("logged_in", False):

    st.warning(
        "Please log in to access the dashboard."
    )

    if st.button("🔐 Go to Login"):

        st.switch_page("pages/login.py")

    st.stop()


# ==================================================
# USER INFORMATION
# ==================================================

username = st.session_state.get(
    "username",
    "User"
)


# ==================================================
# PREDICTION HISTORY
# ==================================================

history = st.session_state.get(
    "prediction_history",
    []
)

history_df = pd.DataFrame(history)


# ==================================================
# CUSTOM STYLING
# ==================================================

st.markdown(
"""
<style>

.dashboard-header {
    padding: 30px;
    border-radius: 18px;
    background: linear-gradient(135deg, #5B21B6, #7C3AED);
    color: white;
    margin-bottom: 30px;
}

.dashboard-header h1 {
    margin: 0;
    color: white;
    font-size: 32px;
}

.dashboard-header p {
    margin-top: 8px;
    margin-bottom: 0;
    color: white;
    font-size: 17px;
}

.metric-card {
    padding: 22px;
    border-radius: 16px;
    background: #F8F5FF;
    border: 1px solid #E9D5FF;
    text-align: center;
    min-height: 120px;
}

.metric-card h2 {
    color: #5B21B6;
    margin: 0;
    font-size: 28px;
}

.metric-card p {
    margin-top: 8px;
    color: #444;
    font-size: 15px;
}

.action-card {
    padding: 25px;
    border-radius: 18px;
    background: white;
    border: 1px solid #E5E7EB;
    margin-bottom: 15px;
    min-height: 150px;
}

.action-card h3 {
    margin-top: 0;
    color: #5B21B6;
}

.action-card p {
    color: #555;
    line-height: 1.6;
}

</style>
""",
unsafe_allow_html=True
)


# ==================================================
# HEADER
# ==================================================

st.markdown(
f"""
<div class="dashboard-header">
<h1>Welcome back, {username}! 👋</h1>
<p>SmartCare AI — Healthcare Intelligence Dashboard</p>
</div>
""",
unsafe_allow_html=True
)


# ==================================================
# MODEL OVERVIEW
# ==================================================

st.subheader(
    "📊 SmartCare Overview"
)

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.markdown(
"""
<div class="metric-card">
<h2>1,000</h2>
<p>Training Records</p>
</div>
""",
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
"""
<div class="metric-card">
<h2>89.5%</h2>
<p>Model Accuracy</p>
</div>
""",
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
"""
<div class="metric-card">
<h2>100%</h2>
<p>Readmission Recall</p>
</div>
""",
        unsafe_allow_html=True
    )


with col4:

    st.markdown(
"""
<div class="metric-card">
<h2>94.14%</h2>
<p>ROC-AUC</p>
</div>
""",
        unsafe_allow_html=True
    )


# ==================================================
# LIVE PREDICTION OVERVIEW
# ==================================================

st.divider()

st.subheader(
    "📈 Live Prediction Overview"
)


if history:

    total_predictions = len(
        history_df
    )

    high_risk_count = len(
        history_df[
            history_df["Risk Level"] == "High"
        ]
    )

    medium_risk_count = len(
        history_df[
            history_df["Risk Level"] == "Medium"
        ]
    )

    low_risk_count = len(
        history_df[
            history_df["Risk Level"] == "Low"
        ]
    )

    average_probability = (
        history_df["Probability"].mean()
    )

else:

    total_predictions = 0
    high_risk_count = 0
    medium_risk_count = 0
    low_risk_count = 0
    average_probability = 0


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Total Predictions",
        total_predictions
    )


with col2:

    st.metric(
        "🔴 High Risk",
        high_risk_count
    )


with col3:

    st.metric(
        "🟠 Medium Risk",
        medium_risk_count
    )


with col4:

    st.metric(
        "🟢 Low Risk",
        low_risk_count
    )


st.caption(
    f"Average predicted readmission probability: "
    f"{average_probability:.2f}%"
)


# ==================================================
# RISK DISTRIBUTION
# ==================================================

if history:

    st.subheader(
        "📊 Current Risk Distribution"
    )

    risk_counts = (
        history_df["Risk Level"]
        .value_counts()
        .reindex(
            ["High", "Medium", "Low"],
            fill_value=0
        )
    )

    st.bar_chart(
        risk_counts
    )


# ==================================================
# QUICK ACTIONS
# ==================================================

st.divider()

st.subheader(
    "⚡ Quick Actions"
)

col1, col2 = st.columns(2)


with col1:

    st.markdown(
"""
<div class="action-card">
<h3>🩺 New Prediction</h3>
<p>
Enter patient information and use the SmartCare
machine learning model to estimate 30-day
readmission risk.
</p>
</div>
""",
        unsafe_allow_html=True
    )

    if st.button(
        "🔮 Start New Prediction",
        use_container_width=True
    ):

        st.switch_page(
            "pages/prediction.py"
        )


with col2:

    st.markdown(
"""
<div class="action-card">
<h3>📋 Prediction History</h3>
<p>
Review previous SmartCare AI predictions
and their results.
</p>
</div>
""",
        unsafe_allow_html=True
    )

    if st.button(
        "📋 View History",
        use_container_width=True
    ):

        st.switch_page(
            "pages/history.py"
        )


# ==================================================
# RECENT PREDICTIONS
# ==================================================

if history:

    st.divider()

    st.subheader(
        "🕒 Recent Predictions"
    )

    recent_df = history_df.tail(5)

    st.dataframe(
        recent_df,
        use_container_width=True,
        hide_index=True
    )

    if st.button(
        "📋 View All Predictions",
        use_container_width=True
    ):

        st.switch_page(
            "pages/history.py"
        )


else:

    st.divider()

    st.info(
        "No patient predictions have been generated "
        "yet. Start a new prediction to see live "
        "analytics here."
    )


# ==================================================
# MODEL INFORMATION
# ==================================================

st.divider()

st.subheader(
    "🤖 SmartCare AI Model"
)

st.write(
    "The current SmartCare AI system uses a Random "
    "Forest classification model to predict whether "
    "a patient will be readmitted within 30 days."
)

st.info(
    "The model achieved 89.5% accuracy, 100% recall, "
    "82.93% F1-score and 94.14% ROC-AUC on the "
    "test dataset."
)


# ==================================================
# SYSTEM STATUS
# ==================================================

st.divider()

st.subheader(
    "🟢 System Status"
)

col1, col2, col3 = st.columns(3)


with col1:

    st.success(
        "🤖 AI Model\n\nLoaded"
    )


with col2:

    st.success(
        "⚙️ Preprocessing\n\nReady"
    )


with col3:

    st.success(
        "🧠 SHAP\n\nAvailable"
    )


# ==================================================
# LOGOUT
# ==================================================

st.divider()

if st.button(
    "🚪 Logout",
    use_container_width=True
):

    st.session_state["logged_in"] = False

    st.session_state["username"] = None

    st.switch_page(
        "pages/home.py"
    )


# ==================================================
# DISCLAIMER
# ==================================================

st.divider()

st.caption(
    "⚠️ SmartCare AI is an educational and research "
    "prototype. Predictions should not replace "
    "professional medical judgment or clinical "
    "diagnosis."
)