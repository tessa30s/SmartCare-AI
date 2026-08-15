import streamlit as st


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="SmartCare AI",
    page_icon="🏥",
    layout="wide"
)


# =========================================================
# SMARTCARE HOME PAGE THEME
# =========================================================

st.html("""
<style>

/* =====================================================
   GLOBAL
===================================================== */

.stApp {
    background:
        radial-gradient(
            circle at 85% 8%,
            rgba(91, 33, 182, 0.20),
            transparent 30%
        ),
        radial-gradient(
            circle at 15% 90%,
            rgba(37, 99, 235, 0.10),
            transparent 30%
        ),
        #060B18;
}

.block-container {
    max-width: 1250px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}


/* =====================================================
   HERO
===================================================== */

.hero {
    position: relative;

    min-height: 390px;

    padding: 45px;

    border-radius: 28px;

    overflow: hidden;

    background:
        radial-gradient(
            circle at 80% 50%,
            rgba(124, 58, 237, 0.35),
            transparent 38%
        ),
        linear-gradient(
            135deg,
            #0B1533 0%,
            #111B4A 48%,
            #24145A 100%
        );

    border: 1px solid #2C3F78;

    box-shadow:
        0 25px 70px rgba(0, 0, 0, 0.35);
}


/* Decorative glow */

.hero-glow {
    position: absolute;

    width: 360px;
    height: 360px;

    right: 60px;
    top: 10px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle,
            rgba(168, 85, 247, 0.22),
            transparent 68%
        );

    pointer-events: none;
}


/* =====================================================
   HERO CONTENT
===================================================== */

.hero-content {
    position: relative;

    z-index: 3;

    max-width: 650px;

    padding-top: 12px;
}

.ai-badge {
    display: inline-block;

    padding: 7px 15px;

    border-radius: 30px;

    color: #C4B5FD;

    background: rgba(99, 102, 241, 0.15);

    border: 1px solid rgba(139, 92, 246, 0.40);

    font-size: 13px;

    font-weight: 600;

    margin-bottom: 18px;
}

.hero-title {
    color: #F8FAFC;

    font-size: 58px;

    line-height: 1.05;

    font-weight: 800;

    letter-spacing: -2px;
}

.hero-title span {
    color: #A855F7;
}

.hero-subtitle {
    margin-top: 16px;

    color: #E2E8F0;

    font-size: 21px;

    font-weight: 500;
}

.hero-description {
    margin-top: 16px;

    max-width: 600px;

    color: #A8B5D1;

    font-size: 16px;

    line-height: 1.7;
}


/* =====================================================
   HERO MEDICAL VISUAL
===================================================== */

.medical-visual {
    position: absolute;

    right: 30px;
    top: 35px;

    width: 410px;
    height: 320px;

    z-index: 2;
}


/* Main circle */

.medical-ring {
    position: absolute;

    width: 270px;
    height: 270px;

    right: 65px;
    top: 25px;

    border-radius: 50%;

    border: 1px solid rgba(139, 92, 246, 0.45);

    box-shadow:
        0 0 60px rgba(124, 58, 237, 0.22),
        inset 0 0 45px rgba(124, 58, 237, 0.10);
}


/* Medical card */

.medical-card {
    position: absolute;

    width: 170px;
    height: 215px;

    right: 90px;
    top: 25px;

    padding: 22px;

    border-radius: 22px;

    transform: rotate(7deg);

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.14),
            rgba(255,255,255,0.035)
        );

    border: 1px solid rgba(167,139,250,0.50);

    box-shadow:
        0 25px 55px rgba(0,0,0,0.35);

    backdrop-filter: blur(10px);
}

.medical-cross {
    text-align: center;

    font-size: 48px;

    color: #D8B4FE;

    text-shadow:
        0 0 25px rgba(192,132,252,0.60);
}

.medical-line {
    height: 7px;

    margin-top: 17px;

    border-radius: 20px;

    background:
        linear-gradient(
            90deg,
            #C084FC,
            #6366F1
        );
}

.medical-line.short {
    width: 62%;

    opacity: 0.55;
}


/* Shield */

.medical-shield {
    position: absolute;

    right: 28px;
    bottom: 28px;

    width: 76px;
    height: 76px;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 22px;

    background:
        linear-gradient(
            145deg,
            #7C3AED,
            #4C1D95
        );

    border: 1px solid #A78BFA;

    box-shadow:
        0 0 38px rgba(139,92,246,0.50);

    font-size: 31px;
}


/* Floating icons */

.floating-icon {
    position: absolute;

    width: 58px;
    height: 58px;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 50%;

    background: rgba(79,70,229,0.18);

    border: 1px solid rgba(139,92,246,0.50);

    box-shadow:
        0 0 25px rgba(99,102,241,0.25);

    font-size: 24px;
}

.icon-brain {
    left: 15px;
    top: 55px;
}

.icon-chart {
    left: 35px;
    bottom: 30px;
}

.icon-heart {
    right: 5px;
    top: 105px;
}


/* =====================================================
   SECTION TITLES
===================================================== */

.section-title {
    margin-top: 34px;

    margin-bottom: 20px;

    color: #F8FAFC;

    font-size: 25px;

    font-weight: 700;
}

.section-line {
    width: 42px;

    height: 3px;

    margin-top: 8px;

    border-radius: 10px;

    background:
        linear-gradient(
            90deg,
            #A855F7,
            #6366F1
        );
}


/* =====================================================
   FEATURE CARDS
===================================================== */

.feature-card {
    min-height: 205px;

    padding: 22px;

    border-radius: 18px;

    background:
        linear-gradient(
            145deg,
            rgba(18,30,57,0.98),
            rgba(10,18,36,0.98)
        );

    border: 1px solid #263657;

    box-shadow:
        0 12px 35px rgba(0,0,0,0.18);
}

.feature-icon {
    width: 48px;
    height: 48px;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 13px;

    background:
        linear-gradient(
            145deg,
            #5B21B6,
            #7C3AED
        );

    box-shadow:
        0 0 25px rgba(124,58,237,0.28);

    font-size: 23px;

    margin-bottom: 17px;
}

.feature-title {
    color: #F8FAFC;

    font-size: 18px;

    font-weight: 700;

    margin-bottom: 9px;
}

.feature-description {
    color: #94A3B8;

    font-size: 14px;

    line-height: 1.65;
}

.feature-number {
    margin-top: 12px;

    color: #334155;

    font-size: 27px;

    font-weight: 800;
}


/* =====================================================
   WORKFLOW
===================================================== */

.workflow {
    min-height: 185px;

    padding: 25px;

    border-radius: 20px;

    background:
        linear-gradient(
            145deg,
            rgba(14,24,46,0.98),
            rgba(9,16,31,0.98)
        );

    border: 1px solid #263657;

    box-shadow:
        0 12px 35px rgba(0,0,0,0.15);
}

.workflow-step {
    text-align: center;
}

.workflow-icon {
    width: 62px;
    height: 62px;

    margin: auto;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 50%;

    background:
        linear-gradient(
            145deg,
            #7C3AED,
            #4F46E5
        );

    box-shadow:
        0 0 30px rgba(124,58,237,0.28);

    font-size: 27px;
}

.workflow-title {
    margin-top: 14px;

    color: #F8FAFC;

    font-size: 16px;

    font-weight: 600;
}

.workflow-number {
    color: #8B5CF6;

    font-weight: 800;
}

.workflow-description {
    margin-top: 8px;

    color: #94A3B8;

    font-size: 13px;

    line-height: 1.6;
}


/* =====================================================
   MODEL STATS
===================================================== */

.stat-card {
    padding: 20px;

    text-align: center;

    border-radius: 16px;

    background: #0D162B;

    border: 1px solid #253454;
}

.stat-value {
    color: #A78BFA;

    font-size: 26px;

    font-weight: 800;
}

.stat-label {
    margin-top: 5px;

    color: #64748B;

    font-size: 12px;
}


/* =====================================================
   DISCLAIMER
===================================================== */

.disclaimer {
    margin-top: 25px;

    padding: 20px 25px;

    border-radius: 18px;

    background:
        linear-gradient(
            135deg,
            rgba(49,46,129,0.30),
            rgba(30,27,75,0.45)
        );

    border: 1px solid #373B75;

    color: #CBD5E1;

    font-size: 13px;

    line-height: 1.6;
}


/* =====================================================
   FOOTER
===================================================== */

.home-footer {
    text-align: center;

    color: #475569;

    font-size: 12px;

    margin-top: 35px;

    padding-top: 20px;

    border-top: 1px solid #1E293B;
}


/* =====================================================
   BUTTONS
===================================================== */

.stButton > button {
    border-radius: 12px;

    min-height: 44px;

    border: 1px solid #374151;

    background: #111827;

    color: #F8FAFC;

    font-weight: 600;
}

.stButton > button:hover {
    border-color: #8B5CF6;

    background: #1A1330;

    color: white;
}


/* =====================================================
   MOBILE SAFETY
===================================================== */

@media (max-width: 900px) {

    .hero {
        min-height: auto;

        padding: 30px;
    }

    .hero-title {
        font-size: 42px;
    }

    .medical-visual {
        display: none;
    }

}

</style>
""")


