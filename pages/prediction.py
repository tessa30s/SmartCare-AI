import streamlit as st
import pandas as pd
import joblib
from datetime import date


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="New Prediction | SmartCare AI",
    page_icon="🩺",
    layout="wide"
)


# =========================================================
# LOAD MODEL + PREPROCESSOR
# =========================================================

try:

    model = joblib.load(
        "models/smartcare_random_forest.pkl"
    )

    preprocessor = joblib.load(
        "models/preprocessor.joblib"
    )

except Exception as e:

    st.error("Unable to load SmartCare AI model.")

    st.exception(e)

    st.stop()


# =========================================================
# LOGIN PROTECTION
# =========================================================

if not st.session_state.get("logged_in", False):

    st.warning(
        "Please log in to access patient predictions."
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
# CUSTOM THEME
# =========================================================

st.html("""
<style>
/* =====================================================
   VIEW RESULT BUTTON
===================================================== */

.result-button-container {
    display: flex;
    justify-content: center;
    margin-top: 22px;
    margin-bottom: 10px;
}

.result-button {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;

    width: 100%;
    max-width: 560px;
    min-height: 52px;

    padding: 14px 24px;

    border-radius: 13px;

    background: linear-gradient(
        135deg,
        #5B21B6 0%,
        #7C3AED 50%,
        #C026D3 100%
    );

    border: 1px solid rgba(168, 85, 247, 0.8);

    color: white !important;

    font-size: 15px;
    font-weight: 700;

    text-decoration: none !important;

    box-shadow:
        0 8px 25px rgba(124, 58, 237, 0.25);

    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease,
        filter 0.2s ease;
}

/* =====================================================
   DETAILED RESULT BUTTON
===================================================== */

a[data-testid="stPageLink-NavLink"] {

    min-height: 54px !important;

    display: flex !important;

    align-items: center !important;

    justify-content: center !important;

    border-radius: 14px !important;

    margin-top: 20px !important;

    padding: 14px 24px !important;

    background:
        linear-gradient(
            135deg,
            #5B21B6 0%,
            #7C3AED 50%,
            #A855F7 100%
        ) !important;

    border:
        1px solid
        rgba(168, 85, 247, 0.75) !important;

    color: #FFFFFF !important;

    font-size: 15px !important;

    font-weight: 700 !important;

    text-decoration: none !important;

    box-shadow:
        0 8px 25px
        rgba(124, 58, 237, 0.30) !important;

    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease,
        filter 0.2s ease !important;
}


/* Hover */

a[data-testid="stPageLink-NavLink"]:hover {

    transform:
        translateY(-2px) !important;

    filter:
        brightness(1.08) !important;

    box-shadow:
        0 12px 35px
        rgba(168, 85, 247, 0.45) !important;

    color: #FFFFFF !important;
}


/* Icon */

a[data-testid="stPageLink-NavLink"] svg {

    width: 20px !important;

    height: 20px !important;

    margin-right: 8px !important;
}
/* =====================================================
   GLOBAL
===================================================== */

.stApp {

    background:

        radial-gradient(
            circle at 78% 8%,
            rgba(124, 58, 237, 0.18),
            transparent 27%
        ),

        radial-gradient(
            circle at 15% 90%,
            rgba(37, 99, 235, 0.10),
            transparent 30%
        ),

        #060B18;

    color: #F8FAFC;
}


.block-container {

    max-width: 1280px;

    padding-top: 1.4rem;

    padding-bottom: 4rem;
}


/* =====================================================
   HERO
===================================================== */

.prediction-hero {

    position: relative;

    overflow: hidden;

    padding: 25px 30px;

    margin-bottom: 18px;

    border-radius: 22px;

    background:

        radial-gradient(
            circle at 78% 30%,
            rgba(168, 85, 247, 0.18),
            transparent 25%
        ),

        linear-gradient(
            135deg,
            #0D1635,
            #11143A,
            #211046
        );

    border: 1px solid #303B68;
}


.prediction-hero::after {

    content: "";

    position: absolute;

    width: 230px;

    height: 230px;

    right: -60px;

    top: -100px;

    border-radius: 50%;

    background:
        rgba(168, 85, 247, 0.08);

    filter: blur(5px);
}


.hero-layout {

    display: flex;

    align-items: center;

    justify-content: space-between;

    gap: 25px;
}


.hero-left {

    position: relative;

    z-index: 2;
}


.hero-badge {

    display: inline-block;

    padding: 6px 12px;

    border-radius: 50px;

    background:
        rgba(124, 58, 237, 0.15);

    border:
        1px solid
        rgba(167, 139, 250, 0.35);

    color: #C4B5FD;

    font-size: 11px;

    font-weight: 700;

    letter-spacing: 0.7px;
}


.hero-title {

    margin-top: 12px;

    font-size: 34px;

    font-weight: 800;

    color: #F8FAFC;
}


.hero-title span {

    color: #A855F7;
}


.hero-description {

    margin-top: 7px;

    max-width: 680px;

    color: #94A3B8;

    font-size: 13px;

    line-height: 1.6;
}


.hero-icon {

    position: relative;

    z-index: 2;

    width: 115px;

    height: 115px;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 28px;

    background:

        linear-gradient(
            145deg,
            rgba(124, 58, 237, 0.35),
            rgba(37, 99, 235, 0.18)
        );

    border:
        1px solid
        rgba(139, 92, 246, 0.4);

    font-size: 58px;

    box-shadow:
        0 0 45px
        rgba(124, 58, 237, 0.22);
}


/* =====================================================
   FORM SECTIONS
===================================================== */

.form-section {

    position: relative;

    margin-bottom: 14px;

    padding: 21px 24px;

    border-radius: 18px;

    background:

        linear-gradient(
            145deg,
            rgba(15, 25, 52, 0.96),
            rgba(8, 17, 35, 0.96)
        );

    border: 1px solid #27385D;

    transition: border 0.2s ease;
}


.form-section:hover {

    border-color:
        rgba(124, 58, 237, 0.48);
}


.section-header {

    display: flex;

    align-items: center;

    gap: 13px;

    margin-bottom: 15px;
}


.section-icon {

    width: 40px;

    height: 40px;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 12px;

    background:

        linear-gradient(
            145deg,
            #5B21B6,
            #7C3AED
        );

    box-shadow:
        0 7px 20px
        rgba(124, 58, 237, 0.20);

    font-size: 19px;
}


.section-title {

    color: #F8FAFC;

    font-size: 18px;

    font-weight: 750;
}


.section-subtitle {

    color: #64748B;

    font-size: 11px;

    margin-top: 2px;
}


/* =====================================================
   INPUTS
===================================================== */

div[data-baseweb="input"] {

    background:
        #111A32 !important;

    border-radius: 10px !important;

    border:
        1px solid
        #2B3A5D !important;
}


div[data-baseweb="select"] > div {

    background:
        #111A32 !important;

    border-radius: 10px !important;

    border:
        1px solid
        #2B3A5D !important;
}


div[data-baseweb="input"]:focus-within {

    border-color:
        #7C3AED !important;

    box-shadow:
        0 0 0 1px
        rgba(124, 58, 237, 0.2);
}


div[data-baseweb="select"] > div:focus-within {

    border-color:
        #7C3AED !important;
}


label {

    color:
        #CBD5E1 !important;

    font-size:
        12px !important;

    font-weight:
        600 !important;
}


div[data-testid="stDateInput"] input {

    background:
        #111A32 !important;

    color:
        #F8FAFC !important;
}


div[data-testid="stNumberInput"] button {

    background:
        #111A32 !important;

    color:
        #C4B5FD !important;

    border-color:
        #2B3A5D !important;
}


div[data-baseweb="select"] span {

    color:
        #E2E8F0 !important;
}


/* =====================================================
   PREDICTION CTA
===================================================== */

.prediction-cta {

    padding: 24px;

    margin-top: 20px;

    border-radius: 20px;

    text-align: center;

    background:

        radial-gradient(
            circle at 50% 0%,
            rgba(168, 85, 247, 0.16),
            transparent 50%
        ),

        linear-gradient(
            135deg,
            #111A38,
            #17113C
        );

    border:
        1px solid
        #3B3972;
}


.cta-title {

    color: #F8FAFC;

    font-size: 20px;

    font-weight: 750;
}


.cta-text {

    color: #8493AD;

    font-size: 12px;

    margin-top: 5px;

    margin-bottom: 17px;
}


/* =====================================================
   BUTTONS
===================================================== */

.stButton > button {

    min-height: 44px;

    border-radius: 11px !important;

    background:
        #111A32 !important;

    border:
        1px solid
        #35466D !important;

    color:
        #E2E8F0 !important;

    font-weight:
        600 !important;

    transition:
        all 0.2s ease;
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
   SUCCESS
===================================================== */

.success-panel {

    margin-top: 20px;

    padding: 20px;

    border-radius: 16px;

    background:
        rgba(16, 185, 129, 0.08);

    border:
        1px solid
        rgba(52, 211, 153, 0.25);

    color: #A7F3D0;
}


.success-title {

    color: #6EE7B7;

    font-weight: 700;

    margin-bottom: 5px;
}


/* =====================================================
   DISCLAIMER
===================================================== */

.disclaimer {

    margin-top: 20px;

    padding: 14px 17px;

    border-radius: 12px;

    background:
        rgba(15, 23, 42, 0.75);

    border:
        1px solid
        #273653;

    color: #71809A;

    font-size: 11px;

    line-height: 1.6;
}

</style>
""")


# =========================================================
# PAGE HEADER
# =========================================================

st.html("""
<div class="prediction-hero">

    <div class="hero-layout">

        <div class="hero-left">

            <div class="hero-badge">
                ✦ AI-POWERED HEALTHCARE
            </div>

            <div class="hero-title">
                New Patient <span>Prediction</span>
            </div>

            <div class="hero-description">
                Enter the patient's information below to
                estimate the likelihood of readmission
                within 30 days using the SmartCare AI model.
            </div>

        </div>

        <div class="hero-icon">
            🩺
        </div>

    </div>

</div>
""")


# =========================================================
# PATIENT INFORMATION
# =========================================================

st.html("""
<div class="form-section">

    <div class="section-header">

        <div class="section-icon">
            👤
        </div>

        <div>

            <div class="section-title">
                Patient Information
            </div>

            <div class="section-subtitle">
                Basic patient demographic information
            </div>

        </div>

    </div>

</div>
""")


col1, col2, col3 = st.columns(3)


with col1:

    age = st.number_input(
        "Age",
        min_value=0,
        max_value=120,
        value=50,
        step=1
    )


with col2:

    gender = st.selectbox(
        "Gender",
        [
            "Male",
            "Female"
        ]
    )


with col3:

    blood_group = st.selectbox(
        "Blood Group",
        [
            "A-",
            "B-",
            "B+",
            "AB-",
            "O+",
            "A+",
            "AB+",
            "O-"
        ]
    )


# =========================================================
# APPOINTMENT INFORMATION
# =========================================================

st.html("""
<div class="form-section">

    <div class="section-header">

        <div class="section-icon">
            📅
        </div>

        <div>

            <div class="section-title">
                Appointment Information
            </div>

            <div class="section-subtitle">
                Appointment history and attendance details
            </div>

        </div>

    </div>

</div>
""")


col1, col2, col3 = st.columns(3)


with col1:

    appointment_date = st.date_input(
        "Appointment Date",
        value=date.today()
    )


with col2:

    waiting_days = st.number_input(
        "Waiting Days",
        min_value=0,
        value=0,
        step=1
    )


with col3:

    appointment_status = st.selectbox(
        "Appointment Status",
        [
            "Completed",
            "Cancelled",
            "No-Show",
            "Scheduled"
        ]
    )


col1, col2 = st.columns(2)


with col1:

    previous_appointments = st.number_input(
        "Previous Appointments",
        min_value=0,
        value=0,
        step=1
    )


with col2:

    missed_previous_appointments = st.number_input(
        "Missed Previous Appointments",
        min_value=0,
        value=0,
        step=1
    )


# =========================================================
# MEDICAL INFORMATION
# =========================================================

st.html("""
<div class="form-section">

    <div class="section-header">

        <div class="section-icon">
            ❤️
        </div>

        <div>

            <div class="section-title">
                Medical Information
            </div>

            <div class="section-subtitle">
                Clinical diagnosis and hospital information
            </div>

        </div>

    </div>

</div>
""")


col1, col2, col3 = st.columns(3)


with col1:

    department = st.selectbox(
        "Department",
        [
            "General Medicine",
            "Orthopedics",
            "Cardiology",
            "Laboratory Services",
            "Neurology",
            "Pediatrics",
            "Radiology"
        ]
    )


with col2:

    diagnosis = st.selectbox(
        "Diagnosis",
        [
            "Asthma",
            "Back Pain",
            "Chest Pain",
            "Diabetes",
            "Fever",
            "Fracture",
            "Hypertension",
            "Kidney Infection",
            "Migraine",
            "Pneumonia"
        ]
    )


with col3:

    admitted = st.selectbox(
        "Hospital Admission",
        [0, 1],
        format_func=lambda x:
            "Yes" if x == 1 else "No"
    )


col1, col2, col3 = st.columns(3)


with col1:

    room_type = st.selectbox(
        "Room Type",
        [
            "Unknown",
            "General Ward",
            "Private Room",
            "ICU"
        ]
    )


with col2:

    length_of_stay_days = st.number_input(
        "Length of Stay (Days)",
        min_value=0,
        value=1,
        step=1
    )


with col3:

    previous_admissions = st.number_input(
        "Previous Admissions",
        min_value=0,
        value=0,
        step=1
    )


# =========================================================
# CLINICAL MEASUREMENTS
# =========================================================

st.html("""
<div class="form-section">

    <div class="section-header">

        <div class="section-icon">
            🧪
        </div>

        <div>

            <div class="section-title">
                Clinical Measurements
            </div>

            <div class="section-subtitle">
                Patient vital signs and laboratory measurements
            </div>

        </div>

    </div>

</div>
""")


col1, col2, col3, col4, col5 = st.columns(5)


with col1:

    systolic_bp = st.number_input(
        "Systolic BP",
        min_value=0,
        value=120,
        step=1
    )


with col2:

    diastolic_bp = st.number_input(
        "Diastolic BP",
        min_value=0,
        value=80,
        step=1
    )


with col3:

    blood_sugar = st.number_input(
        "Blood Sugar",
        min_value=0,
        value=100,
        step=1
    )


with col4:

    cholesterol = st.number_input(
        "Cholesterol",
        min_value=0,
        value=200,
        step=1
    )


with col5:

    bmi = st.number_input(
        "BMI",
        min_value=0.0,
        value=25.0,
        step=0.1
    )


# =========================================================
# TREATMENT INFORMATION
# =========================================================

st.html("""
<div class="form-section">

    <div class="section-header">

        <div class="section-icon">
            💊
        </div>

        <div>

            <div class="section-title">
                Treatment Information
            </div>

            <div class="section-subtitle">
                Tests and treatment activity
            </div>

        </div>

    </div>

</div>
""")


col1, col2 = st.columns(2)


with col1:

    lab_tests_count = st.number_input(
        "Number of Lab Tests",
        min_value=0,
        value=0,
        step=1
    )


with col2:

    treatments_count = st.number_input(
        "Number of Treatments",
        min_value=0,
        value=1,
        step=1
    )


# =========================================================
# FINANCIAL INFORMATION
# =========================================================

st.html("""
<div class="form-section">

    <div class="section-header">

        <div class="section-icon">
            💰
        </div>

        <div>

            <div class="section-title">
                Financial Information
            </div>

            <div class="section-subtitle">
                Healthcare and treatment costs
            </div>

        </div>

    </div>

</div>
""")


col1, col2, col3 = st.columns(3)


with col1:

    consultation_fee = st.number_input(
        "Consultation Fee (LKR)",
        min_value=0,
        value=1000,
        step=100
    )


with col2:

    room_charge = st.number_input(
        "Room Charge (LKR)",
        min_value=0,
        value=0,
        step=100
    )


with col3:

    lab_charge = st.number_input(
        "Lab Charge (LKR)",
        min_value=0,
        value=0,
        step=100
    )


col1, col2 = st.columns(2)


with col1:

    medicine_charge = st.number_input(
        "Medicine Charge (LKR)",
        min_value=0,
        value=0,
        step=100
    )


with col2:

    total_bill = st.number_input(
        "Total Bill (LKR)",
        min_value=0,
        value=0,
        step=100
    )


# =========================================================
# PAYMENT INFORMATION
# =========================================================

st.html("""
<div class="form-section">

    <div class="section-header">

        <div class="section-icon">
            💳
        </div>

        <div>

            <div class="section-title">
                Payment Information
            </div>

            <div class="section-subtitle">
                Payment status and payment method
            </div>

        </div>

    </div>

</div>
""")


col1, col2 = st.columns(2)


with col1:

    payment_status = st.selectbox(
        "Payment Status",
        [
            "Paid",
            "Unpaid",
            "Partially Paid"
        ]
    )


with col2:

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Cash",
            "Card",
            "Online",
            "Insurance"
        ]
    )


