import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('California Hosuing Data (1990) by Anthony Pappalardo')
df = pd.read_csv('housing.csv')

price_filter = st.slider('Median House Price', 0, 500001, 200000) # min, max, default

location_filter = st.sidebar.multiselect(
    'Choose the location',
    df.ocean_proximity.unique(),
    df.ocean_proximity.unique())

income_filter = st.sidebar.radio(
    'Choose the location'
    ('Low', 'Medium', 'High'))

df = df[df.median_house_value <= price_filter]
df = df[df.ocean_proximity.isin(location_filter)]

if income_filter == 'Low':
    df = df[(df.median_income <= 2.5)]
elif income_filter == 'Medium':
    df = df[(df.median_income < 2.5) & (df.median_income < 4.5)]
else:
    df = df[(df.median_income >= 4.5)]
            
st.subheader('Seaborn more filters in the sidebar:')
st.map(df)
    
st.subheader('Histogram of the Median House Value')
fig, ax = plt.subplots()
df.median_house_value.hist(ax = ax, bins = 30)
st.pyplot(fig)
