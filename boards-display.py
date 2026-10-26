import streamlit as st
import pandas as pd

st.set_page_config(page_title = "LEADERBOARDS")

with open("data.json", "r") as file:
    data = json.load(f)

st.title(data["title"])

st.image(data[image])

st.bar_chart(None, *, "Grade", "Points", None, None, None, True, True, "stretch", "content", "this is a leaderboard")