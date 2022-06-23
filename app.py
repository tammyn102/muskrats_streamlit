# To run: python -m streamlit run app.py
import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'A': [1,2,3,4],
    'B': [5,6,7,8]
})

st.write("Here is a data frame:")
st.write(df)

map_location = pd.DataFrame(
    [(43.815, -111.785), (43.811, -111.779)],
    columns=['lat','lon']
)

st.write("Here is a map:")
st.map(map_location)