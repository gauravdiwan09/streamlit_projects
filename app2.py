import streamlit as st

if st.checkbox("Add Masala"):
    st.write("masala is added to your chai!")

if st.button("make chai"):
    st.success("your chai is ready!!")

tea_base = st.radio("pick your chai base: ", ["milk", "water", "almond_milk"])
st.write(f"your selected base is {tea_base}")

sugar = st.slider("sugar spoon", 0, 5, 2)
st.write(f"selecter sugar spoon {sugar}")

cups = st.number_input("How many cups", min_value=1, max_value=10, step=1)
st.write(f"your order of {cups} cup of tea has been taken!")

name = st.text_input("enter your name!")
if name:
    st.write(f"welcome, {name}")
    st.write("your tea is on the way!")

dob = st.date_input("enter your date of birth!")
st.write(f"your dob is {dob}")
