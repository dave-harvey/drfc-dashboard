import streamlit as st
import pandas as pd
from src.helpers import data_source_caption
from src.styles import load_css
from src import overview, performance, outcomes, performance_tracker, justice_league

# Load your base styling
load_css("styles/base.css")


# Set the page configuration
st.set_page_config(page_title="Donny Dashboard", layout="wide")


# ---------------------------
# MENU USING TABS
# ---------------------------
tabs = st.tabs(["Overview", "Performance", "Performance Tracker", "Justice League", "Outcomes"])


with tabs[0]:
    overview.render()

with tabs[1]:
    performance.render()

with tabs[2]:
    performance_tracker.render()

with tabs[3]:
    justice_league.render()

with tabs[4]:
    outcomes.render()


st.caption("")
data_source_caption()
