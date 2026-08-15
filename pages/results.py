import streamlit as st
import pandas as pd
import numpy as np
import joblib
import shap


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Prediction Result | SmartCare AI",
    page_icon="🔍",
    layout="wide"
)


# =========================================================
# LOGIN PROTECTION
# =========================================================

if not st.session_state.get("logged_in", False):

    st.warning(
        "Please log in to access prediction results."
    )

    if st.button(
        "🔐 Go to Login",
        use_container_width=True
    ):
        st.switch_page(
            "pages/login.py"
        )

    st.stop()


# =========================================================
# CHECK PREDICTION
# =========================================================

if "prediction" not in st.session_state:

    st.html("""
    <style>

    .empty-result {

        padding: 60px 30px;

        text-align: center;

        border-radius: 22px;

        background:
            linear-gradient(
                145deg,
                #111A35,
                #0B1228
            );

        border: 1px solid #29385E;

        margin-top: 40px;
    }

    .empty-icon {

        font-size: 55px;

        margin-bottom: 15px;
    }

    .empty-title {

        color: #F8FAFC;

        font-size: 25px;

        font-weight: 750;
    }

    .empty-text {

        color: #94A3B8;

        margin-top: 8px;
    }

    </style>
    """)

    st.html("""
    <div class="empty-result">

        <div class="empty-icon">
            🔍
        </div>

        <div class="empty-title">
            No Prediction Available
        </div>

        <div class="empty-text">
            Enter patient information and generate
            a prediction first.
        </div>

    </div>
    """)

    st.write("")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        if st.button(
            "🩺 Make a New Prediction",
            use_container_width=True
        ):

            st.switch_page(
                "pages/prediction.py"
            )

    st.stop()


# =========================================================
# GET STORED DATA
# =========================================================

prediction = int(
    st.session_state["prediction"]
)

probability = float(
    st.session_state["probability"]
)

input_data = st.session_state.get(
    "input_data"
)


# =========================================================
# LOAD MODEL
# =========================================================

try:

    model = joblib.load(
        "models/smartcare_random_forest.pkl"
    )

    preprocessor = joblib.load(
        "models/preprocessor.joblib"
    )

except Exception as e:

    st.error(
        "Unable to load the SmartCare AI model."
    )

    st.exception(e)

    st.stop()


# =========================================================
# PAGE STYLING
# =========================================================

