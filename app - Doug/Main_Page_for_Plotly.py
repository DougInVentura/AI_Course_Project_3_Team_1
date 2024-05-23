import streamlit as st


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
    layout="wide"
)


st.write("""# 👋 Welcome to Plotly 👋
### Web-Based Application to Automate Graphing and Exploratory Data Analysis
### Project 3 ASU AI Course: Geoff McDaniel, Chris Alvarez, Doug Francis
         
##### Version 1.0""")


if st.button(":blue[Click Here] to select a csv file with your data to begin"):
    st.switch_page("pages/1_Select_data_file_and_init_proc.py")


