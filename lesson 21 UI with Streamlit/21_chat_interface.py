import streamlit as st
st.title("Echo Chatbot")
if "chat" not in st.session_state:
    st.session_state.chat = []
for role, msg in st.session_state.chat:
    with st.chat_message(role):
        st.write(msg)
prompt = st.chat_input("Say something")
if prompt:
    st.session_state.chat.append(("user", prompt))
    st.session_state.chat.append(("assistant", f"You said: {prompt}"))
    st.experimental_rerun()