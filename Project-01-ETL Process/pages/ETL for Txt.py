import pandas as pd
import streamlit as st

st.markdown("# ETL Process for Txt")
st.sidebar.markdown("# Txt")

df1 = pd.read_csv('Company-A/employees.txt', sep=' ')
df2 = pd.read_csv('Company-B/employees.txt', sep=' ')

"""
### Old Txt
"""

st.dataframe(df1)

"""
### New Txt
"""

st.dataframe(df2)
