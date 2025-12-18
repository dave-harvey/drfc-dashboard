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
                "<h3 style='margin-bottom: 0; text-transform: uppercase;'>Outcomes</h3>",
                unsafe_allow_html=True
            )

            st.markdown(
                """
                Outcomes focus on what happens on the scoreboard. This view shows how often Doncaster Rovers
                score and concede goals, and allows those results to be compared with underlying performance
                to highlight where outcomes reflect, or diverge from, the process.
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
                "<h3 style='margin-bottom: 0; text-transform: uppercase;'>Conversion - Goals Scored & Conceded</h3>",
                unsafe_allow_html=True
            )

            # Add a bit of vertical space
            st.write("")

            scatter_plot(
                df=df,
                x="Goals",
                y="Goals_Against",
                title="Goals vs Goals Against",
                xLabel="Average Goals",
                yLabel="Average Goals Against",
                highlight_team=team_to_highlight,
                interactive=False,
            )
