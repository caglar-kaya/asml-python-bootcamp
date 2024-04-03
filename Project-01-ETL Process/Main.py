import streamlit as st

st.markdown("# Welcome Everyone 🎈")

st.markdown("## **Data Engineering** - ETL Processes with Python")

st.sidebar.markdown("# Main")

st.markdown("> This project demonstrates how to work with directories and data in Python. It mainly discusses the creation/deletion of directories, creation of files with data, and the extraction, transformation, loading (ETL) principles of data.")

st.markdown("### 1. Project Setup")

st.markdown("- Python")
st.markdown("- os Package")
st.markdown("- pandas Package")
st.markdown("- streamlit Package")

st.markdown("### 2. How it Works")

st.markdown("> The project is divided into four main steps:")

st.markdown("2.1. **Creating Directories:** Code checks and creates two directories, \"Company-A\" and \"Company-B\" if they don't exist already.")

st.markdown("2.2. **Creating and Storing Data for Company-A:** A pandas DataFrame is created with mock employee data. This DataFrame is then exported as an Excel sheet, CSV file and text file in the \"Company-A\" directory.")

st.markdown("2.3. **ETL Process:** Files from \"Company-A\" are read and transformed (sorted based on employee names), then written to the \"Company-B\" directory.")

st.markdown("### 3. Note")

st.markdown("> Ensure you have the necessary Python libraries installed and ensure the read/write permissions are properly set for the directories before running the script.")
