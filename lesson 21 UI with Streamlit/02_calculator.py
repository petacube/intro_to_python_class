import streamlit as st
st.title("Simple Calculator")
a = st.number_input("First number", value=0.0)
b = st.number_input("Second number", value=0.0)
op = st.selectbox("Operation", ["+", "-", "*", "/"])
if op == "+": result = a + b
elif op == "-": result = a - b
elif op == "*": result = a * b
else: result = "∞" if b == 0 else a / b
st.write("Result:", result)