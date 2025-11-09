import streamlit as st
st.title("Inline Help with Popover")
with st.popover("What is this app?"):
    st.write("This demonstrates using a popover as contextual help.")
    st.code("with st.popover('Title'):\n    st.write('Content')")
value = st.slider("Adjust value", 0, 100, 50)
st.write("Value:", value)