import pandas as pd
import streamlit as st

st.markdown("# Covid-19 Data for 2021")

st.sidebar.markdown("# 2021")

df = pd.read_csv('transformed_daily_covid_data.csv')

st.dataframe(df)

st.line_chart(pd.DataFrame(df), x='Date', y=['Negative Tests', 'Positive Tests', 'Total Test Results'])
