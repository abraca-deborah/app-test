import streamlit as st
import pandas as pd

st.title("This is a Test App")
st.write("Hello. My name is *REDACTED*")

user_name = st.text_input ("Guess my name!")

if st.button("Submit"):
    st.write("Good guess!")