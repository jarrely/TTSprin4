import streamlit as st 
import pandas as pd
import math as mt
import numpy as np
import plotly.express as px
import sys
sys.setrecursionlimit(60000)
# necessary to avoid recursion errors later
## Based on the sample data set I am going to move forward wth the fllowing assumptions:
####    - Nan values on the 4wd section mean it is not 4 wheel drve
####    - model_year: fill by median year (don4t drop rows with NaNs in this column) 
####    - cylindres: fill by median cylindres 
####    - Removing  vehices priced over 60K.
####    - Removing vehicls with missing odometer data. Mileage is a very important determning factor
#  on buying a vehicle, and if you don't know what it is I persnally woudn't buy it. Too big of a risk

# Vehice Df cleanup 
vehicles=pd.read_csv('vehicles_us.csv',sep=',')
def median_fill(df, column):
    df[column].fillna(df[column].median(), inplace=True)
    return df
median_fill(vehicles,"cylinders")
median_fill(vehicles,"model_year")
#vehiclesv1=vehicles[vehicles['model_year'].notna()]
#vehiclesv1['make'] = vehiclesv1['model'].str.split(expand=True)[0]
vehicles['odometer'].dropna()
vehiclesv1=vehicles
vehiclesv1['is_4wd'].replace(1,'Yes', inplace=True)
vehiclesv1['is_4wd'].fillna('No',inplace=True)
vehiclesv1['make'] = vehiclesv1['model'].str.split(expand=True)[0]
vehiclesv1 = vehiclesv1[vehiclesv1['model_year']>= 1980]
vehiclesv1 = vehiclesv1[vehiclesv1['price']<= 60000]
vehiclesv2=vehiclesv1.groupby(['type','model_year'])['price'].median().reset_index()
# potly and visible information
st.header("TripleTen Sprint 4 App", divider=True)
fig1= px.scatter(vehiclesv2, x='model_year', y='price', color='type', color_discrete_sequence=[
        "#0068c9",
        "#83c9ff",
        "#ff2b2b",
        "#ffabab",
        "#29b09d",
        "#7defa1",
        "#ff8700",
        "#ffd16a",
        "#6d3fc0",
        "#d5dae5",
        "#bf9000",
        "#def4d7",
        "#a64d79",])
fig1.update_layout(title_text= 'Median Price by Vehicle Type and Model Year', xaxis_title='Model Year', yaxis_title='Median Price')
st.plotly_chart(fig1)

fig2 = px.histogram(vehiclesv1, x='model_year')
fig2.update_layout(title_text= 'Median Price by Vehicle Type and Model Year')
st.plotly_chart(fig2)

#The Graphs wil show a scatter  plot and a histogram
# for the scatterplot  it is catergorized by colors
#