# =========================================================
# HERO SECTION
# =========================================================

st.html("""
<div class="hero">

    <div class="hero-glow"></div>

    <div class="hero-content">

        <div class="ai-badge">
            ✨ AI Powered Healthcare
        </div>

        <div class="hero-title">
            SmartCare <span>AI</span>
        </div>

        <div class="hero-subtitle">
            Intelligent 30-Day Patient Readmission Prediction
        </div>

        <div class="hero-description">
            Helping healthcare professionals make
            data-driven decisions with machine learning
            and explainable artificial intelligence.
        </div>

    </div>


    <div class="medical-visual">

        <div class="medical-ring"></div>

        <div class="medical-card">

            <div class="medical-cross">
                ✚
            </div>

            <div class="medical-line"></div>

            <div class="medical-line short"></div>

            <div class="medical-line"></div>

            <div class="medical-line short"></div>

        </div>


        <div class="medical-shield">
            🛡️
        </div>


        <div class="floating-icon icon-brain">
            🧠
        </div>

        <div class="floating-icon icon-chart">
            📊
        </div>

        <div class="floating-icon icon-heart">
            ❤️
        </div>

    </div>

</div>
""")


# =========================================================
# HERO ACTIONS
# =========================================================

st.write("")

col1, col2, col3 = st.columns([1.4, 1.4, 4])


