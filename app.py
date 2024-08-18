import streamlit as st 
import pandas as pd
import math as mt
import numpy as np
import plotly.express as px
# Vehice Df cleanup 
vehicles=pd.read_csv('vehicles_us.csv',sep=',')
vehiclesv1=vehicles[vehicles['model_year'].notna()]
vehiclesv1['make'] = vehiclesv1['model'].str.split(expand=True)[0]
vehiclesv1['is_4wd'].replace(1,'Yes', inplace=True)
vehiclesv1['is_4wd'].fillna('No',inplace=True)
vehiclesv2=vehiclesv1.groupby(['type','model_year'])['price'].median().reset_index()
# potly and visible information
st.header("TripleTen Sprint 4 App", divider=True)
fig1= px.scatter(vehiclesv2, x='model_year', y='price', color='type')
fig1.update_layout(title_text= 'Median Price by Vehicle Type and Model Year', xaxis_title='Model Year', yaxis_title='Median Price')
fig1.show()