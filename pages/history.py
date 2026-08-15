import streamlit as st
from datetime import datetime
import pandas as pd


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Prediction History | SmartCare AI",
    page_icon="📋",
    layout="wide"
)


# =========================================================
# LOGIN PROTECTION
# =========================================================

if not st.session_state.get("logged_in", False):

    st.warning("Please log in to access prediction history.")

    if st.button("🔐 Go to Login", use_container_width=True):
        st.switch_page("pages/login.py")

    st.stop()


# =========================================================
# SMARTCARE HISTORY THEME
# =========================================================

st.html("""
<style>

/* =====================================================
   PAGE
===================================================== */

.history-page {
    padding-top: 10px;
}


/* =====================================================
   HEADER
===================================================== */

.history-header {
    display: flex;
    justify-content: space-between;
    align-items: center;

    padding: 10px 5px 25px 5px;
}

.history-title-area {
    padding-top: 10px;
}

.history-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;

    width: 58px;
    height: 58px;

    border-radius: 16px;

    background:
        linear-gradient(
            135deg,
            #4C1D95,
            #7C3AED
        );

    box-shadow:
        0 8px 25px
        rgba(124, 58, 237, 0.30);

    font-size: 28px;

    margin-bottom: 12px;
}

.history-title {
    font-size: 43px;
    font-weight: 800;

    color: #F8FAFC;

    margin: 0;
    letter-spacing: -1px;
}

.history-title span {
    color: #A855F7;
}

.history-line {
    width: 80px;
    height: 4px;

    border-radius: 10px;

    background:
        linear-gradient(
            90deg,
            #A855F7,
            #3B82F6
        );

    margin-top: 12px;
}

.history-subtitle {
    color: #AAB6CC;
    font-size: 16px;
    margin-top: 16px;
}


/* =====================================================
   HEADER VISUAL
===================================================== */

.history-visual {
    width: 190px;
    height: 150px;

    border-radius: 28px;

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 88px;

    background:
        radial-gradient(
            circle,
            rgba(139, 92, 246, 0.28),
            rgba(10, 18, 40, 0.05) 70%
        );

    filter:
        drop-shadow(
            0 15px 25px
            rgba(124, 58, 237, 0.25)
        );
}


/* =====================================================
   MAIN HISTORY CARD
===================================================== */

.history-card {
    padding: 30px;

    border-radius: 22px;

    background:
        linear-gradient(
            145deg,
            rgba(20, 29, 57, 0.94),
            rgba(8, 15, 34, 0.96)
        );

    border:
        1px solid
        rgba(100, 116, 139, 0.28);

    box-shadow:
        0 15px 45px
        rgba(0, 0, 0, 0.20);

    margin-top: 10px;
}


/* =====================================================
   EMPTY STATE
===================================================== */

.empty-state {
    text-align: center;

    padding: 55px 20px 60px 20px;
}

.empty-icon {
    width: 105px;
    height: 105px;

    margin: 0 auto 22px auto;

    border-radius: 50%;

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 52px;

    background:
        radial-gradient(
            circle,
            rgba(139, 92, 246, 0.38),
            rgba(30, 41, 74, 0.15)
        );

    border:
        1px solid
        rgba(139, 92, 246, 0.35);

    box-shadow:
        0 0 40px
        rgba(139, 92, 246, 0.15);
}

.empty-title {
    color: #F8FAFC;

    font-size: 26px;
    font-weight: 750;

    margin-bottom: 10px;
}

.empty-text {
    color: #94A3B8;

    font-size: 15px;

    margin-bottom: 25px;
}

.ready-text {
    color: #A855F7;

    font-size: 14px;
    font-weight: 600;

    margin-bottom: 20px;
}


/* =====================================================
   HISTORY TABLE
===================================================== */

.table-title {
    color: #F8FAFC;

    font-size: 22px;
    font-weight: 750;

    margin-bottom: 18px;
}


/* =====================================================
   SUMMARY CARDS
===================================================== */

.summary-card {
    padding: 20px;

    border-radius: 18px;

    background:
        linear-gradient(
            145deg,
            rgba(20, 30, 58, 0.95),
            rgba(10, 18, 40, 0.95)
        );

    border:
        1px solid
        rgba(100, 116, 139, 0.25);
}

.summary-label {
    color: #94A3B8;
    font-size: 13px;

    margin-bottom: 7px;
}

.summary-value {
    color: #F8FAFC;

    font-size: 28px;
    font-weight: 800;
}

.summary-purple {
    color: #A855F7;
}

.summary-red {
    color: #FB7185;
}

.summary-orange {
    color: #FB923C;
}

.summary-green {
    color: #34D399;
}


/* =====================================================
   WHY TRACK SECTION
===================================================== */

.why-card {
    margin-top: 24px;

    padding: 30px;

    border-radius: 22px;

    background:
        linear-gradient(
            145deg,
            rgba(24, 34, 66, 0.94),
            rgba(9, 17, 38, 0.96)
        );

    border:
        1px solid
        rgba(100, 116, 139, 0.25);
}

.why-title {
    color: #F8FAFC;

    font-size: 22px;
    font-weight: 750;

    margin-bottom: 25px;
}

.feature-box {
    padding: 10px 18px;

    border-right:
        1px solid
        rgba(100, 116, 139, 0.20);
}

.feature-box:last-child {
    border-right: none;
}

.feature-icon {
    font-size: 25px;
    margin-bottom: 10px;
}

.feature-title {
    color: #F8FAFC;

    font-size: 15px;
    font-weight: 700;

    margin-bottom: 7px;
}

.feature-text {
    color: #94A3B8;

    font-size: 13px;

    line-height: 1.6;
}


/* =====================================================
   BUTTONS
===================================================== */

.stButton > button {

    min-height: 50px !important;

    border-radius: 13px !important;

    border:
        1px solid
        rgba(139, 92, 246, 0.55) !important;

    background:
        linear-gradient(
            135deg,
            #6D28D9,
            #9333EA,
            #2563EB
        ) !important;

    color: white !important;

    font-weight: 700 !important;

    box-shadow:
        0 8px 25px
        rgba(124, 58, 237, 0.28) !important;

    transition: all 0.2s ease !important;
}

.stButton > button:hover {

    transform: translateY(-2px) !important;

    box-shadow:
        0 12px 32px
        rgba(139, 92, 246, 0.42) !important;
}


/* =====================================================
   DATAFRAME
===================================================== */

[data-testid="stDataFrame"] {

    border-radius: 14px;

    overflow: hidden;
}


/* =====================================================
   DISCLAIMER
===================================================== */

.history-disclaimer {

    margin-top: 25px;

    padding: 16px 20px;

    border-radius: 14px;

    background:
        rgba(30, 41, 74, 0.55);

    border:
        1px solid
        rgba(100, 116, 139, 0.20);

    color: #7F8EA8;

    font-size: 12px;

    text-align: center;
}

</style>
""")