# =========================================================
# PREPARE INPUT DATA
# =========================================================

input_data = pd.DataFrame([{

    "age": age,

    "gender": gender,

    "blood_group": blood_group,

    "department": department,

    "diagnosis": diagnosis,

    "appointment_status": appointment_status,

    "waiting_days": waiting_days,

    "previous_appointments": previous_appointments,

    "missed_previous_appointments":
        missed_previous_appointments,

    "admitted": admitted,

    "room_type":
        None
        if room_type == "Unknown"
        else room_type,

    "length_of_stay_days":
        length_of_stay_days,

    "previous_admissions":
        previous_admissions,

    "systolic_bp":
        systolic_bp,

    "diastolic_bp":
        diastolic_bp,

    "blood_sugar_mg_dl":
        blood_sugar,

    "cholesterol_mg_dl":
        cholesterol,

    "bmi":
        bmi,

    "lab_tests_count":
        lab_tests_count,

    "treatments_count":
        treatments_count,

    "consultation_fee_lkr":
        consultation_fee,

    "room_charge_lkr":
        room_charge,

    "lab_charge_lkr":
        lab_charge,

    "medicine_charge_lkr":
        medicine_charge,

    "total_bill_lkr":
        total_bill,

    "payment_status":
        payment_status,

    "payment_method":
        payment_method,

    "appointment_year":
        appointment_date.year,

    "appointment_month":
        appointment_date.month,

    "appointment_day":
        appointment_date.day,

    "appointment_dayofweek":
        appointment_date.weekday()

}])


