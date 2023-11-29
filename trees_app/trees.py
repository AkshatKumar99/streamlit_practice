import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import plotly.express as px
from bokeh.plotting import figure
import altair as alt


st.title('SF Trees')
st.write(
    """This app analyzes trees in San Francisco using a dataset 
    kindly provided by SF DPW"""
)

st.subheader('Plotly Chart')
trees_df = pd.read_csv('trees.csv')
fig = px.histogram(trees_df['dbh'])
st.plotly_chart(fig)

st.subheader('Plotly Chart')
trees_df = pd.read_csv('trees.csv')
trees_df['age'] = (pd.to_datetime('today') - pd.to_datetime(trees_df['date'])).dt.days

st.subheader('Seaborn Chart')
fig_sb, ax_sb = plt.subplots()
ax_sb = sns.histplot(trees_df['age'])
plt.xlabel('Age (Days)')
st.pyplot(fig_sb)

st.subheader('Matplotlib Chart')
fig_mpl, ax_mpl = plt.subplots()
ax_mpl = plt.hist(trees_df['age'])
plt.xlabel('Age (Days)')
st.pyplot(fig_mpl)

st.subheader('Bokeh Chart')
scatterplot = figure(title='Bokeh Scatterplot')
scatterplot.scatter(trees_df['dbh'], trees_df['site_order'])
scatterplot.yaxis.axis_label = 'site_order'
scatterplot.xaxis.axis_label = 'dbh'
st.bokeh_chart(scatterplot)

st.subheader('Altair Chart')
df_caretaker = trees_df.groupby(['caretaker']).count()['tree_id'].reset_index()
df_caretaker.columns = ['caretaker', 'tree_count']
fig = alt.Chart(df_caretaker).mark_bar().encode(x='caretaker', y='tree_count')
st.altair_chart(fig)

st.subheader('Altair Chart - Alternative Method')
fig = alt.Chart(trees_df).mark_bar().encode(x='caretaker', y='count(*):Q')
st.altair_chart(fig)




 