with col1:

    if st.button(
        "🚀 Get Started",
        use_container_width=True
    ):
        st.switch_page("pages/login.py")


with col2:

    if st.button(
        "▶ Watch Demo",
        use_container_width=True
    ):
        st.info(
            "Demo video will be available here."
        )


# =========================================================
# WHY SMARTCARE AI
# =========================================================

st.html("""
<div class="section-title">

    Why SmartCare AI?

    <div class="section-line"></div>

</div>
""")


features = [
    (
        "🧠",
        "AI Prediction",
        "Machine learning models estimate the likelihood of patient readmission within 30 days.",
        "01"
    ),
    (
        "🗄️",
        "Data Driven",
        "Uses patient, clinical, hospital and treatment information to generate predictions.",
        "02"
    ),
    (
        "🔍",
        "Explainable AI",
        "SHAP-based explanations help users understand the factors influencing predictions.",
        "03"
    ),
    (
        "🏥",
        "Healthcare Focused",
        "Designed as a decision-support prototype for hospital readmission analysis.",
        "04"
    )
]


col1, col2, col3, col4 = st.columns(4)


for column, feature in zip(
    [col1, col2, col3, col4],
    features
):

    icon, title, description, number = feature

    with column:

        st.html(
            f"""
            <div class="feature-card">

                <div class="feature-icon">
                    {icon}
                </div>

                <div class="feature-title">
                    {title}
                </div>

                <div class="feature-description">
                    {description}
                </div>

                <div class="feature-number">
                    {number}
                </div>

            </div>
            """
        )


# =========================================================
# HOW SMARTCARE AI WORKS
# =========================================================

st.html("""
<div class="section-title">

    How SmartCare AI Works

    <div class="section-line"></div>

</div>
""")


workflow = [
    (
        "📋",
        "01",
        "Enter Patient Data",
        "Provide relevant patient, clinical and hospital information."
    ),
    (
        "🧠",
        "02",
        "AI Analysis",
        "The trained machine learning model processes the information."
    ),
    (
        "📈",
        "03",
        "Understand the Result",
        "Receive a readmission prediction with explainable AI insights."
    )
]


col1, col2, col3 = st.columns(3)


for column, item in zip(
    [col1, col2, col3],
    workflow
):

    icon, number, title, description = item

    with column:

        st.html(
            f"""
            <div class="workflow">

                <div class="workflow-step">

                    <div class="workflow-icon">
                        {icon}
                    </div>

                    <div class="workflow-title">

                        <span class="workflow-number">
                            {number}
                        </span>

                        &nbsp;

                        {title}

                    </div>

                    <div class="workflow-description">
                        {description}
                    </div>

                </div>

            </div>
            """
        )


# =========================================================
# MODEL PERFORMANCE
# =========================================================

st.html("""
<div class="section-title">

    SmartCare AI Model

    <div class="section-line"></div>

</div>
""")


st.write(
    "The current SmartCare AI system uses a Random Forest "
    "classification model to predict whether a patient "
    "will be readmitted within 30 days."
)


stats = [
    ("89.5%", "Accuracy"),
    ("100%", "Readmission Recall"),
    ("82.93%", "F1-Score"),
    ("94.14%", "ROC-AUC")
]


col1, col2, col3, col4 = st.columns(4)


for column, stat in zip(
    [col1, col2, col3, col4],
    stats
):

    value, label = stat

    with column:

        st.html(
            f"""
            <div class="stat-card">

                <div class="stat-value">
                    {value}
                </div>

                <div class="stat-label">
                    {label}
                </div>

            </div>
            """
        )


# =========================================================
# DISCLAIMER
# =========================================================

st.html("""
<div class="disclaimer">

    🛡️ <strong>Important:</strong>

    SmartCare AI is an educational and research
    prototype. Predictions should not be used as a
    substitute for professional medical judgment
    or clinical diagnosis.

</div>
""")


# =========================================================
# FOOTER
# =========================================================

st.html("""
<div class="home-footer">

    SmartCare AI • Machine Learning Healthcare Project

    <br><br>

    Built with Python • Scikit-learn • SHAP • Streamlit

    <br><br>

    © 2026 SmartCare AI

</div>
""")