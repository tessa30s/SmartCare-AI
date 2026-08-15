import streamlit as st
import pandas as pd
import joblib
from datetime import date


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="New Prediction | SmartCare AI",
    page_icon="🩺",
    layout="wide"
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
        "Unable to load the AI model or preprocessing pipeline."
    )

    st.exception(e)

    st.stop()


# ==================================================
# LOGIN PROTECTION
# ==================================================

if not st.session_state.get("logged_in", False):

    st.warning(
        "Please log in to access patient predictions."
    )

    if st.button("🔐 Go to Login"):

        st.switch_page(
            "pages/login.py"
        )

    st.stop()


# ==================================================
# HEADER
# ==================================================

st.title("🩺 New Patient Prediction")

st.write(
    "Enter the patient's information below to estimate "
    "the likelihood of readmission within 30 days."
)

st.divider()


# ==================================================
# PATIENT INFORMATION
# ==================================================

st.header("👤 Patient Information")

col1, col2, col3 = st.columns(3)


with col1:

    age = st.number_input(
        "Age",
        min_value=0,
        max_value=120,
        value=50
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


# ==================================================
# APPOINTMENT INFORMATION
# ==================================================

st.header("📅 Appointment Information")

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
        value=0
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
        value=0
    )


with col2:

    missed_previous_appointments = st.number_input(
        "Missed Previous Appointments",
        min_value=0,
        value=0
    )


# ==================================================
# MEDICAL INFORMATION
# ==================================================

st.header("🩺 Medical Information")

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


col1, col2 = st.columns(2)


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
        value=1
    )


previous_admissions = st.number_input(
    "Previous Admissions",
    min_value=0,
    value=0
)


# ==================================================
# CLINICAL MEASUREMENTS
# ==================================================

st.header("🧪 Clinical Measurements")

col1, col2, col3, col4 = st.columns(4)


with col1:

    systolic_bp = st.number_input(
        "Systolic BP",
        min_value=0,
        value=120
    )


with col2:

    diastolic_bp = st.number_input(
        "Diastolic BP",
        min_value=0,
        value=80
    )


with col3:

    blood_sugar = st.number_input(
        "Blood Sugar (mg/dL)",
        min_value=0,
        value=100
    )


with col4:

    cholesterol = st.number_input(
        "Cholesterol (mg/dL)",
        min_value=0,
        value=200
    )


bmi = st.number_input(
    "BMI",
    min_value=0.0,
    value=25.0,
    step=0.1
)


# ==================================================
# TREATMENT INFORMATION
# ==================================================

st.header("💊 Treatment Information")

col1, col2 = st.columns(2)


with col1:

    lab_tests_count = st.number_input(
        "Number of Lab Tests",
        min_value=0,
        value=0
    )


with col2:

    treatments_count = st.number_input(
        "Number of Treatments",
        min_value=0,
        value=1
    )


# ==================================================
# FINANCIAL INFORMATION
# ==================================================

st.header("💰 Financial Information")

col1, col2 = st.columns(2)


with col1:

    consultation_fee = st.number_input(
        "Consultation Fee (LKR)",
        min_value=0,
        value=1000
    )


with col2:

    room_charge = st.number_input(
        "Room Charge (LKR)",
        min_value=0,
        value=0
    )


col1, col2 = st.columns(2)


with col1:

    lab_charge = st.number_input(
        "Lab Charge (LKR)",
        min_value=0,
        value=0
    )


with col2:

    medicine_charge = st.number_input(
        "Medicine Charge (LKR)",
        min_value=0,
        value=0
    )


total_bill = st.number_input(
    "Total Bill (LKR)",
    min_value=0,
    value=0
)


# ==================================================
# PAYMENT INFORMATION
# ==================================================

st.header("💳 Payment Information")

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


# ==================================================
# PREDICTION BUTTON
# ==================================================

st.divider()

predict_button = st.button(
    "🔮 Predict Readmission Risk",
    use_container_width=True
)


# ==================================================
# PREDICTION PROCESS
# ==================================================

if predict_button:

    try:

        # ------------------------------------------
        # CREATE INPUT DATAFRAME
        # ------------------------------------------

        input_data = pd.DataFrame([{

            "age": age,

            "gender": gender,

            "blood_group": blood_group,

            "department": department,

            "diagnosis": diagnosis,

            "waiting_days": waiting_days,

            "previous_appointments":
                previous_appointments,

            "missed_previous_appointments":
                missed_previous_appointments,

            "appointment_status":
                appointment_status,

            "admitted":
                admitted,

            "room_type":
                None if room_type == "Unknown"
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


        # ------------------------------------------
        # PREPROCESS INPUT
        # ------------------------------------------

        processed_input = preprocessor.transform(
            input_data
        )


        # ------------------------------------------
        # MAKE PREDICTION
        # ------------------------------------------

        prediction = model.predict(
            processed_input
        )[0]


        # ------------------------------------------
        # GET PROBABILITY
        # ------------------------------------------

        probability = model.predict_proba(
            processed_input
        )[0][1]

        probability_percentage = (
            probability * 100
        )


        # ------------------------------------------
        # SAVE CURRENT RESULT
        # ------------------------------------------

        st.session_state["prediction"] = int(
            prediction
        )

        st.session_state["probability"] = (
            probability_percentage
        )

        st.session_state["input_data"] = (
            input_data
        )


        # ==========================================
        # SAVE TO PREDICTION HISTORY
        # ==========================================

        if "prediction_history" not in st.session_state:

            st.session_state["prediction_history"] = []


        # ------------------------------------------
        # CREATE PREDICTION ID
        # ------------------------------------------

        prediction_number = (
            len(
                st.session_state[
                    "prediction_history"
                ]
            ) + 1
        )


        prediction_id = (
            f"SC-{prediction_number:04d}"
        )


        # ------------------------------------------
        # DETERMINE RISK LEVEL
        # ------------------------------------------

        if probability_percentage >= 70:

            risk_level = "High"

        elif probability_percentage >= 40:

            risk_level = "Medium"

        else:

            risk_level = "Low"


        # ------------------------------------------
        # CREATE HISTORY RECORD
        # ------------------------------------------

        prediction_record = {

            "Prediction ID":
                prediction_id,

            "Date":
                pd.Timestamp.now().strftime(
                    "%Y-%m-%d %H:%M"
                ),

            "Diagnosis":
                diagnosis,

            "Department":
                department,

            "Prediction":
                (
                    "Readmitted"
                    if prediction == 1
                    else "Not Readmitted"
                ),

            "Probability":
                round(
                    probability_percentage,
                    2
                ),

            "Risk Level":
                risk_level
        }


        # ------------------------------------------
        # ADD RECORD TO HISTORY
        # ------------------------------------------

        st.session_state[
            "prediction_history"
        ].append(
            prediction_record
        )


        # ------------------------------------------
        # SUCCESS MESSAGE
        # ------------------------------------------

        st.success(
            "Prediction completed successfully!"
        )


        # ------------------------------------------
        # GO TO RESULTS PAGE
        # ------------------------------------------

        st.switch_page(
            "pages/results.py"
        )


    except Exception as e:

        st.error(
            "An error occurred while generating "
            "the prediction."
        )

        st.exception(e)


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