import streamlit as st
from datetime import datetime


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Dashboard | SmartCare AI",
    page_icon="📊",
    layout="wide"
)


# =========================================================
# LOGIN PROTECTION
# =========================================================

if not st.session_state.get("logged_in", False):

    st.warning("Please log in to access the SmartCare AI dashboard.")

    if st.button(
        "🔐 Go to Login",
        use_container_width=True
    ):
        st.switch_page("pages/login.py")

    st.stop()


# =========================================================
# USER
# =========================================================

username = st.session_state.get("username", "User")

current_hour = datetime.now().hour

if current_hour < 12:
    greeting = "Good morning"
elif current_hour < 18:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"


# =========================================================
# OPTIONAL SESSION-BASED PREDICTION DATA
# =========================================================
#
# This safely checks for prediction history.
# If your history page later stores predictions in
# st.session_state["prediction_history"], this dashboard
# will automatically start using them.
#
# Until then, all counts remain 0 instead of showing
# fake patient statistics.
# =========================================================

prediction_history = st.session_state.get(
    "prediction_history",
    []
)

if not isinstance(prediction_history, list):
    prediction_history = []


total_predictions = len(prediction_history)

high_risk = 0
medium_risk = 0
low_risk = 0


for record in prediction_history:

    if not isinstance(record, dict):
        continue

    risk = str(
        record.get(
            "risk_level",
            record.get("risk", "")
        )
    ).lower()

    if "high" in risk:
        high_risk += 1

    elif "medium" in risk or "moderate" in risk:
        medium_risk += 1

    elif "low" in risk:
        low_risk += 1


# =========================================================
# CSS
# =========================================================

