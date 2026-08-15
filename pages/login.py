import streamlit as st


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Login | SmartCare AI",
    page_icon="🔐",
    layout="wide"
)


# ==================================================
# CUSTOM CSS
# ==================================================

st.html("""
<style>

/* ==================================================
   GLOBAL
================================================== */

.stApp {
    background:
        radial-gradient(
            circle at 80% 10%,
            rgba(124, 58, 237, 0.18),
            transparent 30%
        ),
        radial-gradient(
            circle at 20% 90%,
            rgba(37, 99, 235, 0.10),
            transparent 30%
        ),
        #060B18;

    color: #F8FAFC;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* ==================================================
   LEFT PANEL
================================================== */

.left-panel {
    padding: 30px;
    border-radius: 24px;

    background:
        linear-gradient(
            145deg,
            #10183A,
            #12143B,
            #1B1243
        );

    border: 1px solid #293866;
    min-height: 650px;
}


/* ==================================================
   BRAND
================================================== */

.brand-title {
    font-size: 30px;
    font-weight: 800;
    color: #F8FAFC;
    margin-top: 10px;
}

.brand-title span {
    color: #A855F7;
}

.brand-subtitle {
    color: #64748B;
    font-size: 11px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
}


/* ==================================================
   MEDICAL VISUAL
================================================== */

.visual-box {
    text-align: center;
    padding: 35px 10px;
    margin-top: 10px;
    margin-bottom: 20px;
    border-radius: 25px;

    background:
        radial-gradient(
            circle,
            rgba(124, 58, 237, 0.28),
            transparent 65%
        );
}

.medical-icon {
    font-size: 120px;
    filter:
        drop-shadow(
            0 0 25px
            rgba(168, 85, 247, 0.65)
        );
}


/* ==================================================
   LEFT CONTENT
================================================== */

.left-heading {
    font-size: 31px;
    line-height: 1.15;
    font-weight: 800;
    color: #F8FAFC;
    margin-top: 10px;
}

.left-heading span {
    color: #D946EF;
}

.left-description {
    color: #A8B5D1;
    font-size: 14px;
    line-height: 1.7;
    margin-top: 12px;
}


/* ==================================================
   FEATURE BOXES
================================================== */

.feature-box {
    padding: 15px;
    min-height: 95px;
    border-radius: 14px;

    background: rgba(18, 29, 59, 0.85);
    border: 1px solid #293A61;
}

.feature-icon {
    font-size: 23px;
}

.feature-title {
    color: #F8FAFC;
    font-size: 13px;
    font-weight: 700;
    margin-top: 5px;
}

.feature-text {
    color: #94A3B8;
    font-size: 11px;
    margin-top: 3px;
}


/* ==================================================
   QUOTE
================================================== */

.quote-box {
    margin-top: 20px;
    padding: 18px;
    border-radius: 15px;

    background: rgba(25, 26, 66, 0.8);
    border: 1px solid #303A70;

    color: #CBD5E1;
    font-size: 13px;
    line-height: 1.6;
}

.stars {
    color: #FBBF24;
    margin-top: 8px;
}


/* ==================================================
   LOGIN PANEL
================================================== */

.login-card {
    padding: 35px 45px 25px 45px;
    border-radius: 24px;

    background:
        linear-gradient(
            145deg,
            rgba(19, 29, 55, 0.98),
            rgba(10, 18, 38, 0.98)
        );

    border: 1px solid #34446C;

    min-height: 650px;

    box-shadow:
        0 25px 70px
        rgba(0, 0, 0, 0.30);
}


/* ==================================================
   LOGIN TITLE
================================================== */

.login-title {
    text-align: center;
    color: #F8FAFC;
    font-size: 34px;
    font-weight: 800;
    margin-top: 20px;
}

.login-subtitle {
    text-align: center;
    color: #94A3B8;
    font-size: 14px;
    margin-bottom: 25px;
}


/* ==================================================
   INPUTS
================================================== */

label {
    color: #E2E8F0 !important;
    font-weight: 600 !important;
}

input {
    background-color: #18223D !important;
    color: #F8FAFC !important;
    border: 1px solid #34446C !important;
    border-radius: 11px !important;
}

input:focus {
    border-color: #8B5CF6 !important;

    box-shadow:
        0 0 0 1px #8B5CF6 !important;
}


/* ==================================================
   LOGIN BUTTON
================================================== */

div[data-testid="stFormSubmitButton"] button {

    background:
        linear-gradient(
            90deg,
            #5B21B6,
            #7C3AED,
            #C026D3
        ) !important;

    color: white !important;
    border: none !important;
    border-radius: 12px !important;

    min-height: 52px !important;

    font-size: 16px !important;
    font-weight: 700 !important;

    margin-top: 10px;
}

div[data-testid="stFormSubmitButton"] button:hover {

    background:
        linear-gradient(
            90deg,
            #6D28D9,
            #8B5CF6,
            #D946EF
        ) !important;
}


/* ==================================================
   NORMAL BUTTONS
================================================== */

.stButton button {

    border-radius: 11px !important;
    background: #111A31 !important;
    border: 1px solid #34446C !important;
    color: #E2E8F0 !important;
}

.stButton button:hover {

    border-color: #8B5CF6 !important;
    color: white !important;
    background: #1A1330 !important;
}


/* ==================================================
   FORM
================================================== */

div[data-testid="stForm"] {
    background: transparent !important;
    border: none !important;
}


/* ==================================================
   FOOTER
================================================== */

.login-footer {
    text-align: center;
    color: #64748B;
    font-size: 12px;
    margin-top: 20px;
}

.login-footer span {
    color: #A78BFA;
}


/* ==================================================
   DISCLAIMER
================================================== */

.disclaimer {
    text-align: center;
    margin-top: 25px;
    color: #475569;
    font-size: 11px;
    line-height: 1.7;
}


/* ==================================================
   MOBILE
================================================== */

@media (max-width: 900px) {

    .left-panel {
        min-height: auto;
    }

    .login-card {
        padding: 25px;
    }

}

</style>
""")


