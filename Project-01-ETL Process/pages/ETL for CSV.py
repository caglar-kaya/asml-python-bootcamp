import pandas as pd
import streamlit as st

st.markdown("# ETL Process for CSV")
st.sidebar.markdown("# CSV")

df1 = pd.read_csv('Company-A/employees.csv')
df2 = pd.read_csv('Company-B/employees.csv')

"""
### Old CSV
"""

st.dataframe(df1)

"""
### New CSV
"""

st.dataframe(df2)
