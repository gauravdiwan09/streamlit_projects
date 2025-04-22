import streamlit as st
from datetime import date

st.title("Age Calculator")

dob = st.date_input("Enter your DOB to calculate your age!", min_value=date(1900, 1, 1), max_value=date.today())

today = date.today()

# Adjust age if birthday hasn't occurred yet this year
age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

st.success(f"You are {age} years old!")
