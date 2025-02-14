import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

# Title
st.title("AI Diagnostic Platform")

# Sidebar Navigation
menu = ["Home", "Pregnancy Risk Assessment", "Skin Cancer Detection"]
choice = st.sidebar.selectbox("Select Diagnosis Type", menu)

if choice == "Home":
    st.write("Welcome to the AI Diagnostic Platform! Please select a diagnosis type from the sidebar.")

elif choice == "Pregnancy Risk Assessment":
    st.subheader("Pregnancy Risk Assessment")
    age = st.number_input("Enter Age", min_value=15, max_value=50, value=25)
    blood_pressure = st.number_input("Blood Pressure (mmHg)", min_value=80, max_value=200, value=120)
    glucose_level = st.number_input("Glucose Level (mg/dL)", min_value=50, max_value=250, value=100)

    if st.button("Assess Risk"):
        risk_score = (blood_pressure / 2) + (glucose_level / 3) + (age / 5)  # Dummy calculation
        if risk_score > 80:
            st.error("High Risk: Please consult a doctor.")
        else:
            st.success("Low Risk: No immediate concerns.")

elif choice == "Skin Cancer Detection":
    st.subheader("Skin Cancer Detection")
    uploaded_file = st.file_uploader("Upload a skin lesion image", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        if st.button("Analyze Image"):
            st.warning("This is a placeholder for AI-based skin cancer detection.")  # Replace with AI model logic
