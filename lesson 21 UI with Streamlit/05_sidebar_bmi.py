import streamlit as st
st.title("BMI Calculator")
weight = st.sidebar.number_input("Weight (kg)", 40.0, 200.0, 70.0)
height = st.sidebar.number_input("Height (m)", 1.3, 2.2, 1.75)
bmi = weight / (height ** 2)
st.metric("BMI", f"{bmi:.1f}")