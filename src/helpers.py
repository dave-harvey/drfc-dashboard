import streamlit as st
from datetime import date
from typing import Union


def data_source_caption(
    source: str = "WyScout",
):
    """
    Render a standardised data source caption.

    Args:
        source: Data source name (default: WyScount)
    """
    st.caption(
        f"Analysis reflects matches played up to and including 17 Feb 2026. Match statistics used for this analysis were sourced from {source}."
    )
