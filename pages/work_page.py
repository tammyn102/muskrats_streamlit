# Run main_page.py first
import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
from plotnine import *

# Set the page name
st.sidebar.markdown("# Work Page")

# Load in data, and cache it so we don't have to load in a lot of data on refresh.
@st.cache
def get_data():
    return pd.read_csv("data.csv").drop(['_c0'],axis=1)
df = get_data()

# Write the title header.
st.write("""# Muskrats Streamlit App""")

# Show a table of the entire dataset.
st.write("## Our dataset:")
st.write(df)

# Show a table of the top movies by budget, with a slider to limit the number shown.
st.write("## Top highest budgeted movies:")
x = st.slider('Number of movies to display:', value=5, min_value=1, max_value=50)
# Use a cache so we can load display our sorted data quickly
@st.cache
def get_data_sorted_by_budget():
    return df.sort_values("budget",ascending=False) 
df_sorted_by_budget = get_data_sorted_by_budget()
st.write(df_sorted_by_budget.head(x))

# Show a scatter plot of movie budget vs year
st.write("## Movie budget vs. year")
plot = (
    ggplot(df.sample(1000, random_state=42).query('budget > 100'), aes(x='year',y='budget'))
    + geom_point()
    + geom_smooth()
    + theme_bw()
).draw(show=False)
st.write(plot)