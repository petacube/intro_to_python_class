import streamlit as st, pandas as pd
st.title("Download CSV")
df = pd.DataFrame({"x": [1, 2, 3], "y": [10, 20, 30]})
csv = df.to_csv(index=False).encode("utf-8")
st.dataframe(df)
st.download_button("Download as CSV", data=csv, file_name="data.csv", mime="text/csv")