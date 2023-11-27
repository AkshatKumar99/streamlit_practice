import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns
import time

@st.cache_data()
def load_file(penguin_file):
    time.sleep(3)
    if penguin_file is not None:
        df = pd.read_csv(penguin_file)
    else:
        df = pd.read_csv('penguins.csv')
    return df

st.title("Palmer's Penguins")
st.markdown('Use this Streamlit app to make your own scatterplot about penguins!')

#penguins_subset = penguins_df[penguins_df['species'] == selected_species]
penguin_file = st.file_uploader('Select Your Local Penguins CSV(default provided)')
penguins_df = load_file(penguin_file)

selected_x_var = st.selectbox('What do you want the x variable to be?',
                              ['bill_length_mm', 'bill_depth_mm', 
                               'flipper_length_mm', 'body_mass_g'])
selected_y_var = st.selectbox('What about the y?',
                              ['bill_length_mm', 'bill_depth_mm',
                               'flipper_length_mm', 'body_mass_g'])
selected_gender = st.selectbox('What gender do you want to filter for?',
                               ['all_penguins', 'male penguins', 'female penguins'])

if selected_gender == 'male penguins':
    penguins_df = penguins_df[penguins_df.sex == 'male']
elif selected_gender == 'female penguins':
    penguins_df = penguins_df[penguins_df.sex == 'female']
else:
    pass

alt_chart = (
    alt.Chart(penguins_df, title=f'Scatterplot of Palmer\'s Penguins')
    .mark_circle()
    .encode(
        x=selected_x_var,
        y=selected_y_var,
        color='species'
    )
).interactive() 

st.altair_chart(alt_chart, use_container_width=True)
 
 
 
 