import streamlit as st
import pandas as pd
import json

editorPassword = "GoEagles2026!"

st.title("Edits Page")

password = st.text_input("Type Password Here: ")

if password == editorPassword:
    #add code here later
    st.text("Fantastic!")

    #Option to change title
    title = st.text_input("New Title: " value = data["title"])

    #Option to change image
    image = st.file_uploader("Sprite: ")

    #Option to change horizontal or not
    horizontal = True

    #Option to change number of columns/rows (meant to show the different people participating in the leaderboard)
    players = st.number_input("Number of Participants: ", 1, 30)

    #Option to change number of points (or maybe just set it to 10?)
    points = st.number_input("Points Possible: ", 1, 10)

    #Option to change each person's number of points (inc by 1)


    if st.button("Save Changes"):
        update = {
            "title" = title,
            "image" = image,
            "horizontal" = horizontal,
            "players" = players,
            "points" = points
        }

        with open("data.json", "w") as file:
            json.dump(update, f, indent = 4)

        st.success("Changes saved!")
        st.balloons()


