import streamlit as st
import pandas as pd


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Prediction History | SmartCare AI",
    page_icon="📋",
    layout="wide"
)


# ==================================================
# LOGIN PROTECTION
# ==================================================

if not st.session_state.get("logged_in", False):

    st.warning(
        "Please log in to access prediction history."
    )

    if st.button("🔐 Go to Login"):

        st.switch_page(
            "pages/login.py"
        )

    st.stop()


# ==================================================
# HEADER
# ==================================================

st.title("📋 Prediction History")

st.write(
    "View predictions generated during your current "
    "SmartCare AI session."
)

st.divider()


# ==================================================
# CHECK HISTORY
# ==================================================

history = st.session_state.get(
    "prediction_history",
    []
)


if not history:

    st.info(
        "No predictions have been made yet."
    )

    if st.button(
        "🩺 Make Your First Prediction",
        use_container_width=True
    ):

        st.switch_page(
            "pages/prediction.py"
        )

    st.stop()


# ==================================================
# CONVERT TO DATAFRAME
# ==================================================

history_df = pd.DataFrame(
    history
)


# ==================================================
# SUMMARY
# ==================================================

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


st.subheader("📊 History Summary")

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Total Predictions",
        total_predictions
    )


with col2:

    st.metric(
        "High Risk",
        high_risk_count
    )


with col3:

    st.metric(
        "Medium Risk",
        medium_risk_count
    )


with col4:

    st.metric(
        "Low Risk",
        low_risk_count
    )


# ==================================================
# HISTORY TABLE
# ==================================================

st.divider()

st.subheader("🗂️ Previous Predictions")

display_df = history_df.copy()

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)


# ==================================================
# RISK DISTRIBUTION
# ==================================================

st.divider()

st.subheader("📈 Risk Distribution")

risk_counts = (
    history_df["Risk Level"]
    .value_counts()
)

st.bar_chart(
    risk_counts
)


# ==================================================
# ACTIONS
# ==================================================

st.divider()

col1, col2 = st.columns(2)


with col1:

    if st.button(
        "🩺 New Prediction",
        use_container_width=True
    ):

        st.switch_page(
            "pages/prediction.py"
        )


with col2:

    if st.button(
        "📊 Back to Dashboard",
        use_container_width=True
    ):

        st.switch_page(
            "pages/dashboard.py"
        )


# ==================================================
# DISCLAIMER
# ==================================================

st.divider()

st.caption(
    "⚠️ SmartCare AI is an educational and research "
    "prototype. Prediction history is stored only "
    "for the current application session."
)