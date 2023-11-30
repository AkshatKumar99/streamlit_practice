import streamlit as st
import numpy as np
import pickle

st.title('Penguin Classifer')
st.write('This app uses six inputs to predict the species of penguin using a model build on the Palmer Penguins dataset. Use the form below to get started!')

with open('rf_penguin.pkl', 'rb') as f:
	rfc = pickle.load(f)

with open('output_penguin.pkl', 'rb') as f:
	unique_penguin_mapping = pickle.load(f)

with st.form('user_inputs'):
	island = st.selectbox("Penguin Island", options=[
		"Biscoe", "Dream", "Torgerson"])
	sex = st.selectbox("Sex", options=['Female', 'Male'])
	bill_length = st.number_input("Bill Length (mm)", 
		min_value=0)
	bill_depth = st.number_input("Bill Depth (mm)", 
		min_value=0)
	flipper_length = st.number_input("Flipper Length (mm)", min_value=0)
	body_mass = st.number_input("Body Mass (g)", min_value=0)
	st.form_submit_button()

#user_inputs = [island, sex, bill_length, 
#			   bill_depth, flipper_length, body_mass]
#st.write(f"The user inputs are {user_inputs}")

island_bins = {'Biscoe': [1,0,0],
				'Dream': [0,1,0],
				'Torgerson': [0,0,1]}

island_biscoe, island_dream, island_torgerson = island_bins[island]

sex_male, sex_female = 0, 0
if sex == 'Female':
	sex_female = 1
elif sex == 'Male':
	sex_male = 1

new_prediction = rfc.predict(np.array([bill_length, bill_depth, flipper_length, body_mass, island_biscoe, island_dream, island_torgerson, sex_female, sex_male]).reshape(1,-1))

pred = unique_penguin_mapping[new_prediction][0]

st.subheader('Predicting Your Penguin\'s Species')
st.write(f'We predict your penguin is of the {pred} species')





