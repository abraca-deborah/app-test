import streamlit as st
import pandas as pd

editorPassword = "GoEagles2026!"

st.title("Edits Page")

password = st.text_input("Type Password Here: ")

if password == editorPassword:
    #add code here later
    st.text("Fantastic!")

