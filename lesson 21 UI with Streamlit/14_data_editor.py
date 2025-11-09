import streamlit as st, pandas as pd
st.title("Data Table vs Data Editor")
df = pd.DataFrame({"x": [1, 2, 3], "y": [10, 20, 30]})
st.subheader("Static table")
st.dataframe(df)
st.subheader("Editable table")
edited = st.data_editor(df)
st.write("Edited data:")
st.write(edited)