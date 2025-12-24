import streamlit as st
import pandas as pd
from src.plots import scatter_plot
from src.styles import load_css
from src import overview, performance, outcomes, performance_tracker

# Load your base styling
load_css("styles/base.css")


# Set the page configuration
st.set_page_config(page_title="Donny Dashboard", layout="wide")


# ---------------------------
# MENU USING TABS
# ---------------------------
tabs = st.tabs(["Overview", "Performance", "Performance Tracker", "Outcomes"])


with tabs[0]:
    # overview.render(df)  # if you want to pass data
    overview.render()

with tabs[1]:
    # performance.render(df)
    performance.render()

with tabs[2]:
    # performance.render(df)
    performance_tracker.render()

with tabs[3]:
    # outcomes.render(df)
    outcomes.render()

