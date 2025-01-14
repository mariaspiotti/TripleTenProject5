# Importing Required Libraries:
import streamlit as st
import pandas as pd
import plotly.express as px
data = pd.read_csv ('C:\\Users\\mspio\\Documents\\TripleTenProject5VS\\vehicles_us.csv')
# Header
st.header("My Data Analysis Dashboard")
# Histogram
st.subheader("Price Distibrution")
histogram = px.histogram(data, x='price')
st.plotly_chart(histogram)

# Scatter Plot
st.subheader("Scatter Plot of Odometer Reading vs Price")
scatter_plot = px.scatter(data, x='odometer', y='price')
st.plotly_chart(scatter_plot)
show_histogram = st.checkbox("Show Histogram")
if show_histogram:
    st.plotly_chart(histogram)
