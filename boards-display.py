import streamlit as st
import pandas as pd
import json

st.set_page_config(page_title = "LEADERBOARDS")

with open("data.json", "r") as file:
    data = json.load(f)

st.title(data["title"])

st.image(data[image])

st.bar_chart(None, x = "Grade", y ="Points")