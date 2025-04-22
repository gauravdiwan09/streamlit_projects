import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.header("masala chai")
    st.image("https://masalaandchai.com/wp-content/uploads/2021/07/Masala-Chai-Featured.jpg", width=200)
    vote1 = st.button("vote for masala chai")

with col2:
    st.header("adrak chai")
    st.image("https://www.indianhealthyrecipes.com/wp-content/uploads/2023/07/ginger-milk-tea-adrak-chai-recipe.jpg", width=200)
    vote2 = st.button("vote for adrak chai")

if vote1:
    st.success("Thanks for voting masala chai!")
elif vote2:
    st.success("Thanks for voting adrak chai")

name = st.sidebar.text_input("Enter your name")
fav_chai = st.sidebar.selectbox("which is fav chai ?", ["masala chai", "adrak chai", "green tea", "lemon tea"])

st.write(f"{name}, you like {fav_chai} the most!")

with st.expander("Here are the instructions to make a simple chai"):
    st.write("""
    1) boil the water and put some tea powder in it.
    2) add milk and sugar as per your taste!
    3) your chai will be ready!
""")