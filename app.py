# Importing Required Libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Loading the dataset
data = pd.read_csv('vehicles_us.csv')

# Header
st.header("My Data Analysis Dashboard")
# Slider for Price Range
price_range = st.slider("Select Price Range", 
                         min_value=int(data['price'].min()), 
                         max_value=int(data['price'].max()), 
                         value=(int(data['price'].min()), int(data['price'].max())))

# Filter data based on the selected price range
filtered_data_price = data[(data['price'] >= price_range[0]) & 
                            (data['price'] <= price_range[1])]


# Histogram
st.subheader("Price Distribution")
histogram = px.histogram(data, x='price')
st.plotly_chart(histogram)

# Slider for Odometer
odometer_range = st.slider("Select Odometer Range", 
                            min_value=int(data['odometer'].min()), 
                            max_value=int(data['odometer'].max()), 
                            value=(int(data['odometer'].min()), int(data['odometer'].max())))

# Filter data based on the selected odometer range
filtered_data = data[(data['odometer'] >= odometer_range[0]) & 
                     (data['odometer'] <= odometer_range[1])]

# Scatter Plot
st.subheader("Scatter Plot of Odometer Reading vs Price")
scatter_plot = px.scatter(filtered_data, x='odometer', y='price')
st.plotly_chart(scatter_plot)

# Checkbox for Histogram
show_histogram = st.checkbox("Show Histogram")
if show_histogram:
    st.plotly_chart(histogram)