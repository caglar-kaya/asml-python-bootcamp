import pandas as pd
import streamlit as st

st.markdown("# ETL Process for Excel")
st.sidebar.markdown("# Excel")

df1 = pd.read_excel('Company-A/employees.xlsx')
df2 = pd.read_excel('Company-B/employees.xlsx')

"""
### Old excel
"""

st.dataframe(df1)

"""
### New excel
"""

st.dataframe(df2)
