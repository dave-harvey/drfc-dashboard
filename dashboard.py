import streamlit as st
import pandas as pd
from src.plots import scatter_with_labels

st.set_page_config(page_title="Donny Dashboard", layout="wide")

st.title("Doncaster Rovers Dashboard")

st.markdown("""
This dashboard summarises Doncaster Rovers’ performances in EFL League One during the 2025/26 season, focusing on two areas: **performance** and **outcomes**.

**Performance** covers:
- **Frequency** – how often Rovers create shots and how many they concede.
- **Quality** – the standard of those chances, using expected goals (xG) for and expected goals against (xGA).

**Outcomes** reflect:
- **Conversion** – goals scored and conceded, showing how effectively chances are taken and prevented.

Each chart is divided into four quadrants. The **bottom-right** generally indicates the strongest position, combining positive attacking output with solid defensive performance. The **top-right** and **bottom-left** can still represent effective styles, while the **top-left** typically highlights teams struggling at both ends of the pitch.

_Data reflects matches played up to and including 9 December 2025._
""")


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
    st.write("This chart shows how often Doncaster Rovers create shots and how many they allow the opposition to take. It reflects the team’s overall attacking and defensive activity.")

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
    st.plotly_chart(fig, use_container_width=True)

with tab_qual:
    st.subheader("Quality — Expected Goals")
    st.write("This chart shows the quality of chances created and conceded, using expected goals (xG) for and expected goals against (xGA). It indicates how dangerous Doncaster Rovers are in attack and how well they limit opposition chances.")

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
    st.plotly_chart(fig, use_container_width=True)

with tab_conv:
    st.subheader("Conversion — Goals vs Goals Against")
    st.write("This chart shows goals scored and conceded, illustrating how effectively Doncaster Rovers convert their chances and prevent the opposition from scoring.")

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
    st.plotly_chart(fig, use_container_width=True)

