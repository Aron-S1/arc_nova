import streamlit as st
from datetime import datetime

st.title("ArcNova Test App")
st.write("If you're seeing this, the repo layout works!")
if st.button("Ping"):
    st.success(f"App is live — {datetime.now()}")
