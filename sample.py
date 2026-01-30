

import streamlit as st
import numpy as np

# Page settings
st.set_page_config(
    page_title="Smart Crop Recommendation",
    page_icon="🌾",
    layout="wide"
)

# Header
st.markdown(
    "<h1 style='text-align: center; color: green;'>🌱 Smart Crop Recommendation System</h1>",
    unsafe_allow_html=True
)

st.markdown("---")

# Input Section
st.subheader("🔍 Enter Soil & Climate Details To Get The best Crop Recommendation")

col1, col2, col3 = st.columns(3)

with col1:
    N = st.number_input("Nitrogen (N)", 0, 200)
    temperature = st.number_input("Temperature (°C)", 0.0, 50.0)

with col2:
    P = st.number_input("Phosphorus (P)", 0, 200)
    humidity = st.number_input("Humidity (%)", 0.0, 100.0)

with col3:
    K = st.number_input("Potassium (K)", 0, 200)
    ph = st.number_input("Soil pH", 0.0, 14.0)

rainfall = st.number_input("Rainfall (mm)", 0.0)

st.markdown("---")

# Predict Button
if st.button("🌾 Predict Best Crop", use_container_width=True):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

    # Replace with ML model prediction
    st.markdown(
        """
        <div style="background-color:#e8f5e9; padding:20px; border-radius:10px;">
            <h3 style="color:green;">✅ Recommended Crop</h3>
            <h2>🌾 Wheat</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
