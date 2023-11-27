import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

MIN_VAL = 1
MAX_VAL = 5000
num = 100

st.title('Illustrating the Central Limit Theorem with Streamlit')
st.subheader('An App by Akshat Kumar')
st.write('This app simulates a thousand coin flips using the chance of heads input below,',
         ' and then samples with replacement from that population and plots the histogram of the',
         ' means of the samples in order to illustrate the central limit theorem!')

perc_heads = st.number_input(label='Chance of Coins Landing on Heads', 
                             min_value=0.0, 
                             max_value=1.0,
                             value=0.5)
binom_dist = np.random.binomial(1, perc_heads, 100)
list_of_means = []

for i in range(0,1000):
    list_of_means.append(np.random.choice(binom_dist, num, replace=True).mean())

title = st.text_input(label='Graph Title')    
fig, ax = plt.subplots()

plt.hist(list_of_means, range=[0,1])
plt.title(title)

st.pyplot(fig)

num = st.slider("Sample Size:", min_value=MIN_VAL, max_value=MAX_VAL, value=100)

st.button('Re-run')
