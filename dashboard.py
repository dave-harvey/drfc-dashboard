import streamlit as st
import pandas as pd
from src.plots import scatter_plot
from src.styles import load_css
from src import overview, performance, outcomes

# Load your base styling
load_css("styles/base.css")


# Set the page configuration
st.set_page_config(page_title="Donny Dashboard", layout="wide")


# ---------------------------
# MENU USING TABS
# ---------------------------
tab_overview, tab_perf, tab_outcomes = st.tabs(["Overview", "Performance", "Outcomes"])


with tab_overview:
    # overview.render(df)  # if you want to pass data
    overview.render()

with tab_perf:
    # performance.render(df)
    performance.render()

with tab_outcomes:
    # outcomes.render(df)
    outcomes.render()