st.html("""
<style>

/* =====================================================
   GLOBAL
===================================================== */

.stApp {

    background:

        radial-gradient(
            circle at 80% 5%,
            rgba(124, 58, 237, 0.16),
            transparent 30%
        ),

        radial-gradient(
            circle at 15% 90%,
            rgba(37, 99, 235, 0.08),
            transparent 30%
        ),

        #060B18;

    color: #F8FAFC;
}


.block-container {

    max-width: 1250px;

    padding-top: 1.5rem;

    padding-bottom: 4rem;
}


/* =====================================================
   HEADER
===================================================== */

.result-header {

    padding: 25px 30px;

    border-radius: 22px;

    background:

        linear-gradient(
            135deg,
            #111A3B,
            #171142,
            #25104A
        );

    border: 1px solid #303B68;

    margin-bottom: 18px;
}


.result-badge {

    display: inline-block;

    padding: 6px 12px;

    border-radius: 30px;

    background:
        rgba(124, 58, 237, 0.15);

    border:
        1px solid
        rgba(168, 85, 247, 0.35);

    color: #C4B5FD;

    font-size: 11px;

    font-weight: 700;

    letter-spacing: 0.7px;
}


.result-title {

    margin-top: 10px;

    font-size: 34px;

    font-weight: 800;

    color: #F8FAFC;
}


.result-title span {

    color: #A855F7;
}


.result-description {

    margin-top: 7px;

    color: #94A3B8;

    font-size: 13px;
}


/* =====================================================
   MAIN RESULT CARD
===================================================== */

.result-card {

    padding: 30px;

    border-radius: 22px;

    text-align: center;

    margin-top: 15px;

    margin-bottom: 18px;

    background:

        radial-gradient(
            circle at 50% 0%,
            rgba(124, 58, 237, 0.20),
            transparent 55%
        ),

        linear-gradient(
            145deg,
            #111A35,
            #0B1227
        );

    border: 1px solid #303D67;
}


.result-icon {

    font-size: 48px;

    margin-bottom: 8px;
}


.result-label {

    font-size: 14px;

    color: #94A3B8;

    text-transform: uppercase;

    letter-spacing: 1px;
}


.result-status {

    font-size: 31px;

    font-weight: 800;

    margin-top: 7px;
}


.result-probability {

    font-size: 45px;

    font-weight: 850;

    margin-top: 8px;

    color: #C4B5FD;
}


.result-description-text {

    color: #94A3B8;

    font-size: 13px;

    margin-top: 7px;
}


/* =====================================================
   RISK COLORS
===================================================== */

.risk-high {

    color: #FB7185;
}


.risk-medium {

    color: #FBBF24;
}


.risk-low {

    color: #34D399;
}


/* =====================================================
   SUMMARY CARDS
===================================================== */

.summary-card {

    padding: 20px;

    border-radius: 17px;

    background:
        #0E172E;

    border:
        1px solid #29385D;

    min-height: 115px;
}


.summary-label {

    color: #71809A;

    font-size: 11px;

    text-transform: uppercase;

    letter-spacing: 0.7px;
}


.summary-value {

    color: #F8FAFC;

    font-size: 22px;

    font-weight: 750;

    margin-top: 8px;
}


/* =====================================================
   SECTION
===================================================== */

.section-card {

    padding: 22px 24px;

    border-radius: 18px;

    background:

        linear-gradient(
            145deg,
            rgba(15, 25, 52, 0.96),
            rgba(8, 17, 35, 0.96)
        );

    border: 1px solid #27385D;

    margin-top: 18px;
}


.section-title {

    color: #F8FAFC;

    font-size: 19px;

    font-weight: 750;

    margin-bottom: 5px;
}


.section-description {

    color: #71809A;

    font-size: 12px;

    margin-bottom: 17px;
}


/* =====================================================
   SHAP FEATURE
===================================================== */

.shap-positive {

    color: #FB7185;

    font-weight: 600;
}


.shap-negative {

    color: #34D399;

    font-weight: 600;
}


/* =====================================================
   BUTTONS
===================================================== */

.stButton > button {

    min-height: 45px;

    border-radius: 11px !important;

    background:
        #111A32 !important;

    border:
        1px solid #35466D !important;

    color:
        #E2E8F0 !important;

    font-weight:
        600 !important;
}


.stButton > button:hover {

    border-color:
        #8B5CF6 !important;

    background:
        #1A1330 !important;

    color: white !important;
}


/* =====================================================
   DISCLAIMER
===================================================== */

.disclaimer {

    margin-top: 22px;

    padding: 14px 17px;

    border-radius: 12px;

    background:
        rgba(15, 23, 42, 0.75);

    border: 1px solid #273653;

    color: #71809A;

    font-size: 11px;

    line-height: 1.6;
}

</style>
""")


# =========================================================
# DETERMINE RISK
# =========================================================

if probability >= 70:

    risk_level = "High"

    risk_class = "risk-high"

    risk_icon = "🔴"

elif probability >= 40:

    risk_level = "Medium"

    risk_class = "risk-medium"

    risk_icon = "🟠"

else:

    risk_level = "Low"

    risk_class = "risk-low"

    risk_icon = "🟢"


# =========================================================
# HEADER
# =========================================================

st.html("""
<div class="result-header">

    <div class="result-badge">
        ✦ AI PREDICTION COMPLETE
    </div>

    <div class="result-title">
        Prediction <span>Result</span>
    </div>

    <div class="result-description">
        SmartCare AI has analyzed the patient's
        information using the trained Random Forest model.
    </div>

</div>
""")


# =========================================================
# MAIN RESULT
# =========================================================

if prediction == 1:

    status = "Readmission Predicted"

    result_description = (
        "The model predicts that the patient has "
        "a higher likelihood of being readmitted "
        "within 30 days."
    )

    result_icon = "⚠️"

else:

    status = "Not Readmitted"

    result_description = (
        "The model predicts that the patient has "
        "a lower likelihood of being readmitted "
        "within 30 days."
    )

    result_icon = "✓"


st.html(
    f"""
    <div class="result-card">

        <div class="result-icon">
            {result_icon}
        </div>

        <div class="result-label">
            Prediction Outcome
        </div>

        <div class="result-status {risk_class}">
            {status}
        </div>

        <div class="result-probability">
            {probability:.2f}%
        </div>

        <div class="result-description-text">
            {result_description}
        </div>

    </div>
    """
)


