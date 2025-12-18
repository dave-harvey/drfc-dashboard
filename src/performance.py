import streamlit as st
import pandas as pd
from src.plots import scatter_plot

# --------------------------
# Load data from JSON file
# --------------------------
@st.cache_data
def load_data():
    df_raw = pd.read_json("data/efl_1_20251218.json")
    df = df_raw.rename(
        columns={
            "name": "Team",
            "shots": "Shots",
            "shotsAgainst": "Shots_Against",
            "xG": "xG",
            "xGA": "xGA",
            "goals": "Goals",
            "goalsAgainst": "Goals_Against",
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
                "<h3 style='margin-bottom: 0; text-transform: uppercase;'>Performance</h3>",
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

            st.caption("Data reflects matches played up to and including 9 December 2025.")

            # Add a bit of vertical space
            st.write("")


    secondCols = st.columns(1)

    with secondCols[0]:
        with st.container(border=True):
            st.markdown(
                "<h3 style='margin-bottom: 0; text-transform: uppercase;'>Frequency - Shot Volume</h3>",
                unsafe_allow_html=True
            )

            # Add a bit of vertical space
            st.write("")

            scatter_plot(
                df=df,
                x="Shots",
                y="Shots_Against",
                title="Shots vs Shots Against",
                xLabel="Average Shots",
                yLabel="Average Shots Against",
                highlight_team=team_to_highlight,
                interactive=False,
            )

    thirdCols = st.columns(1)
    with thirdCols[0]:
        with st.container(border=True):
            st.markdown(
                "<h3 style='margin-bottom: 0; text-transform: uppercase;'>Quality - Expected Goals</h3>",
                unsafe_allow_html=True
            )

            # Add a bit of vertical space
            st.write("")

            scatter_plot(
                df=df,
                x="xG",
                y="xGA",
                title="xG vs xGA",
                xLabel="Average xG",
                yLabel="Average xGA",
                highlight_team=team_to_highlight,
                interactive=False,
            )