# =========================================================
# PAGE WRAPPER
# =========================================================

st.html("""
<div class="history-page">
</div>
""")


# =========================================================
# HEADER
# =========================================================

header_col1, header_col2 = st.columns([3.5, 1])

with header_col1:

    st.html("""
    <div class="history-title-area">

        <div class="history-icon">
            📋
        </div>

        <h1 class="history-title">
            Prediction History
        </h1>

        <div class="history-line"></div>

        <div class="history-subtitle">
            View predictions generated during your
            SmartCare AI session.
        </div>

    </div>
    """)


with header_col2:

    st.html("""
    <div class="history-visual">
        🩺
    </div>
    """)


# =========================================================
# GET HISTORY
# =========================================================

history = st.session_state.get(
    "prediction_history",
    []
)


# =========================================================
# FALLBACK — CURRENT PREDICTION
# =========================================================

# This allows the page to still work even if the
# history list has not yet been created.

if (
    not history
    and "prediction" in st.session_state
):

    current_prediction = st.session_state.get(
        "prediction"
    )

    current_probability = st.session_state.get(
        "probability",
        0.0
    )

    current_input = st.session_state.get(
        "input_data"
    )

    history = [{
        "id": "SC-0001",
        "timestamp": datetime.now().strftime(
            "%Y-%m-%d %H:%M"
        ),
        "prediction": int(
            current_prediction
        ),
        "probability": float(
            current_probability
        ),
        "input_data": current_input
    }]


# =========================================================
# EMPTY HISTORY
# =========================================================

if not history:

    st.html("""
    <div class="history-card">

        <div class="empty-state">

            <div class="empty-icon">
                📦
            </div>

            <div class="empty-title">
                No predictions yet
            </div>

            <div class="empty-text">
                You haven't made any predictions
                in this session.
            </div>

            <div class="ready-text">
                ───── &nbsp; Ready to get started? &nbsp; ─────
            </div>

        </div>

    </div>
    """)

    empty_col1, empty_col2, empty_col3 = st.columns(
        [1, 2, 1]
    )

    with empty_col2:

        if st.button(
            "🩺  Make Your First Prediction  →",
            use_container_width=True
        ):

            st.switch_page(
                "pages/prediction.py"
            )


# =========================================================
# HISTORY AVAILABLE
# =========================================================