# ==================================================
# PAGE COLUMNS
# ==================================================

left, right = st.columns(
    [1, 1],
    gap="large"
)


# ==================================================
# LEFT SIDE
# ==================================================

with left:

    st.html("""
    <div class="left-panel">

        <div style="
            text-align:center;
            font-size:42px;
        ">
            🏥
        </div>

        <div class="brand-title">
            SmartCare <span>AI</span>
        </div>

        <div class="brand-subtitle">
            Healthcare Intelligence
        </div>

        <div class="visual-box">

            <div class="medical-icon">
                🩺
            </div>

        </div>

        <div class="left-heading">
            AI-Powered Healthcare
            <br>
            <span>Decisions</span>
        </div>

        <div class="left-description">
            SmartCare AI helps healthcare professionals
            predict 30-day patient readmissions using
            machine learning and explainable AI.
        </div>

    </div>
    """)


    # --------------------------------------------------
    # FEATURES
    # --------------------------------------------------

    f1, f2, f3 = st.columns(3)

    with f1:

        st.html("""
        <div class="feature-box">

            <div class="feature-icon">
                🛡️
            </div>

            <div class="feature-title">
                Accurate
            </div>

            <div class="feature-text">
                Predictions
            </div>

        </div>
        """)

    with f2:

        st.html("""
        <div class="feature-box">

            <div class="feature-icon">
                🔍
            </div>

            <div class="feature-title">
                Explainable
            </div>

            <div class="feature-text">
                AI Insights
            </div>

        </div>
        """)

    with f3:

        st.html("""
        <div class="feature-box">

            <div class="feature-icon">
                🔐
            </div>

            <div class="feature-title">
                Secure &
            </div>

            <div class="feature-text">
                Private
            </div>

        </div>
        """)


    # --------------------------------------------------
    # QUOTE
    # --------------------------------------------------

    st.html("""
    <div class="quote-box">

        💜

        <br><br>

        Empowering clinicians with intelligent
        insights for better patient outcomes.

        <div class="stars">
            ★★★★★
        </div>

    </div>
    """)


# ==================================================
# RIGHT SIDE
# ==================================================

with right:

    st.html("""
    <div class="login-card">

        <div style="
            text-align:center;
            font-size:48px;
        ">
            🏥
        </div>

        <div class="login-title">
            Welcome Back
        </div>

        <div class="login-subtitle">
            Sign in to access your SmartCare AI dashboard
        </div>

    </div>
    """)


    # ==================================================
    # LOGIN FORM
    # ==================================================

    with st.form("login_form"):

        username = st.text_input(
            "Username",
            placeholder="Enter your username"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter your password"
        )

        remember = st.checkbox(
            "Remember me"
        )

        login_button = st.form_submit_button(
            "🔐  Sign In",
            use_container_width=True
        )


    # ==================================================
    # LOGIN LOGIC
    # ==================================================

    if login_button:

        if username == "admin" and password == "smartcare123":

            st.session_state["logged_in"] = True
            st.session_state["username"] = username

            st.success(
                "Login successful!"
            )

            st.switch_page(
                "pages/dashboard.py"
            )

        else:

            st.error(
                "Invalid username or password."
            )


    # ==================================================
    # DIVIDER
    # ==================================================

    st.html("""
    <div style="
        height:1px;
        background:#293653;
        margin:20px 0;
    "></div>

    <div style="
        text-align:center;
        color:#64748B;
        font-size:12px;
    ">
        or continue with
    </div>
    """)


    st.write("")


    # ==================================================
    # GOOGLE BUTTON
    # ==================================================

    if st.button(
        "🌐  Sign in with Google",
        use_container_width=True
    ):

        st.info(
            "Google authentication is not configured "
            "in this prototype."
        )


    # ==================================================
    # ACCOUNT MESSAGE
    # ==================================================

    st.html("""
    <div class="login-footer">

        Don't have an account?
        <span>Contact Administrator</span>

    </div>
    """)


    # ==================================================
    # DEMO CREDENTIALS
    # ==================================================

    with st.expander(
        "🔑 Demo Login Credentials"
    ):

        st.write(
            "Username: `admin`"
        )

        st.write(
            "Password: `smartcare123`"
        )


    # ==================================================
    # BACK HOME
    # ==================================================

    if st.button(
        "← Back to Home",
        use_container_width=True
    ):

        st.switch_page(
            "pages/home.py"
        )


# ==================================================
# DISCLAIMER
# ==================================================

st.html("""
<div class="disclaimer">

    SmartCare AI is an educational and research prototype.
    <br>
    Predictions should not replace professional medical judgment.

</div>
""")