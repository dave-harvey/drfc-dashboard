import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from adjustText import adjust_text

st.set_page_config(page_title="Football Analytics Dashboard", layout="wide")

st.title("Football Analytics Dashboard")
st.write("Scatter plots for Shots, xG, and Goals data.")


# --------------------------
# Load the three datasets
# --------------------------
df_shots = pd.DataFrame({
    "Team": [
        "AFC Wimbledon","Barnsley","Blackpool","Bolton Wanderers","Bradford City",
        "Burton Albion","Cardiff City","Doncaster Rovers","Exeter City","Huddersfield Town",
        "Leyton Orient","Lincoln City","Luton Town","Mansfield Town","Northampton Town",
        "Peterborough United","Plymouth Argyle","Port Vale","Reading","Rotherham United",
        "Stevenage","Stockport County","Wigan Athletic","Wycombe Wanderers"
    ],
    "Shots": [
        9.17,11.06,9.28,15.11,11.83,11.06,12.89,10.95,8.67,12.32,
        11.37,9.47,11.00,9.50,7.61,9.83,9.79,11.89,11.94,7.83,
        8.18,11.17,9.78,12.00
    ],
    "Shots_Against": [
        11.28,11.00,13.67,7.28,11.89,12.00,12.72,9.63,11.11,9.58,
        9.74,11.32,8.11,11.11,11.17,11.56,11.79,9.33,10.89,10.67,
        9.00,10.00,10.44,8.89
    ]
})

df_xg = pd.DataFrame({
    "Team": df_shots["Team"],
    "xG": [
        1.16,1.34,0.94,1.53,1.63,1.32,1.45,1.29,1.06,1.41,
        1.36,1.20,1.36,1.15,1.06,1.18,1.05,1.46,1.20,0.87,
        0.91,1.30,1.45,1.55
    ],
    "xGA": [
        1.50,1.50,1.73,0.96,1.21,1.43,1.29,1.19,1.34,1.15,
        1.38,1.16,1.10,1.52,1.13,1.27,1.60,0.98,1.22,1.48,
        0.96,1.09,1.15,0.94
    ]
})

df_goals = pd.DataFrame({
    "Team": df_shots["Team"],
    "Goals": [
        1.28,1.69,0.94,1.39,1.44,0.89,1.78,0.89,0.94,1.63,
        1.58,1.37,1.16,1.28,0.94,1.17,1.05,0.61,1.17,1.11,
        1.12,1.39,1.17,1.37
    ],
    "Goals_Against": [
        1.44,1.38,1.56,0.89,1.00,1.33,0.94,1.37,1.00,1.53,
        1.58,1.00,1.21,1.33,1.00,1.44,1.68,1.17,1.22,1.11,
        0.71,1.17,1.11,1.11
    ]
})

# Merge datasets
df = df_shots.merge(df_xg, on="Team").merge(df_goals, on="Team")


# --------------------------
# Select team to highlight
# --------------------------
team_to_highlight = st.sidebar.selectbox("Highlight a team", df["Team"].unique())


# --------------------------
# Reusable plotting function
# --------------------------
def make_scatter(df, x, y, title):
    fig, ax = plt.subplots(figsize=(8, 6))

    df["_color"] = df["Team"].eq(team_to_highlight).map({True: "crimson", False: "royalblue"})
    df["_size"] = df["Team"].eq(team_to_highlight).map({True: 120, False: 50})

    sns.scatterplot(
        data=df,
        x=x, y=y,
        hue="_color",
        palette=["royalblue", "crimson"],
        size="_size",
        sizes=(50, 120),
        legend=False,
        ax=ax,
        edgecolor="black",
        linewidth=0.6
    )

    # Labels
    texts = []
    for _, row in df.iterrows():
        texts.append(ax.text(row[x], row[y], row["Team"], fontsize=8))

    adjust_text(texts, ax=ax, arrowprops=dict(arrowstyle="-", lw=0.5, color="gray"))

    # Mean lines
    ax.axvline(df[x].mean(), ls="--", color="gray", lw=1)
    ax.axhline(df[y].mean(), ls="--", color="gray", lw=1)

    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_title(title)

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
    st.pyplot(make_scatter(df, "Goals", "Goals_Against", "Goals vs Goals Against"))
