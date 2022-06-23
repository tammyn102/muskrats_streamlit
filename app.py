# To run: python -m streamlit run app.py
import streamlit as st
import pandas as pd

# Load in data
df = pd.read_csv("data.csv").drop(['_c0'],axis=1)

st.write("""# Muskrats Streamlit App""")

st.write("## Our dataset:")
st.write(df)

st.write("## Top ten highest budgeted movies:")
st.write(df.sort_values("budget",ascending=False).head(10))