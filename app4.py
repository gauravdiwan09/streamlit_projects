import streamlit as st
import pandas as pd

st.title("Employee Dashboard!")
file = st.file_uploader("Upload your CSV file", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Preview")
    st.dataframe(df)

if file:
    st.subheader("Summary of the CSV data")
    st.write(df.describe())

if file:
    cities = df['city'].unique()
    choosed_city = st.selectbox("choose your city to check the data accordingly!", cities)
    filtered_df = df[df['city']==choosed_city]
    st.dataframe(filtered_df)