import streamlit as st
from datetime import datetime

st.set_page_config(page_title="ArcNova - Test Mode", layout="wide")

st.title("🧪 ArcNova System Test")
st.write("✅ Streamlit app has booted successfully!")

# Fake controls
temperature = st.slider("Test Plasma Temp (M K)", 50, 300, 150)
field_strength = st.slider("Test Magnetic Field", 1, 10, 5)

if st.button("🔍 Simulate"):
    st.success(f"Test complete at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    st.balloons()
