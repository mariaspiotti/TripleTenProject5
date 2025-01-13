# TripleTenProject5
# Web Application Dashboard Project

## Project Description
This project aimed to enhance my software engineering skills by building and deploying a web application dashboard to the Render cloud service. I worked with a dataset on car sales advertisements and applied my data skills to create interactive visualizations.

## Table of Contents
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Developing the Web Application](#developing-the-web-application)
- [Deployment](#deployment)
- [Submission](#submission)
- [Evaluation Criteria](#evaluation-criteria)

## Getting Started

### Prerequisites
- Created an account on [GitHub](https://github.com).
- Created a new Git repository with a `README.md` file and a `.gitignore` file (using the Python template).
- Created a new Python environment and installed the following packages:
  
  conda install pandas streamlit plotly-express altair
•	Created an account on Render and linked it to my GitHub account.
•	Cloned project’s Git repository to local machine:
git clone https://github.com/mariaspiotti/TripleTenProject5.git
## Project Setup
1.	Opened the project directory in Visual Studio Code.
2.	Set the Python interpreter to the one used by my environment.
3.	Downloaded the car advertisement dataset (vehicles_us.csv) and place it in the root directory of the project.
## Project Structure

├── README.md
├── app.py
├── vehicles_us.csv
├── notebooks
│   └── EDA.ipynb
├── requirements.txt
└── .streamlit
    └── config.toml
## Exploratory Data Analysis
•	Created an EDA.ipynb Jupyter notebook in the notebooks directory.
•	Performed exploratory analysis on the dataset, creating various visualizations using the plotly-express library.
## Developing the Web Application
1.	Created an app.py file in the root directory.
2.	Import the necessary libraries:
import streamlit as st
import pandas as pd
import plotly.express as px
3.	Read the dataset into a Pandas DataFrame and create visualizations.
4.	Added interactive components such as headers, histograms, scatter plots, and checkboxes.
## Deployment
1.	Created a requirements.txt file with the necessary packages:
pandas==2.2.3
streamlit==1.40.1
plotly==5.24.1
altair==5.0.1
2.	Created the .streamlit/config.toml file with the following content:
[server]
headless = true
port = 10000

[browser]
serverAddress = "0.0.0.0"
serverPort = 10000
3.	Deployed the application on Render by linking my GitHub repository and configuring the build and start commands.
## Submission
•	Committed changes to GitHub repository: TripleTenProject5.
•	Included the URL of the deployed app on Render.
