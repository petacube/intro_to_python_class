import streamlit as st
st.title("Tabs Demo")
tab1, tab2, tab3 = st.tabs(["Intro", "Code", "Results"])
with tab1: st.write("High-level description.")
with tab2: st.code("print('hello streamlit')", language="python")
with tab3: st.write("Show results here.")