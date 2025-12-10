import streamlit as st
import pandas as pd
from src.plots import scatter_with_labels

st.set_page_config(page_title="Football Analytics Dashboard", layout="wide")

st.title("Football Analytics Dashboard")
st.write("Scatter plots for Shots, xG, and Goals data.")


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

# --------------------------
# Optional: team to highlight (sidebar)
# --------------------------
#team_to_highlight = st.sidebar.selectbox("Highlight a team", df["Team"].unique())
team_to_highlight = "Doncaster Rovers"

# --------------------------
# Tabs for the three views
# --------------------------
tab_freq, tab_qual, tab_conv = st.tabs(["Frequency", "Quality", "Conversion"])

with tab_freq:
    st.subheader("Frequency — Shot Volume")
    fig = scatter_with_labels(
        df=df,
        x="Shots",
        y="Shots_Against",
        title="Shots vs Shots Against",
        xLabel="Shots For (per match)",
        yLabel="Shots Against (per match)",
        highlight_team=team_to_highlight,
        figsize=(7, 4),
    )
    st.pyplot(fig, use_container_width=False)

with tab_qual:
    st.subheader("Quality — Expected Goals")
    fig = scatter_with_labels(
        df=df,
        x="xG",
        y="xGA",
        title="xG vs xGA",
        xLabel="xG (Expected Goals For, per match)",
        yLabel="xGA (Expected Goals Against, per match)",
        highlight_team=team_to_highlight,
        figsize=(10, 7),
    )
    st.pyplot(fig, use_container_width=False)

with tab_conv:
    st.subheader("Conversion — Goals vs Goals Against")
    fig = scatter_with_labels(
        df=df,
        x="Goals",
        y="Goals_Against",
        title="Goals vs Goals Against",
        xLabel="Goals Scored (per match)",
        yLabel="Goals Conceded (per match)",
        highlight_team=team_to_highlight,
        figsize=(10, 7),
    )
    st.pyplot(fig, use_container_width=False)
