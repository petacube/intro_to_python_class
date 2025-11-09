import streamlit as st
st.title("Audio Player")
audio_file = st.file_uploader("Upload audio", type=["mp3", "wav", "ogg"])
if audio_file:
    st.audio(audio_file)