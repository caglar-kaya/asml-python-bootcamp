import streamlit as st

st.markdown("# 🚀 Welcome Everyone 🎈")
st.markdown("## Data Engineering - Analyzing COVID-19 Data")

st.sidebar.markdown("# Main")

st.markdown("> This project demonstrates how to work with APIs and data in Python. It mainly discusses getting data from \
an API and extraction, transformation, loading (ETL) principles of data.")

st.markdown("### ⚙️ 1. Project Setup")
st.markdown("##### 1.1. Python")
st.markdown("##### 1.2. requests Package")
st.markdown("##### 1.3. json Package")
st.markdown("##### 1.4. pandas Package")
st.markdown("##### 1.5. streamlit Package")

st.markdown("### 🔑 2. How it works")
st.markdown("> The project is divided into three main steps:")

st.markdown("##### 2.1. EXTRACTION:")
st.markdown("&nbsp;&nbsp;&nbsp;&nbsp;It makes a get request to API to get daily Covid-19 data and stores this data as a JSON file.")

st.markdown("##### 2.2. TRANSFORMATION:")
st.markdown("&nbsp;&nbsp;&nbsp;&nbsp;It loads daily Covid-19 data into a pandas DataFrame, keeps only records that include data from all 56 states, \
removes unnecessary columns, reorders columns, renames columns, converts date column to datetime, and filters rows for year 2021 only.")

st.markdown("##### 2.3. LOADING:")
st.markdown("&nbsp;&nbsp;&nbsp;&nbsp;It stores transformed daily Covid-19 data as a CSV file.")
