import streamlit as st, pandas as pd
st.title("CSV Previewer")
file = st.file_uploader("Upload CSV file", type=["csv"])
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())