# =========================================================
# PREDICTION CTA
# =========================================================

st.html("""
<div class="prediction-cta">

    <div class="cta-title">
        🔮 Ready to Analyze the Patient?
    </div>

    <div class="cta-text">
        SmartCare AI will process the entered information
        and prepare the patient for readmission risk analysis.
    </div>

</div>
""")


col1, col2, col3 = st.columns([1, 2, 1])


with col2:

    predict_button = st.button(
        "🔮 Generate Prediction",
        use_container_width=True
    )


# =========================================================
# GENERATE PREDICTION
# =========================================================

if predict_button:

    try:

        # -------------------------------------------------
        # TRANSFORM INPUT
        # -------------------------------------------------

        transformed_data = preprocessor.transform(
            input_data
        )

        # -------------------------------------------------
        # PREDICTION
        # -------------------------------------------------

        prediction_value = model.predict(
            transformed_data
        )[0]

        # -------------------------------------------------
        # PROBABILITY
        # -------------------------------------------------

        if hasattr(model, "predict_proba"):

            probability = model.predict_proba(
                transformed_data
            )[0][1]

            probability_percent = (
                float(probability) * 100
            )

        else:

            probability_percent = 0.0

        # -------------------------------------------------
        # SAVE PREDICTION
        # -------------------------------------------------

        st.session_state["prediction"] = int(
            prediction_value
        )

        st.session_state["probability"] = (
            probability_percent
        )

        st.session_state["input_data"] = (
            input_data.copy()
        )

        # Also keep latest values
        st.session_state["latest_prediction"] = int(
            prediction_value
        )

        st.session_state["latest_probability"] = (
            probability_percent
        )

        st.session_state["latest_input_data"] = (
            input_data.copy()
        )

        # -------------------------------------------------
        # SUCCESS MESSAGE
        # -------------------------------------------------

        if prediction_value == 1:

            st.html("""
            <div class="success-panel">

                <div class="success-title">
                    ⚠️ Prediction Generated
                </div>

                The model detected a higher likelihood
                of 30-day readmission.

            </div>
            """)

        else:

            st.html("""
            <div class="success-panel">

                <div class="success-title">
                    ✓ Prediction Generated Successfully
                </div>

                The model detected a lower likelihood
                of 30-day readmission.

            </div>
            """)

        # -------------------------------------------------
        # SHOW PROBABILITY
        # -------------------------------------------------

        st.write("")

        st.metric(
            "Estimated Readmission Probability",
            f"{probability_percent:.2f}%"
        )

    except Exception as e:

        st.error(
            "Unable to generate the prediction."
        )

        st.exception(e)


# =========================================================
# SHOW STORED PREDICTION RESULT
# =========================================================

# =========================================================
# SHOW STORED PREDICTION RESULT
# =========================================================

if "prediction" in st.session_state:

    probability_percent = st.session_state.get(
        "probability",
        0.0
    )

    st.write("")

    result_col1, result_col2, result_col3 = st.columns(
        [1, 2, 1]
    )

    with result_col2:

        st.page_link(
            "pages/results.py",
            label="📊  View Detailed Prediction Result  →",
            use_container_width=True
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