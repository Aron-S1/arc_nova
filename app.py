import streamlit as st
import numpy as np
import joblib
import tensorflow as tf
from datetime import datetime

st.set_page_config(page_title="ArcNova Fusion AI", layout="wide")

st.title("⚛️ ArcNova Fusion Control Panel")
st.caption("AI-powered hybrid LSTM/XGBoost fusion ignition predictor")

# Sliders
col1, col2 = st.columns(2)
with col1:
    temp = st.slider("Plasma Temp (M K)", 50, 300, 150)
    pressure = st.slider("Pressure (atm)", 1, 6, 3)
    field = st.slider("Magnetic Field (T)", 1, 10, 5)
with col2:
    density = st.slider("Fuel Density (g/cm³)", 0.1, 2.0, 1.0, 0.1)
    duration = st.slider("Confinement Time (s)", 1, 30, 10)

# Input scaling
def scale_input(temp, pressure, field, density, duration):
    return np.array([[
        (temp - 150) / 50,
        (pressure - 3) / 1,
        (field - 5) / 2,
        (density - 1) / 0.5,
        (duration - 10) / 5
    ]])

# Model selection
model_type = st.selectbox("Choose AI Model", ["LSTM", "XGBoost"])

if st.button("🚀 Predict Ignition"):
    st.write("⏳ Loading model...")
    
    try:
        if model_type == "LSTM":
            model = tf.keras.models.load_model("arcnova_lstm_model.h5")
        else:
            model = joblib.load("arcnova_xgb_model.joblib")

        features = scale_input(temp, pressure, field, density, duration)
        prediction = model.predict(features)

        if model_type == "LSTM":
            ignition = prediction[0][0] > 0.5
        else:
            ignition = prediction[0] > 0.5

        st.subheader("🔍 Result:")
        if ignition:
            st.success("🔥 Fusion Ignition Achieved!")
        else:
            st.error("❄️ No Ignition – Adjust Parameters")

    except Exception as e:
        st.error(f"❌ Error loading model: {e}")

        
