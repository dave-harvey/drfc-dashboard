import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from adjustText import adjust_text

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
team_to_highlight = st.sidebar.selectbox("Highlight a team", df["Team"].unique())

# --------------------------
# Reusable plotting function
# --------------------------
def make_scatter(df, x, y, title):
    fig, ax = plt.subplots(figsize=(8, 6))

    # Colour + size for highlight
    df_plot = df.copy()
    df_plot["_color"] = df_plot["Team"].eq(team_to_highlight).map(
        {True: "crimson", False: "royalblue"}
    )
    df_plot["_size"] = df_plot["Team"].eq(team_to_highlight).map(
        {True: 120, False: 50}
    )

    sns.scatterplot(
        data=df_plot,
        x=x,
        y=y,
        hue="_color",
        palette=["royalblue", "crimson"],
        size="_size",
        sizes=(50, 120),
        legend=False,
        edgecolor="black",
        linewidth=0.6,
        ax=ax,
    )

    # Labels with adjustText
    texts = []
    for _, row in df_plot.iterrows():
        texts.append(ax.text(row[x], row[y], row["Team"], fontsize=8))

    adjust_text(
        texts,
        ax=ax,
        arrowprops=dict(arrowstyle="-", lw=0.5, color="gray", alpha=0.8),
    )

    # Mean reference lines
    ax.axvline(df_plot[x].mean(), ls="--", color="gray", lw=1)
    ax.axhline(df_plot[y].mean(), ls="--", color="gray", lw=1)

    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_title(title)
    ax.grid(False)

    plt.tight_layout()
    return fig

# --------------------------
# Layout: three charts side-by-side
# --------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Shots vs Shots Against")
    st.pyplot(make_scatter(df, "Shots", "Shots_Against", "Shots vs Shots Against"))

with col2:
    st.subheader("xG vs xGA")
    st.pyplot(make_scatter(df, "xG", "xGA", "xG vs xGA"))

with col3:
    st.subheader("Goals vs Goals Against")
    st.pyplot(make_scatter(df, "Goals", "Goals_Against", "Goals Scored vs Goals Conceded"))
