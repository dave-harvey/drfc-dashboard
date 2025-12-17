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

    st.subheader("Conversion — Goals vs Goals Against")
    st.write("This chart shows goals scored and conceded, illustrating how effectively Doncaster Rovers convert their chances and prevent the opposition from scoring.")

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

