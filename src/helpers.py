import streamlit as st
from datetime import date
from typing import Union


data_date_to_string = st.secrets["DATA_DATE_TO"]

def data_source_caption(
    source: str = "WyScout",
):
    """
    Render a standardised data source caption.

    Args:
        source: Data source name (default: WyScount)
    """
    st.caption(
        f"Analysis reflects matches played up to and including " + data_date_to_string + ". Match statistics used for this analysis were sourced from " + source + " . " +
        f"This website is an independent analytical project and is not affiliated with any clubs, leagues, or data providers."
    )
