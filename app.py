# To run: python -m streamlit run app.py
import streamlit as st
import pandas as pd

# Load in data
df = pd.read_csv("data.csv").drop(['_c0'],axis=1)

st.write("""# Muskrats Streamlit App""")

st.write("## Our dataset:")
st.write(df)

st.write("## Top highest budgeted movies:")
x = st.slider('Number of movies to display:', value=5, min_value=1, max_value=50)
st.write(df.sort_values("budget",ascending=False).head(x))