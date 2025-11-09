import streamlit as st, time
st.title("Cached Computation Demo")
@st.cache_data
def slow_square(x):
    time.sleep(2)
    return x * x
n = st.number_input("Enter a number", 0, 100, 10)
st.write("Result:", slow_square(n))