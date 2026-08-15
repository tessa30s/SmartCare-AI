import streamlit as st

st.set_page_config(
    page_title="SmartCare AI",
    page_icon="🏥",
    layout="wide"
)

# -----------------------------
# Custom Styling
# -----------------------------

st.markdown("""
<style>

.hero {
    padding: 70px 40px;
    border-radius: 24px;
    background: linear-gradient(
        135deg,
        #5B21B6 0%,
        #7C3AED 50%,
        #A855F7 100%
    );
    color: white;
    text-align: center;
    margin-bottom: 40px;
}

.hero h1 {
    font-size: 55px;
    font-weight: 800;
    margin-bottom: 10px;
}

.hero p {
    font-size: 21px;
    opacity: 0.95;
}

.feature-card {
    padding: 25px;
    border-radius: 18px;
    background: #F8F5FF;
    border: 1px solid #E9D5FF;
    min-height: 190px;
}

.feature-card h3 {
    color: #5B21B6;
}

.feature-card p {
    color: #4B5563;
    line-height: 1.6;
}

.section-title {
    text-align: center;
    margin-top: 35px;
    margin-bottom: 25px;
}

.footer {
    text-align: center;
    padding: 30px;
    color: #6B7280;
    margin-top: 50px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Hero Section
# -----------------------------

st.markdown("""
<div class="hero">

<h1>🏥 SmartCare AI</h1>

<p>
Intelligent 30-Day Patient Readmission Prediction
</p>

<p>
Helping healthcare professionals make data-driven decisions
with machine learning and explainable AI.
</p>

</div>
""", unsafe_allow_html=True)

# -----------------------------
# Get Started
# -----------------------------

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button(
        "🚀 Get Started",
        use_container_width=True
    ):
        st.switch_page("pages/login.py")

# -----------------------------
# Features
# -----------------------------

st.markdown(
    '<h2 class="section-title">Why SmartCare AI?</h2>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>🤖 AI Prediction</h3>
        <p>
        Machine learning models estimate the likelihood
        of patient readmission within 30 days.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>📊 Data Driven</h3>
        <p>
        Uses patient, clinical, hospital and treatment
        information to generate predictions.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3>🔍 Explainable AI</h3>
        <p>
        SHAP-based explanations help users understand
        the factors influencing predictions.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature-card">
        <h3>🏥 Healthcare Focused</h3>
        <p>
        Designed as a decision-support prototype for
        hospital readmission analysis.
        </p>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# How It Works
# -----------------------------

st.markdown(
    '<h2 class="section-title">How SmartCare AI Works</h2>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 01 — Enter Patient Data
    Provide relevant patient, clinical and hospital information.
    """)

with col2:
    st.markdown("""
    ### 02 — AI Analysis
    The trained machine learning model processes the information.
    """)

with col3:
    st.markdown("""
    ### 03 — Understand the Result
    Receive a readmission prediction with explainable AI insights.
    """)

# -----------------------------
# Disclaimer
# -----------------------------

st.warning(
    "⚠️ SmartCare AI is an educational and research prototype. "
    "Predictions should not be used as a substitute for professional "
    "medical judgment or clinical diagnosis."
)

# -----------------------------
# Footer
# -----------------------------

st.markdown("""
<div class="footer">
    <p>SmartCare AI • Machine Learning Healthcare Project</p>
    <p>Built with Python, Scikit-learn, XGBoost, SHAP & Streamlit</p>
</div>
""", unsafe_allow_html=True)