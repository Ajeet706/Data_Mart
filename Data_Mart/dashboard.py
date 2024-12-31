# dashboard.py
import streamlit as st
import plotly.express as px
import pandas as pd

# Sample data
df = pd.DataFrame({
    "Category": ["A", "B", "C", "D"],
    "Values": [10, 20, 15, 25]
})

st.title("Interactive Dashboard")
st.write("This is a sample dashboard using Streamlit and Plotly.")

# Plotly chart
fig = px.bar(df, x="Category", y="Values", title="Sample Bar Chart")
st.plotly_chart(fig)
