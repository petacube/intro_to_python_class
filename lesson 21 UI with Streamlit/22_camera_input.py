import streamlit as st
st.title("Camera Capture")
picture = st.camera_input("Take a picture")
if picture:
    st.image(picture)