st.html("""
<style>


/* =====================================================
   GLOBAL
===================================================== */

.stApp {

    background:

        radial-gradient(
            circle at 90% 0%,
            rgba(124, 58, 237, 0.18),
            transparent 28%
        ),

        radial-gradient(
            circle at 10% 90%,
            rgba(37, 99, 235, 0.09),
            transparent 30%
        ),

        #060B18;

    color: #F8FAFC;
}


.block-container {

    max-width: 1280px;

    padding-top: 1.5rem;

    padding-bottom: 4rem;
}


/* =====================================================
   HERO
===================================================== */

.dashboard-hero {

    position: relative;

    overflow: hidden;

    padding: 34px 36px;

    border-radius: 24px;

    background:

        radial-gradient(
            circle at 82% 45%,
            rgba(168, 85, 247, 0.20),
            transparent 28%
        ),

        linear-gradient(
            135deg,
            #0D1734 0%,
            #11183D 48%,
            #24114A 100%
        );

    border: 1px solid #303C69;

    box-shadow:
        0 24px 70px
        rgba(0, 0, 0, 0.30);

    margin-bottom: 18px;
}


.hero-glow {

    position: absolute;

    width: 300px;

    height: 300px;

    right: -80px;

    top: -120px;

    border-radius: 50%;

    background:
        rgba(168, 85, 247, 0.13);

    filter: blur(5px);
}


.hero-top {

    display: flex;

    justify-content: space-between;

    align-items: center;

    gap: 20px;
}


.hero-badge {

    display: inline-flex;

    align-items: center;

    gap: 8px;

    padding: 7px 13px;

    border-radius: 50px;

    background:
        rgba(124, 58, 237, 0.15);

    border:
        1px solid
        rgba(167, 139, 250, 0.35);

    color: #C4B5FD;

    font-size: 11px;

    font-weight: 700;

    letter-spacing: 0.8px;
}


.system-online {

    display: inline-flex;

    align-items: center;

    gap: 8px;

    padding: 7px 13px;

    border-radius: 50px;

    background:
        rgba(16, 185, 129, 0.08);

    border:
        1px solid
        rgba(52, 211, 153, 0.25);

    color: #6EE7B7;

    font-size: 11px;

    font-weight: 700;

    letter-spacing: 0.5px;
}


.online-dot {

    width: 8px;

    height: 8px;

    border-radius: 50%;

    background: #4ADE80;

    box-shadow:
        0 0 13px
        rgba(74, 222, 128, 0.90);
}


.hero-title {

    margin-top: 24px;

    color: #F8FAFC;

    font-size: 38px;

    line-height: 1.1;

    font-weight: 800;

    letter-spacing: -1px;
}


.hero-title span {

    background:
        linear-gradient(
            90deg,
            #A78BFA,
            #E879F9
        );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;
}


.hero-description {

    max-width: 680px;

    margin-top: 12px;

    color: #9AA8C3;

    font-size: 14px;

    line-height: 1.7;
}


/* =====================================================
   SECTION
===================================================== */

.section-heading {

    margin-top: 30px;

    margin-bottom: 18px;

    display: flex;

    align-items: center;

    justify-content: space-between;
}


.section-title {

    color: #F8FAFC;

    font-size: 20px;

    font-weight: 750;
}


.section-subtitle {

    color: #64748B;

    font-size: 12px;

    margin-top: 4px;
}


/* =====================================================
   OVERVIEW CARDS
===================================================== */

.overview-card {

    position: relative;

    overflow: hidden;

    min-height: 150px;

    padding: 20px;

    border-radius: 18px;

    background:
        linear-gradient(
            145deg,
            rgba(17, 27, 52, 0.98),
            rgba(9, 17, 34, 0.98)
        );

    border: 1px solid #253557;

    transition:
        transform 0.25s ease,
        border 0.25s ease;
}


.overview-card:hover {

    transform: translateY(-4px);

    border-color: #6D4BC3;
}


.overview-icon {

    width: 42px;

    height: 42px;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 12px;

    background:
        rgba(124, 58, 237, 0.13);

    border:
        1px solid
        rgba(139, 92, 246, 0.25);

    font-size: 20px;

    margin-bottom: 14px;
}


.overview-value {

    color: #F8FAFC;

    font-size: 29px;

    font-weight: 800;
}


.overview-label {

    color: #94A3B8;

    font-size: 12px;

    margin-top: 3px;
}


.card-accent {

    position: absolute;

    right: -25px;

    top: -25px;

    width: 90px;

    height: 90px;

    border-radius: 50%;

    background:
        rgba(124, 58, 237, 0.08);
}


/* =====================================================
   RISK CARD VARIANTS
===================================================== */

.high-card {

    border-color:
        rgba(244, 63, 94, 0.25);
}


.high-card .overview-icon {

    background:
        rgba(244, 63, 94, 0.10);

    border-color:
        rgba(244, 63, 94, 0.20);
}


.medium-card {

    border-color:
        rgba(245, 158, 11, 0.22);
}


.medium-card .overview-icon {

    background:
        rgba(245, 158, 11, 0.10);

    border-color:
        rgba(245, 158, 11, 0.20);
}


.low-card {

    border-color:
        rgba(16, 185, 129, 0.22);
}


.low-card .overview-icon {

    background:
        rgba(16, 185, 129, 0.10);

    border-color:
        rgba(16, 185, 129, 0.20);
}


/* =====================================================
   QUICK ACTION CARDS
===================================================== */

.action-card {

    min-height: 170px;

    padding: 23px;

    border-radius: 18px;

    background:

        radial-gradient(
            circle at 90% 0%,
            rgba(124, 58, 237, 0.11),
            transparent 35%
        ),

        linear-gradient(
            145deg,
            #111A32,
            #0B1427
        );

    border: 1px solid #29395D;
}


.action-icon {

    font-size: 28px;

    margin-bottom: 12px;
}


.action-title {

    color: #F8FAFC;

    font-size: 18px;

    font-weight: 700;
}


.action-description {

    margin-top: 8px;

    color: #8493AE;

    font-size: 12px;

    line-height: 1.6;
}


/* =====================================================
   AI MODEL CARD
===================================================== */

.model-card {

    padding: 25px;

    border-radius: 20px;

    background:
        linear-gradient(
            145deg,
            #101A32,
            #0B1327
        );

    border: 1px solid #29395D;
}


.model-header {

    display: flex;

    align-items: center;

    gap: 15px;

    margin-bottom: 20px;
}


.model-icon {

    width: 52px;

    height: 52px;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 15px;

    background:
        linear-gradient(
            145deg,
            #5B21B6,
            #7C3AED
        );

    font-size: 25px;

    box-shadow:
        0 0 25px
        rgba(124, 58, 237, 0.25);
}


.model-name {

    color: #F8FAFC;

    font-size: 18px;

    font-weight: 700;
}


.model-type {

    color: #71809D;

    font-size: 11px;

    margin-top: 3px;
}


/* =====================================================
   PERFORMANCE
===================================================== */

.performance-row {

    margin-top: 14px;
}


.performance-top {

    display: flex;

    justify-content: space-between;

    margin-bottom: 7px;
}


.performance-label {

    color: #94A3B8;

    font-size: 12px;
}


.performance-value {

    color: #C4B5FD;

    font-size: 12px;

    font-weight: 700;
}


.performance-track {

    width: 100%;

    height: 7px;

    overflow: hidden;

    border-radius: 10px;

    background: #18243C;
}


.performance-fill {

    height: 100%;

    border-radius: 10px;

    background:
        linear-gradient(
            90deg,
            #6D28D9,
            #A855F7,
            #D946EF
        );
}


/* =====================================================
   MODEL HEALTH
===================================================== */

.health-card {

    padding: 25px;

    border-radius: 20px;

    background:
        linear-gradient(
            145deg,
            #101A32,
            #0B1327
        );

    border: 1px solid #29395D;

    min-height: 100%;
}


.health-title {

    color: #F8FAFC;

    font-size: 18px;

    font-weight: 700;

    margin-bottom: 20px;
}


.health-row {

    display: flex;

    align-items: center;

    justify-content: space-between;

    padding: 13px 0;

    border-bottom:
        1px solid
        rgba(51, 65, 85, 0.45);
}


.health-row:last-child {

    border-bottom: none;
}


.health-name {

    display: flex;

    align-items: center;

    gap: 10px;

    color: #A8B5CA;

    font-size: 12px;
}


.health-dot {

    width: 8px;

    height: 8px;

    border-radius: 50%;

    background: #4ADE80;

    box-shadow:
        0 0 10px
        rgba(74, 222, 128, 0.65);
}


.health-status {

    color: #6EE7B7;

    font-size: 11px;

    font-weight: 700;
}


/* =====================================================
   EMPTY ACTIVITY
===================================================== */

.activity-card {

    padding: 35px;

    text-align: center;

    border-radius: 20px;

    background:
        linear-gradient(
            145deg,
            rgba(16, 26, 50, 0.96),
            rgba(8, 16, 32, 0.96)
        );

    border: 1px solid #273757;
}


.activity-icon {

    width: 60px;

    height: 60px;

    margin: auto;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 18px;

    background:
        rgba(124, 58, 237, 0.10);

    border:
        1px solid
        rgba(139, 92, 246, 0.22);

    font-size: 27px;
}


.activity-title {

    color: #E2E8F0;

    font-size: 16px;

    font-weight: 700;

    margin-top: 15px;
}


.activity-text {

    color: #64748B;

    font-size: 12px;

    margin-top: 6px;
}


/* =====================================================
   DISCLAIMER
===================================================== */

.disclaimer {

    margin-top: 28px;

    padding: 16px 19px;

    border-radius: 14px;

    background:
        rgba(15, 23, 42, 0.70);

    border: 1px solid #273653;

    color: #71809A;

    font-size: 11px;

    line-height: 1.6;
}


/* =====================================================
   BUTTONS
===================================================== */

.stButton > button {

    min-height: 45px;

    border-radius: 11px !important;

    border:
        1px solid
        #35456C !important;

    background:
        #111A31 !important;

    color:
        #E2E8F0 !important;

    font-weight: 600 !important;

    transition: all 0.2s ease;
}


.stButton > button:hover {

    border-color:
        #8B5CF6 !important;

    background:
        #1A1330 !important;

    color:
        white !important;

    transform:
        translateY(-1px);
}


/* =====================================================
   MOBILE
===================================================== */

@media (max-width: 900px) {

    .hero-top {

        display: block;
    }

    .system-online {

        margin-top: 12px;
    }

    .hero-title {

        font-size: 30px;
    }

}

</style>
""")


