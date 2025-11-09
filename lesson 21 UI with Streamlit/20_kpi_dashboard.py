import streamlit as st
st.title("Mini KPI Dashboard")
col1, col2, col3 = st.columns(3)
col1.metric("Users", "1200", "+50")
col2.metric("Conversion Rate", "4.2%", "+0.4%")
col3.metric("Errors", "3", "-2")