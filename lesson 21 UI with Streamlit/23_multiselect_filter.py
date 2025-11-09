import streamlit as st, pandas as pd
st.title("Multiselect Filter")
df = pd.DataFrame({"lang": ["Python", "Python", "Java", "C++", "Rust"], "score": [95, 88, 70, 60, 85]})
langs = st.multiselect("Select languages", options=sorted(df["lang"].unique()), default=["Python"])
st.dataframe(df[df["lang"].isin(langs)])