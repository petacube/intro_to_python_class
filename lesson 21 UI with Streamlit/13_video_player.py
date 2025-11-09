import streamlit as st
st.title("Video Player")
video_file = st.file_uploader("Upload video", type=["mp4", "mov"])
if video_file:
    st.video(video_file)