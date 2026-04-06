import streamlit as st
import requests

st.title("🤖 AI Architecture Compliance Assistant")

uploaded_file = st.file_uploader("Upload Architecture Document")

if uploaded_file:
    if st.button("Analyze"):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://localhost:8000/analyze/", files=files)

        if response.status_code == 200:
            st.subheader("📊 Compliance Report")
            st.write(response.json()["report"])
        else:
            st.error(f"Backend Error: {response.status_code}")
            st.write(response.text)