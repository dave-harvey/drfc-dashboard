import streamlit as st
import pandas as pd
from src.plots import scatter_with_labels

st.set_page_config(page_title="Football Analytics Dashboard", layout="wide")

st.title("Doncaster Rovers Dashboard")
st.write("Basic analysis of Doncaster Rovers in EFL League One 2025/25.  This shows an indicator of both performance and outcomes.")
st.write("Performance is determined through two sets of metrics:")
st.write("- **Frequency** - the volume of shots created or conceded.")
st.write("- **Quality** - the quality of shots created or conceded measured by the expected goals (xG and xGA).")
st.write("Outcomes are determined through the conversion of the shots into goals.  This is measured by goals for and against. ")

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
        xLabel="Shots / 90",
        yLabel="Shots Against / 90",
        highlight_team=team_to_highlight,
        figsize=(7, 5),
    )
    st.pyplot(fig, use_container_width=False)

with tab_qual:
    st.subheader("Quality — Expected Goals")
    fig = scatter_with_labels(
        df=df,
        x="xG",
        y="xGA",
        title="xG vs xGA",
        xLabel="xG / 90",
        yLabel="xGA / 90",
        highlight_team=team_to_highlight,
        figsize=(7, 5),
    )
    st.pyplot(fig, use_container_width=False)

with tab_conv:
    st.subheader("Conversion — Goals vs Goals Against")
    fig = scatter_with_labels(
        df=df,
        x="Goals",
        y="Goals_Against",
        title="Goals vs Goals Against",
        xLabel="Goals / 90",
        yLabel="Goals Against / 90",
        highlight_team=team_to_highlight,
        figsize=(7, 5),
    )
    st.pyplot(fig, use_container_width=False)
