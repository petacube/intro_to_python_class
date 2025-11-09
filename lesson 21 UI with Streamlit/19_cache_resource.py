import streamlit as st
st.title("Cached Resource Demo")
@st.cache_resource
def get_connection():
    return "fake-db-connection"
st.write("Connection object:", get_connection())