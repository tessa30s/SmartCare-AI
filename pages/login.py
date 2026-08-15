import streamlit as st

st.set_page_config(
    page_title="Login | SmartCare AI",
    page_icon="🔐",
    layout="centered"
)

# -----------------------------
# Custom Styling
# -----------------------------

st.markdown("""
<style>

.login-container {
    text-align: center;
    padding: 20px 0 30px 0;
}

.login-container h1 {
    color: #5B21B6;
    font-size: 42px;
    margin-bottom: 5px;
}

.login-container p {
    color: #6B7280;
    font-size: 17px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------

st.markdown("""
<div class="login-container">

<h1>🏥 SmartCare AI</h1>

<p>Sign in to access your healthcare AI dashboard</p>

</div>
""", unsafe_allow_html=True)

# -----------------------------
# Login Form
# -----------------------------

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

    login_button = st.form_submit_button(
        "🔐 Sign In",
        use_container_width=True
    )

# -----------------------------
# Login Logic
# -----------------------------

if login_button:

    if username == "admin" and password == "smartcare123":

        st.session_state["logged_in"] = True
        st.session_state["username"] = username

        st.success("Login successful!")

        st.switch_page("pages/dashboard.py")

    else:

        st.error(
            "Invalid username or password."
        )

# -----------------------------
# Demo Credentials
# -----------------------------

st.info(
    "Demo Login\n\n"
    "Username: admin\n\n"
    "Password: smartcare123"
)

# -----------------------------
# Back to Home
# -----------------------------

if st.button("← Back to Home"):
    st.switch_page("pages/home.py")