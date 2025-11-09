import streamlit as st, pandas as pd, numpy as np
st.title("Random Points on a Map")
points = pd.DataFrame(np.random.randn(100, 2) / [50, 50] + [40.7128, -74.0060], columns=["lat", "lon"])
st.map(points)