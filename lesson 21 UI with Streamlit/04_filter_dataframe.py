import streamlit as st, pandas as pd
st.title("Fruit Sales Explorer")
df = pd.DataFrame({
    "fruit": ["apple", "banana", "orange", "apple", "banana"],
    "quantity": [10, 5, 7, 3, 9]
})
fruit = st.selectbox("Choose fruit", sorted(df["fruit"].unique()))
st.dataframe(df[df["fruit"] == fruit])