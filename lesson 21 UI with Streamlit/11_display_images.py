import streamlit as st
from PIL import Image
st.title("Image Display")
uploaded = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if uploaded:
    img = Image.open(uploaded)
    st.image(img, caption="Uploaded image", use_container_width=True)