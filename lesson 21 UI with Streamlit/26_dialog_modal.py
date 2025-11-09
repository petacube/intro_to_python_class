import streamlit as st
st.title("Modal Dialog Demo")
@st.dialog("Subscribe")
def subscribe_dialog():
    email = st.text_input("Email")
    if st.button("Submit"):
        st.write("Subscribed (not really).")
if st.button("Open Subscribe Dialog"):
    subscribe_dialog()