# =========================================================
# HERO
# =========================================================

st.html(
    f"""
    <div class="dashboard-hero">

        <div class="hero-glow"></div>

        <div class="hero-top">

            <div class="hero-badge">
                ✦ SMARTCARE AI • COMMAND CENTER
            </div>

            <div class="system-online">

                <div class="online-dot"></div>

                SYSTEM OPERATIONAL

            </div>

        </div>


        <div class="hero-title">

            {greeting},
            <span>{username}</span> 👋

        </div>


        <div class="hero-description">

            Welcome to your intelligent healthcare command center.
            Monitor patient readmission risk, review AI performance
            and generate explainable predictions from one place.

        </div>

    </div>
    """
)


# =========================================================
# HERO BUTTONS
# =========================================================

button1, button2, button3 = st.columns(
    [1.3, 1.3, 3.4]
)


with button1:

    if st.button(
        "🔮 Run New Assessment",
        use_container_width=True,
        key="hero_prediction"
    ):

        st.switch_page(
            "pages/prediction.py"
        )


with button2:

    if st.button(
        "📋 View History",
        use_container_width=True,
        key="hero_history"
    ):

        st.switch_page(
            "pages/history.py"
        )


# =========================================================
# TODAY AT A GLANCE
# =========================================================

st.html("""
<div class="section-heading">

    <div>

        <div class="section-title">
            Today at a Glance
        </div>

        <div class="section-subtitle">
            Your SmartCare AI prediction overview
        </div>

    </div>

</div>
""")


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.html(
        f"""
        <div class="overview-card">

            <div class="card-accent"></div>

            <div class="overview-icon">
                ✦
            </div>

            <div class="overview-value">
                {total_predictions}
            </div>

            <div class="overview-label">
                Total Predictions
            </div>

        </div>
        """
    )


