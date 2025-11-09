import streamlit as st, time
st.title("Progress Bar Demo")
progress = st.progress(0)
status = st.empty()
for i in range(101):
    time.sleep(0.02)
    progress.progress(i)
    status.text(f"Completed: {i}%")
st.success("Done!")