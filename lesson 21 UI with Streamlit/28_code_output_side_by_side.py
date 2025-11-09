import streamlit as st, textwrap
st.title("Show Code & Output")
code = textwrap.dedent("""
def square(x):
    return x * x
""")
col1, col2 = st.columns(2)
with col1:
    st.code(code, language="python")
with col2:
    st.write("square(5) =", 5 * 5)