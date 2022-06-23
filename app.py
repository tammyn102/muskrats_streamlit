# To run: python -m streamlit run app.py
import streamlit as st
import pandas as pd

# Load in data
df = pd.read_csv("data.csv").drop(['_c0'],axis=1)

st.write("""# Muskrats Streamlit App""")
st.write("## Our dataset:")
st.write(df)

map_location = pd.DataFrame(
    [(43.815, -111.785), (43.811, -111.779)],
    columns=['lat','lon']
)

st.write("Here is a map:")
st.map(map_location)