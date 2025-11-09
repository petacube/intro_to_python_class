import streamlit as st
st.title("Two-Column Layout")
left, right = st.columns(2)
with left:
    st.header("Left")
    st.write("Use this for inputs.")
with right:
    st.header("Right")
    st.write("Use this for outputs.")