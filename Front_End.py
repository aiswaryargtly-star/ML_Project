import streamlit as st
import joblib
import time

# -------------------- Page Config --------------------
st.set_page_config(page_title="Crop_Reccomadation_Login", page_icon="🌱", layout="centered")

# -------------------- Dummy User Credentials --------------------
USER_CREDENTIALS = {
    "admin": "1234",
    "user": "user123"
}

# -------------------- Session State --------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# -------------------- Login Function --------------------
def login():
    # ---------- Background Image + CSS ----------
    st.markdown(
        """
        <style>
        .stApp {background-image: 
            linear-gradient(
                rgba(0, 0, 0, 0.55),
                rgba(0, 0, 0, 0.55)
            ),
            url("https://i.pinimg.com/736x/38/58/a3/3858a3cf90607b70be01107b66440400.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        animation: zoomEffect 18s ease-in-out infinite alternate


           
        }

        .login-card {
            background: rgba(255, 255, 255, 0.9);
            padding: 35px;
            border-radius: 20px;
            width: 400px;
            margin: auto;
            margin-top: 120px;
            box-shadow: 0px 8px 25px rgba(0,0,0,0.3);
        }

        .login-title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: #66bb6a;
        }

        .login-subtitle {
            text-align: center;
            font-size: 25px;
            color: #ffffff;
            margin-bottom: 25px;
        }
         .login_Text {
            font-size: 18px;
            color: #ffffff;
            margin-bottom: 25px;
        }

        .stTextInput input {
            border-radius: 10px;
        }

        .login-btn button {
            background-color: #2e7d32;
            color: white;
            font-size: 18px;
            border-radius: 12px;
            width: 100%;
            padding: 10px;
        }

        .login-btn button:hover {
            background-color: #1b5e20;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # ---------- Login Card ----------
    #st.markdown('<div class="login-card">', unsafe_allow_html=True)
    # ---------- Login Attempts ----------
    if "attempts" not in st.session_state:
        st.session_state.attempts = 0

    st.markdown('<div class="login-title">🔐 Login</div>', unsafe_allow_html=True)
    st.markdown('<div class="login-subtitle">🌾 Crop Recommendation System</div>', unsafe_allow_html=True)

    # username = st.text_input("👤 Username")
    st.markdown('<div class="login_Text">👤 Username</div>', unsafe_allow_html=True)
    username = st.text_input("",placeholder="Enter username",label_visibility="collapsed")
    st.markdown('<div class="login_Text">🔑 Password</div>', unsafe_allow_html=True)
    password = st.text_input(
    "",
    type="password",
    placeholder="Enter password",
    label_visibility="collapsed"
)

    # password = st.text_input("🔑 Password", type="password")

    st.markdown('<div class="login-btn">', unsafe_allow_html=True)
    
    if st.button("Login"):
        if st.session_state.attempts >= 3:
            st.error("🔒 Too many attempts. Try again later.")
            st.stop()

        with st.spinner("Authenticating..."):
            time.sleep(1)
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
           st.session_state.logged_in = True
           st.session_state.attempts = 0
           st.toast("Login Successful 🎉", icon="✅")
           st.rerun()
        else:
            st.session_state.attempts += 1
            st.error(f"❌ Invalid credentials (Attempts left: {3 - st.session_state.attempts})")
    



# -------------------- Main App --------------------
def main_app():
    # ---------- CSS ----------
    st.markdown("""
    <style>
    .stApp {
       background: linear-gradient(135deg, #c8e6c9, #f0f0f0);
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    }  
     

    .header {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #1b5e20;
        margin-bottom: 5px;
    }

    .subheader {
        text-align: center;
        font-size: 18px;
        color: #2e7d32;
        margin-bottom: 30px;
    }

    .card {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0px 6px 20px rgba(0,0,0,0.15);
        margin-bottom: 20px;
    }

    .predict-btn button {
        background-color: #1b5e20;
        color: white;
        font-size: 18px;
        border-radius: 12px;
        padding: 10px;
        width: 100%;
    }

    .predict-btn button:hover {
        background-color: #2e7d32;
    }

    .logout-btn button {
        background-color: #c62828;
        color: white;
        border-radius: 10px;
        width: 100%;
                
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------- Header ----------
    st.markdown('<div class="header">🌾 Crop Recommendation System</div>', unsafe_allow_html=True)
    st.markdown('<div class="subheader">Smart Agriculture using Machine Learning</div>', unsafe_allow_html=True)

    # ---------- Load Model ----------
    model = joblib.load("model.pkl")

    # ---------- Input Card ----------
    # st.markdown('<div class="card">', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        N = st.number_input("🌱 Nitrogen", 0, 200)
        temp = st.number_input("🌡️ Temperature (°C)")

    with col2:
        P = st.number_input("🧪 Phosphorus", 0, 200)
        humidity = st.number_input("💧 Humidity (%)")

    with col3:
        K = st.number_input("🧂 Potassium", 0, 200)
        ph = st.number_input("⚗️ pH Value")

    rainfall = st.number_input("🌧️ Rainfall (mm)")

    st.markdown('</div>', unsafe_allow_html=True)

    # ---------- Predict ----------
    st.markdown('<div class="predict-btn">', unsafe_allow_html=True)
    if st.button("🌿 Predict Best Crop"):
        result = model.predict([[N, P, K, temp, humidity, ph, rainfall]])
        st.success(f"✅ Recommended Crop: **{result[0]}**")
    st.markdown('</div>', unsafe_allow_html=True)

    # ---------- Logout ----------
    st.markdown('<div class="logout-btn">', unsafe_allow_html=True)
    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


# -------------------- Routing --------------------
if st.session_state.logged_in:
    main_app()
else:
    login()

