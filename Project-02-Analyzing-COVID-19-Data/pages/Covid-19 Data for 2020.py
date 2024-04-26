import pandas as pd
import streamlit as st

st.markdown("# Covid-19 Data for 2020")

df = pd.read_csv('transformed_daily_covid_data_for_2020.csv')

df = df.drop(df.columns[0], axis=1)

st.dataframe(df)

st.line_chart(pd.DataFrame(df), x='Date', y=['Negative Tests', 'Positive Tests', 'Total Test Results'])
