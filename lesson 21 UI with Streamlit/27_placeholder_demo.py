import streamlit as st, time
st.title("Dynamic Placeholder Demo")
slot = st.empty()
for i in range(5):
    slot.write(f"Step {i+1}/5")
    time.sleep(0.5)
slot.success("Finished updating placeholder!")