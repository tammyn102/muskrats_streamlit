# To run: python -m streamlit run app.py
import streamlit as st
import pandas as pd

st.sidebar.markdown("# Work Page")

# Load in data.
df = pd.read_csv("data.csv").drop(['_c0'],axis=1)

# Write the title header.
st.write("""# Muskrats Streamlit App""")

# Show a table of the entire dataset.
st.write("## Our dataset:")
st.write(df)

# Show a table of the top movies by budget, with a slider to limit the number shown.
st.write("## Top highest budgeted movies:")
x = st.slider('Number of movies to display:', value=5, min_value=1, max_value=50)
st.write(df.sort_values("budget",ascending=False).head(x))