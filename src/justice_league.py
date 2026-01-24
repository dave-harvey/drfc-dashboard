from src.helpers import data_source_caption
import streamlit as st
import pandas as pd
from src.bar_chart import bar_chart

# --------------------------
# Load data from JSON file
# --------------------------
@st.cache_data
def load_data():
    df_raw = pd.read_json("data/efl_1_xpts.json")
    df = df_raw.rename(
        columns={
            "team": "Team",
            "xPts": "xPts"
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
                "<h3 style='margin-bottom: 0; text-transform: uppercase;'>Justice League</h3>",
                unsafe_allow_html=True
            )

            st.markdown(
                """
                Coming soon
                """,
                unsafe_allow_html=True
            )
            # Add a bit of vertical space
            st.write("")

            data_source_caption()

            # Add a bit of vertical space
            st.write("")

    secondCols = st.columns(1)

    with secondCols[0]:
        with st.container(border=True):
            st.markdown(
                "<h3 style='margin-bottom: 0; text-transform: uppercase;'>Expected Points League</h3>",
                unsafe_allow_html=True
            )

            # Add a bit of vertical space
            st.write("")

            #
            bar_chart(
                df=df,
                y="Team",
                x="xPts",
                title="League 1 2025/26 - Average xPts per Game",
                value_format="{:.2f}",
                highlight_label=team_to_highlight
            )