# =========================================================
# SUMMARY
# =========================================================

st.html("""
<div class="section-card">

    <div class="section-title">
        📊 Prediction Summary
    </div>

    <div class="section-description">
        Overview of the generated prediction.
    </div>

</div>
""")


col1, col2, col3 = st.columns(3)


with col1:

    st.html(
        f"""
        <div class="summary-card">

            <div class="summary-label">
                Prediction
            </div>

            <div class="summary-value">
                {"Readmitted" if prediction == 1 else "Not Readmitted"}
            </div>

        </div>
        """
    )


with col2:

    st.html(
        f"""
        <div class="summary-card">

            <div class="summary-label">
                Readmission Probability
            </div>

            <div class="summary-value">
                {probability:.2f}%
            </div>

        </div>
        """
    )


with col3:

    st.html(
        f"""
        <div class="summary-card">

            <div class="summary-label">
                Risk Level
            </div>

            <div class="summary-value {risk_class}">
                {risk_icon} {risk_level}
            </div>

        </div>
        """
    )


# =========================================================
# PROBABILITY
# =========================================================

st.html("""
<div class="section-card">

    <div class="section-title">
        📈 Readmission Probability
    </div>

    <div class="section-description">
        Estimated likelihood of 30-day patient readmission.
    </div>

</div>
""")


st.progress(
    min(
        max(probability / 100, 0.0),
        1.0
    )
)

st.caption(
    f"Estimated 30-day readmission probability: "
    f"{probability:.2f}%"
)


# =========================================================
# PATIENT INFORMATION
# =========================================================

if input_data is not None:

    st.html("""
    <div class="section-card">

        <div class="section-title">
            👤 Patient Information
        </div>

        <div class="section-description">
            Information used by the SmartCare AI model.
        </div>

    </div>
    """)

    with st.expander(
        "View Patient Data"
    ):

        st.dataframe(
            input_data,
            use_container_width=True,
            hide_index=True
        )


# =========================================================
# SHAP EXPLAINABLE AI
# =========================================================

st.html("""
<div class="section-card">

    <div class="section-title">
        🧠 Explainable AI
    </div>

    <div class="section-description">
        SHAP identifies the patient features that
        contributed most strongly to this prediction.
    </div>

</div>
""")


if input_data is not None:

    try:

        # -------------------------------------------------
        # PREPROCESS
        # -------------------------------------------------

        processed_input = preprocessor.transform(
            input_data
        )


        # -------------------------------------------------
        # FEATURE NAMES
        # -------------------------------------------------

        feature_names = (
            preprocessor
            .get_feature_names_out()
        )


        # -------------------------------------------------
        # SHAP EXPLAINER
        # -------------------------------------------------

        explainer = shap.TreeExplainer(
            model
        )


        shap_values = explainer.shap_values(
            processed_input
        )


        # -------------------------------------------------
        # HANDLE SHAP FORMAT
        # -------------------------------------------------

        if isinstance(
            shap_values,
            list
        ):

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


        # -------------------------------------------------
        # CREATE DATAFRAME
        # -------------------------------------------------

        explanation_df = pd.DataFrame({

            "Feature":
                feature_names,

            "SHAP Value":
                shap_for_prediction,

            "Absolute Impact":
                np.abs(shap_for_prediction)

        })


        # -------------------------------------------------
        # TOP FEATURES
        # -------------------------------------------------

        explanation_df = (
            explanation_df
            .sort_values(
                "Absolute Impact",
                ascending=False
            )
            .head(10)
        )


        display_df = explanation_df[
            [
                "Feature",
                "SHAP Value"
            ]
        ].copy()


        display_df["Impact"] = (
            display_df["SHAP Value"]
            .apply(
                lambda x:
                "⬆️ Increases risk"
                if x > 0
                else
                "⬇️ Decreases risk"
            )
        )


        st.success(
            "✓ SHAP explanation generated successfully."
        )


        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True
        )


        # -------------------------------------------------
        # SHAP CHART
        # -------------------------------------------------

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

        st.caption(
            "The prediction itself is still valid."
        )


# =========================================================
# ACTIONS
# =========================================================

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


# =========================================================
# DISCLAIMER
# =========================================================

st.html("""
<div class="disclaimer">

    ⚠️ <strong>SmartCare AI</strong> is an educational
    and research prototype. Predictions are intended for
    decision-support purposes only and should not replace
    professional medical judgment or clinical diagnosis.

</div>
""")