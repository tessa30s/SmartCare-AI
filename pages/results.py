import streamlit as st
import pandas as pd
import numpy as np
import joblib
import shap


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Prediction Result | SmartCare AI",
    page_icon="🔍",
    layout="wide"
)


# ==================================================
# LOGIN PROTECTION
# ==================================================

if not st.session_state.get("logged_in", False):

    st.warning(
        "Please log in to access prediction results."
    )

    if st.button("🔐 Go to Login"):

        st.switch_page(
            "pages/login.py"
        )

    st.stop()


# ==================================================
# CHECK PREDICTION
# ==================================================

if "prediction" not in st.session_state:

    st.warning(
        "No prediction is available yet."
    )

    if st.button("🩺 Make a New Prediction"):

        st.switch_page(
            "pages/prediction.py"
        )

    st.stop()


# ==================================================
# GET STORED DATA
# ==================================================

prediction = st.session_state["prediction"]

probability = st.session_state["probability"]

input_data = st.session_state.get(
    "input_data"
)


# ==================================================
# LOAD MODEL AND PREPROCESSOR
# ==================================================

try:

    model = joblib.load(
        "models/smartcare_random_forest.pkl"
    )

    preprocessor = joblib.load(
        "models/preprocessor.joblib"
    )

except Exception as e:

    st.error(
        "Unable to load the AI model."
    )

    st.exception(e)

    st.stop()


# ==================================================
# HEADER
# ==================================================

st.title(
    "🔍 SmartCare AI — Prediction Result"
)

st.write(
    "The prediction below was generated using "
    "the trained SmartCare AI Random Forest model."
)

st.divider()


# ==================================================
# RISK LEVEL
# ==================================================

if probability >= 70:

    risk_level = "High"

elif probability >= 40:

    risk_level = "Medium"

else:

    risk_level = "Low"


# ==================================================
# MAIN RESULT
# ==================================================

if prediction == 1:

    st.error(
        f"""
        ## ⚠️ Higher Readmission Risk

        ### {probability:.2f}% probability

        The model predicts a higher likelihood of
        readmission within 30 days.
        """
    )

else:

    st.success(
        f"""
        ## ✅ Lower Readmission Risk

        ### {probability:.2f}% probability

        The model predicts a lower likelihood of
        readmission within 30 days.
        """
    )


# ==================================================
# SUMMARY METRICS
# ==================================================

st.subheader(
    "📊 Prediction Summary"
)

col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Prediction",
        "Readmitted"
        if prediction == 1
        else "Not Readmitted"
    )


with col2:

    st.metric(
        "Readmission Probability",
        f"{probability:.2f}%"
    )


with col3:

    st.metric(
        "Risk Level",
        risk_level
    )


# ==================================================
# PROBABILITY
# ==================================================

st.subheader(
    "📈 Readmission Probability"
)

st.progress(
    min(
        max(
            probability / 100,
            0.0
        ),
        1.0
    )
)

st.caption(
    f"Estimated probability of 30-day readmission: "
    f"{probability:.2f}%"
)


# ==================================================
# PATIENT INFORMATION
# ==================================================

if input_data is not None:

    st.divider()

    st.subheader(
        "👤 Patient Information"
    )

    with st.expander(
        "View Patient Information"
    ):

        st.dataframe(
            input_data,
            use_container_width=True
        )


# ==================================================
# SHAP EXPLAINABLE AI
# ==================================================

st.divider()

st.subheader(
    "🧠 Explainable AI"
)

st.write(
    "SHAP explains how individual patient features "
    "contributed to this prediction."
)


try:

    # ----------------------------------------------
    # PREPROCESS PATIENT INPUT
    # ----------------------------------------------

    processed_input = preprocessor.transform(
        input_data
    )


    # ----------------------------------------------
    # GET FEATURE NAMES
    # ----------------------------------------------

    feature_names = (
        preprocessor.get_feature_names_out()
    )


    # ----------------------------------------------
    # CREATE SHAP EXPLAINER
    # ----------------------------------------------

    explainer = shap.TreeExplainer(
        model
    )


    # ----------------------------------------------
    # CALCULATE SHAP VALUES
    # ----------------------------------------------

    shap_values = explainer.shap_values(
        processed_input
    )


    # ----------------------------------------------
    # HANDLE SHAP OUTPUT FORMAT
    # ----------------------------------------------

    if isinstance(shap_values, list):

        shap_for_prediction = np.asarray(
            shap_values[prediction][0]
        )

    else:

        shap_array = np.asarray(
            shap_values
        )

        if shap_array.ndim == 3:

            shap_for_prediction = (
                shap_array[0, :, prediction]
            )

        else:

            shap_for_prediction = (
                shap_array[0]
            )


    # ----------------------------------------------
    # CREATE EXPLANATION DATAFRAME
    # ----------------------------------------------

    explanation_df = pd.DataFrame({

        "Feature": feature_names,

        "SHAP Value": shap_for_prediction,

        "Absolute Impact":
            np.abs(shap_for_prediction)

    })


    # ----------------------------------------------
    # SORT BY IMPORTANCE
    # ----------------------------------------------

    explanation_df = (
        explanation_df
        .sort_values(
            "Absolute Impact",
            ascending=False
        )
        .head(10)
    )


    # ----------------------------------------------
    # DISPLAY TOP FEATURES
    # ----------------------------------------------

    st.success(
        "SHAP explanation generated successfully."
    )

    st.write(
        "Top factors influencing this prediction:"
    )

    display_df = explanation_df[
        [
            "Feature",
            "SHAP Value"
        ]
    ].copy()

    display_df["Impact"] = display_df[
        "SHAP Value"
    ].apply(
        lambda x:
        "⬆️ Increases risk"
        if x > 0
        else "⬇️ Decreases risk"
    )


    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )


    # ----------------------------------------------
    # SHAP BAR CHART
    # ----------------------------------------------

    st.write(
        "### Feature Contribution"
    )

    chart_df = (
        explanation_df
        .set_index("Feature")[
            "SHAP Value"
        ]
        .sort_values()
    )

    st.bar_chart(
        chart_df
    )


except Exception as e:

    st.warning(
        "SHAP explanation could not be generated."
    )

    st.exception(e)


# ==================================================
# ACTION BUTTONS
# ==================================================

st.divider()

col1, col2 = st.columns(2)


with col1:

    if st.button(
        "🩺 New Prediction",
        use_container_width=True
    ):

        st.session_state.pop(
            "prediction",
            None
        )

        st.session_state.pop(
            "probability",
            None
        )

        st.session_state.pop(
            "input_data",
            None
        )

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
    "prototype. Predictions should not replace "
    "professional medical judgment or clinical diagnosis."
)