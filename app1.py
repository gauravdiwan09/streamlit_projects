import streamlit as st

st.title("hello world")
st.write("Hello world")
st.subheader("hello world")
st.text("hello world")

chai = st.selectbox("choose your fav. chai",["masala chai", "lemon chai", "green tea"])

if(chai=="masala chai"):
    st.subheader("your fav. chai is masala chai wow!")
    st.success(f"you choice is excellent!")
if(chai=="lemon chai"):
    st.subheader("your fav. chai is lemon chai wow!")
    st.success(f"you choice is excellent!")
if(chai=="green tea"):
    st.subheader("your fav. chai is green tea wow!")
    st.success(f"you choice is excellent!")
