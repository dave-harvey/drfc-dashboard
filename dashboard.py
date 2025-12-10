import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from adjustText import adjust_text
from src.plots import scatter_with_labels

st.set_page_config(page_title="Football Analytics Dashboard", layout="wide")

st.title("Football Analytics Dashboard")
st.write("Scatter plots for Shots, xG, and Goals data (loaded from JSON).")

# --------------------------
# Load data from JSON file
# --------------------------
@st.cache_data
def load_data():
    # JSON file must be in the same directory as app.py
    df_raw = pd.read_json("data/efl_1_20251209.json")
    # Rename columns to match previous code style
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
# Select team to highlight
# --------------------------
#team_to_highlight = st.sidebar.selectbox("Highlight a team", df["Team"].unique())
team_to_highlight = "Doncaster Rovers"


# --------------------------
# Layout: three charts side-by-side
# --------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.pyplot(
        scatter_with_labels(
            df,
            x="Shots",
            y="Shots_Against",
            title="Shots vs Shots Against",
            xLabel="Shots/90",
            yLabel="Shots Against/90",
            highlight_team=team_to_highlight
        )
    )

with col2:
    st.pyplot(
        scatter_with_labels(
            df,
            x="xG",
            y="xGA",
            title="xG vs xGA",
            xLabel="xG/90",
            yLabel="xGA/90",
            highlight_team=team_to_highlight
        )
    )

with col3:
    st.pyplot(
        scatter_with_labels(
            df,
            x="Goals",
            y="Goals_Against",
            title="Goals vs Goals Against",
            xLabel="Goals/90",
            yLabel="Goals Against/90",
            highlight_team=team_to_highlight
        )
    )
