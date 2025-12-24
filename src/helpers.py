import streamlit as st
from datetime import date
from typing import Union


def data_source_caption(
    source: str = "FotMob",
):
    """
    Render a standardised data source caption.

    Args:
        source: Data source name (default: FotMob)
    """
    st.caption(
        f"Data reflects matches played up to and including 21 Dec 2025 (source: {source})."
    )