with col2:

    st.html(
        f"""
        <div class="overview-card high-card">

            <div class="card-accent"></div>

            <div class="overview-icon">
                ⚠️
            </div>

            <div class="overview-value">
                {high_risk}
            </div>

            <div class="overview-label">
                High Risk
            </div>

        </div>
        """
    )


with col3:

    st.html(
        f"""
        <div class="overview-card medium-card">

            <div class="card-accent"></div>

            <div class="overview-icon">
                ◐
            </div>

            <div class="overview-value">
                {medium_risk}
            </div>

            <div class="overview-label">
                Medium Risk
            </div>

        </div>
        """
    )


with col4:

    st.html(
        f"""
        <div class="overview-card low-card">

            <div class="card-accent"></div>

            <div class="overview-icon">
                ✓
            </div>

            <div class="overview-value">
                {low_risk}
            </div>

            <div class="overview-label">
                Low Risk
            </div>

        </div>
        """
    )


# =========================================================
# QUICK ACTIONS
# =========================================================

st.html("""
<div class="section-heading">

    <div>

        <div class="section-title">
            Quick Actions
        </div>

        <div class="section-subtitle">
            Continue your SmartCare workflow
        </div>

    </div>

</div>
""")


action1, action2, action3 = st.columns(3)


with action1:

    st.html("""
    <div class="action-card">

        <div class="action-icon">
            🩺
        </div>

        <div class="action-title">
            Patient Assessment
        </div>

        <div class="action-description">
            Enter clinical, appointment and hospital
            information to estimate 30-day
            readmission risk.
        </div>

    </div>
    """)

    st.write("")

    if st.button(
        "Start Assessment →",
        use_container_width=True,
        key="action_prediction"
    ):

        st.switch_page(
            "pages/prediction.py"
        )


with action2:

    st.html("""
    <div class="action-card">

        <div class="action-icon">
            📋
        </div>

        <div class="action-title">
            Prediction History
        </div>

        <div class="action-description">
            Review previous SmartCare predictions
            and revisit patient risk assessment
            results.
        </div>

    </div>
    """)

    st.write("")

    if st.button(
        "Open History →",
        use_container_width=True,
        key="action_history"
    ):

        st.switch_page(
            "pages/history.py"
        )


with action3:

    st.html("""
    <div class="action-card">

        <div class="action-icon">
            🔍
        </div>

        <div class="action-title">
            Explainable AI
        </div>

        <div class="action-description">
            Understand how clinical factors
            contribute to predictions through
            SHAP-based explanations.
        </div>

    </div>
    """)

    st.write("")

    if st.button(
        "View Latest Result →",
        use_container_width=True,
        key="action_result"
    ):

        st.switch_page(
            "pages/results.py"
        )


# =========================================================
# MODEL PERFORMANCE
# =========================================================

st.html("""
<div class="section-heading">

    <div>

        <div class="section-title">
            AI Intelligence
        </div>

        <div class="section-subtitle">
            Model performance and system health
        </div>

    </div>

</div>
""")


model_col, health_col = st.columns(
    [1.7, 1]
)


with model_col:

    st.html("""
    <div class="model-card">

        <div class="model-header">

            <div class="model-icon">
                🧠
            </div>

            <div>

                <div class="model-name">
                    Random Forest Classifier
                </div>

                <div class="model-type">
                    30-DAY READMISSION PREDICTION MODEL
                </div>

            </div>

        </div>


        <div class="performance-row">

            <div class="performance-top">

                <div class="performance-label">
                    Accuracy
                </div>

                <div class="performance-value">
                    89.5%
                </div>

            </div>

            <div class="performance-track">

                <div
                    class="performance-fill"
                    style="width:89.5%;">
                </div>

            </div>

        </div>


        <div class="performance-row">

            <div class="performance-top">

                <div class="performance-label">
                    Readmission Recall
                </div>

                <div class="performance-value">
                    100%
                </div>

            </div>

            <div class="performance-track">

                <div
                    class="performance-fill"
                    style="width:100%;">
                </div>

            </div>

        </div>


        <div class="performance-row">

            <div class="performance-top">

                <div class="performance-label">
                    F1 Score
                </div>

                <div class="performance-value">
                    82.93%
                </div>

            </div>

            <div class="performance-track">

                <div
                    class="performance-fill"
                    style="width:82.93%;">
                </div>

            </div>

        </div>


        <div class="performance-row">

            <div class="performance-top">

                <div class="performance-label">
                    ROC-AUC
                </div>

                <div class="performance-value">
                    94.14%
                </div>

            </div>

            <div class="performance-track">

                <div
                    class="performance-fill"
                    style="width:94.14%;">
                </div>

            </div>

        </div>

    </div>
    """)


