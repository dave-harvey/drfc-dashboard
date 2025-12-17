import streamlit as st
import pandas as pd
from src.plots import scatter_plot

# --------------------------
# Load data from JSON file
# --------------------------
@st.cache_data
def load_data():
    df_raw = pd.read_json("data/efl_1_20251209.json")
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


    tab_freq, tab_qual = st.tabs(["Frequency", "Quality"])

    with tab_freq:
        st.subheader("Frequency — Shot Volume")
        st.write("This chart shows how often Doncaster Rovers create shots and how many they allow the opposition to take. It reflects the team’s overall attacking and defensive activity.")

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

    with tab_qual:
        st.subheader("Quality — Expected Goals")
        st.write("This chart shows the quality of chances created and conceded, using expected goals (xG) for and expected goals against (xGA). It indicates how dangerous Doncaster Rovers are in attack and how well they limit opposition chances.")

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
