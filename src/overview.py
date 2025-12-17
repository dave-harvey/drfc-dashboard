import streamlit as st

def render():
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