else:

    # -----------------------------------------------------
    # PREPARE SUMMARY
    # -----------------------------------------------------

    total_predictions = len(history)

    high_risk = 0
    medium_risk = 0
    low_risk = 0

    table_rows = []

    for index, item in enumerate(history):

        prediction_value = int(
            item.get("prediction", 0)
        )

        probability = float(
            item.get("probability", 0.0)
        )

        if probability >= 70:

            risk = "High"
            high_risk += 1

        elif probability >= 40:

            risk = "Medium"
            medium_risk += 1

        else:

            risk = "Low"
            low_risk += 1


        input_data = item.get(
            "input_data"
        )

        diagnosis = "—"
        department = "—"

        if input_data is not None:

            try:

                if isinstance(
                    input_data,
                    pd.DataFrame
                ):

                    if "diagnosis" in input_data.columns:

                        diagnosis = str(
                            input_data.iloc[0][
                                "diagnosis"
                            ]
                        )

                    if "department" in input_data.columns:

                        department = str(
                            input_data.iloc[0][
                                "department"
                            ]
                        )

            except Exception:

                pass


        prediction_text = (
            "Readmitted"
            if prediction_value == 1
            else "Not Readmitted"
        )


        table_rows.append({

            "Prediction ID":
                item.get(
                    "id",
                    f"SC-{index + 1:04d}"
                ),

            "Date":
                item.get(
                    "timestamp",
                    "—"
                ),

            "Diagnosis":
                diagnosis,

            "Department":
                department,

            "Prediction":
                prediction_text,

            "Probability":
                f"{probability:.2f}%",

            "Risk Level":
                risk
        })


    # -----------------------------------------------------
    # SUMMARY
    # -----------------------------------------------------

    st.write("")

    st.html("""
    <div class="table-title">
        📊 History Overview
    </div>
    """)


    summary_col1, summary_col2, summary_col3, summary_col4 = (
        st.columns(4)
    )


    with summary_col1:

        st.html(f"""
        <div class="summary-card">

            <div class="summary-label">
                Total Predictions
            </div>

            <div class="summary-value summary-purple">
                {total_predictions}
            </div>

        </div>
        """)


    with summary_col2:

        st.html(f"""
        <div class="summary-card">

            <div class="summary-label">
                High Risk
            </div>

            <div class="summary-value summary-red">
                {high_risk}
            </div>

        </div>
        """)


    with summary_col3:

        st.html(f"""
        <div class="summary-card">

            <div class="summary-label">
                Medium Risk
            </div>

            <div class="summary-value summary-orange">
                {medium_risk}
            </div>

        </div>
        """)


    with summary_col4:

        st.html(f"""
        <div class="summary-card">

            <div class="summary-label">
                Low Risk
            </div>

            <div class="summary-value summary-green">
                {low_risk}
            </div>

        </div>
        """)


    # -----------------------------------------------------
    # PREDICTION TABLE
    # -----------------------------------------------------

    st.write("")
    st.write("")

    st.html("""
    <div class="history-card">

        <div class="table-title">
            📁 Previous Predictions
        </div>

    </div>
    """)


    history_df = pd.DataFrame(
        table_rows
    )


    st.dataframe(
        history_df,
        use_container_width=True,
        hide_index=True,
        height=300
    )


    # -----------------------------------------------------
    # NEW PREDICTION BUTTON
    # -----------------------------------------------------

    st.write("")

    new_col1, new_col2, new_col3 = st.columns(
        [1, 2, 1]
    )

    with new_col2:

        if st.button(
            "🩺  Make New Prediction  →",
            use_container_width=True
        ):

            st.switch_page(
                "pages/prediction.py"
            )


# =========================================================
# WHY TRACK HISTORY
# =========================================================

st.write("")
st.write("")

st.html("""
<div class="why-card">

    <div class="why-title">
        Why track your prediction history?
    </div>

</div>
""")


feature_col1, feature_col2, feature_col3, feature_col4 = (
    st.columns(4)
)


with feature_col1:

    st.html("""
    <div class="feature-box">

        <div class="feature-icon">
            📈
        </div>

        <div class="feature-title">
            Monitor Progress
        </div>

        <div class="feature-text">
            Track your prediction activity
            and analyze patterns over time.
        </div>

    </div>
    """)


with feature_col2:

    st.html("""
    <div class="feature-box">

        <div class="feature-icon">
            📊
        </div>

        <div class="feature-title">
            Review Results
        </div>

        <div class="feature-text">
            Review previous predictions
            and understand your results.
        </div>

    </div>
    """)


with feature_col3:

    st.html("""
    <div class="feature-box">

        <div class="feature-icon">
            🔍
        </div>

        <div class="feature-title">
            Understand Risk
        </div>

        <div class="feature-text">
            Compare probability values
            and identify different risk levels.
        </div>

    </div>
    """)


with feature_col4:

    st.html("""
    <div class="feature-box">

        <div class="feature-icon">
            🛡️
        </div>

        <div class="feature-title">
            Secure & Private
        </div>

        <div class="feature-text">
            Prediction information remains
            within your SmartCare AI session.
        </div>

    </div>
    """)


# =========================================================
# DISCLAIMER
# =========================================================

st.html("""
<div class="history-disclaimer">

    ⚠️ <strong>SmartCare AI</strong> is an educational
    and research prototype. Predictions are intended
    for decision-support purposes only and should not
    replace professional medical judgment or clinical
    diagnosis.

</div>
""")