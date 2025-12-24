from src.helpers import data_source_caption
import streamlit as st
import pandas as pd
from src.line_chart import line_chart

# --------------------------
# Load data from JSON file
# --------------------------
@st.cache_data
def load_data():
    df_raw = pd.read_json("data/matches.json")
    df = df_raw.rename(
        columns={
            "match": "Match",
            "xG": "xG",
            "xGA": "xGA",
            "xGD": "xGD"
        }
    )
    return df


df = load_data()

def render():
    team_to_highlight = "Doncaster Rovers"

    firstCols = st.columns(1)

    with firstCols[0]:
        with st.container(border=True):
            st.markdown(
                "<h3 style='margin-bottom: 0; text-transform: uppercase;'>Performance Tracker</h3>",
                unsafe_allow_html=True
            )

            st.markdown(
                """
                We assess Doncaster Rovers’ performance from two complementary perspectives:

                - <span style="color:#00cc44; font-weight:800; text-transform: uppercase;">Frequency:</span>
                Reflects how often chances are created and how many shots are conceded, capturing the team’s
                overall attacking and defensive activity.

                - <span style="color:#00cc44; font-weight:800; text-transform: uppercase;">Quality:</span>
                Measures the standard of those chances using expected goals (xG) for and expected goals against (xGA),
                indicating how dangerous Doncaster Rovers are in attack and how effectively they limit opposition opportunities.
                """,
                unsafe_allow_html=True
            )
            # Add a bit of vertical space
            st.write("")

            data_source_caption()

            # Add a bit of vertical space
            st.write("")


    secondCols = st.columns(1)

    with secondCols[0]:
        with st.container(border=True):
            st.markdown(
                "<h3 style='margin-bottom: 0; text-transform: uppercase;'>Excpeted Goals</h3>",
                unsafe_allow_html=True
            )

            # Add a bit of vertical space
            st.write("")

            line_chart(
                df=df,
                x="Match",
                series1="xG",
                series2="xGA",
                title="Rolling 6-game average xG and xGA",
                series1Label="xG",
                series2Label="xGA",
            )

    thirdCols = st.columns(1)
    with thirdCols[0]:
        with st.container(border=True):
            st.markdown(
                "<h3 style='margin-bottom: 0; text-transform: uppercase;'>Expected Goal Difference</h3>",
                unsafe_allow_html=True
            )

            # Add a bit of vertical space
            st.write("")

            line_chart(
                df=df,
                x="Match",
                series1="xGD",
                title="Rolling 6-game average xGD",
            )
