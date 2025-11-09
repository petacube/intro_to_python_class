import streamlit as st
st.title("Search App")
query = st.text_input("Search term")
with st.expander("Advanced options"):
    case_sensitive = st.checkbox("Case sensitive")
    exact_match = st.checkbox("Exact match")
st.write("You searched for:", query)
st.write("Case sensitive:", case_sensitive, "| Exact:", exact_match)