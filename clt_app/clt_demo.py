import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

MIN_VAL = 1
MAX_VAL = 5000
num = 100

st.write('# Central Limit Theorem App')

binom_dist = np.random.binomial(1, .5, 100)
list_of_means = []

for i in range(0,1000):
    list_of_means.append(np.random.choice(binom_dist, num, replace=True).mean())
    
fig, ax = plt.subplots()

ax = plt.hist(list_of_means)

st.pyplot(fig)

num = st.slider("Sample Size:", min_value=MIN_VAL, max_value=MAX_VAL, value=100)

st.button('Re-run')
