import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import pandas as pd

st.write(1234)

df = pd.read_csv("class2022.csv")
df

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig