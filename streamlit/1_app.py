import random
import numpy as np
import pandas as pd
import streamlit as st

st.title("Welcome $@! **7")

df1 = pd.DataFrame(np.random.randn(5,2), columns=["First_Column", "Second_Column"], index=[i for i in range(1,6)])
st.write("Data Frame 1:")
st.write(df1)

df2 = pd.DataFrame(np.random.randint(10,20, size=(5,2)), columns=["First_Column", "Second_Column"], index=[i for i in range(1,6)])
st.write("Data Frame 2:")
st.write(df2)
st.line_chart(df2)

df3 = pd.DataFrame({"1st_column" : [i for i in range(11)], "2nd_column" : [i**2 for i in range(11)]})
st.write("Data Frame 3:")
st.write(df3)
st.line_chart(df3, x="1st_column", y="2nd_column")