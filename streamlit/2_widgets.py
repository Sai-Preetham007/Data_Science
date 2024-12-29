import pandas as pd
import streamlit as st

st.title("Welcome $@! **7 :")

name = st.text_input("Enter Your Name:")
if name:
    st.write(f"Hello {name}")

age = st.slider("Select Your Age:", 0,100,25)
st.write(f"Age : {age}")

lang = st.selectbox("Choose Your Favourite language:", ["C", "C++", "Java", "python"])
st.write(f"Fav lang : {lang}")

read_file = st.file_uploader("Choose a csv file:", type="csv")
if read_file:
    df = pd.read_csv(read_file)
    st.write(df)