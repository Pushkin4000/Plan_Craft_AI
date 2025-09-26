import streamlit as st
import langchain_helpz
import time

st.title("Plan Craft AI")
Technology=st.text_input("Enter the name of technology for project ideas and procedures:")



if Technology:
    with st.spinner(text="Please wait uwu!!!!!!"):
        response=langchain_helpz.techo(Technology)
    st.header(response["project_name"])
    zap=response["Procedure"].split(",")
    for items in zap:
        st.write(items)
    st.snow()


   