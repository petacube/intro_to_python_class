import streamlit as st
st.title("Course Feedback Form")
with st.form("feedback"):
    name = st.text_input("Name")
    rating = st.slider("Course rating", 1, 5, 5)
    comments = st.text_area("Comments")
    submitted = st.form_submit_button("Submit")
if submitted:
    st.success(f"Thanks {name}, rating recorded: {rating}/5")