with health_col:

    st.html("""
    <div class="health-card">

        <div class="health-title">
            ⚡ Model Health
        </div>


        <div class="health-row">

            <div class="health-name">

                <div class="health-dot"></div>

                AI Model

            </div>

            <div class="health-status">
                READY
            </div>

        </div>


        <div class="health-row">

            <div class="health-name">

                <div class="health-dot"></div>

                Preprocessor

            </div>

            <div class="health-status">
                READY
            </div>

        </div>


        <div class="health-row">

            <div class="health-name">

                <div class="health-dot"></div>

                SHAP Engine

            </div>

            <div class="health-status">
                AVAILABLE
            </div>

        </div>


        <div class="health-row">

            <div class="health-name">

                <div class="health-dot"></div>

                Application

            </div>

            <div class="health-status">
                ONLINE
            </div>

        </div>

    </div>
    """)


# =========================================================
# RECENT ACTIVITY
# =========================================================

st.html("""
<div class="section-heading">

    <div>

        <div class="section-title">
            Recent Activity
        </div>

        <div class="section-subtitle">
            Latest SmartCare AI assessments
        </div>

    </div>

</div>
""")


if total_predictions == 0:

    st.html("""
    <div class="activity-card">

        <div class="activity-icon">
            🩺
        </div>

        <div class="activity-title">
            No assessments yet
        </div>

        <div class="activity-text">
            Your recent patient predictions will appear here
            after you run your first assessment.
        </div>

    </div>
    """)

else:

    # Display the last five session records safely.

    recent_records = prediction_history[-5:]
    recent_records.reverse()

    for index, record in enumerate(recent_records):

        if not isinstance(record, dict):
            continue

        diagnosis = record.get(
            "diagnosis",
            "Patient Assessment"
        )

        risk = record.get(
            "risk_level",
            record.get(
                "risk",
                "Prediction Complete"
            )
        )

        probability = record.get(
            "probability",
            record.get(
                "readmission_probability",
                None
            )
        )

        probability_text = ""

        if probability is not None:

            try:

                probability_value = float(probability)

                if probability_value <= 1:
                    probability_value *= 100

                probability_text = (
                    f"{probability_value:.1f}% probability"
                )

            except (ValueError, TypeError):

                probability_text = str(probability)


        st.html(
            f"""
            <div style="
                padding:16px 20px;
                margin-bottom:10px;
                border-radius:14px;
                background:#0F192F;
                border:1px solid #283857;
                display:flex;
                justify-content:space-between;
                align-items:center;
            ">

                <div>

                    <div style="
                        color:#F8FAFC;
                        font-size:13px;
                        font-weight:700;
                    ">
                        🩺 {diagnosis}
                    </div>

                    <div style="
                        color:#64748B;
                        font-size:11px;
                        margin-top:4px;
                    ">
                        {probability_text}
                    </div>

                </div>

                <div style="
                    color:#C4B5FD;
                    font-size:11px;
                    font-weight:700;
                ">
                    {risk}
                </div>

            </div>
            """
        )


# =========================================================
# SECOND CTA
# =========================================================

st.write("")

cta1, cta2, cta3 = st.columns(
    [1, 1.5, 1]
)


with cta2:

    if st.button(
        "✦  Create New Patient Prediction",
        use_container_width=True,
        key="bottom_prediction"
    ):

        st.switch_page(
            "pages/prediction.py"
        )


# =========================================================
# LOGOUT
# =========================================================

st.write("")

logout1, logout2, logout3 = st.columns(
    [2, 1, 2]
)


with logout2:

    if st.button(
        "🚪 Logout",
        use_container_width=True
    ):

        st.session_state["logged_in"] = False

        st.session_state["username"] = None

        st.switch_page(
            "pages/home.py"
        )


# =========================================================
# DISCLAIMER
# =========================================================

st.html("""
<div class="disclaimer">

    🛡️ <strong>Clinical Decision Support Notice:</strong>

    SmartCare AI is an educational and research prototype.
    Model predictions and explainability information should
    support — not replace — professional medical judgment
    or clinical diagnosis.

</div>
""")