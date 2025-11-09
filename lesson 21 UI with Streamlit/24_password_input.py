import streamlit as st
st.title("Login Form (Demo Only)")
username = st.text_input("Username")
password = st.text_input("Password", type="password")
if st.button("Login"):
    st.write("Don't do real auth like this in production 😄")
    st.write(f"Hello, {username or 'mystery user'}")