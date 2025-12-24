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
                This view tracks Doncaster Rovers’ underlying performance across the season using rolling
                six-match averages.

                - <span style="color:#00cc44; font-weight:800;">xG vs xGA:</span>
                Compares expected goals for and against over time, showing how attacking output and defensive
                performance have evolved across the season.

                - <span style="color:#00cc44; font-weight:800;">xGD:</span>
                Displays the rolling expected goal difference, summarising the balance between chance creation
                and prevention and highlighting periods of stronger or weaker underlying performance.
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
                "<h3 style='margin-bottom: 0; text-transform: uppercase;'>Expected Goals</h3>",
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
                show_zero_line=True,
            )
