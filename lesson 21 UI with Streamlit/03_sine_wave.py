import streamlit as st, numpy as np, matplotlib.pyplot as plt
st.title("Sine Wave Explorer")
freq = st.slider("Frequency", 1, 10, 3)
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(freq * x)
fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)