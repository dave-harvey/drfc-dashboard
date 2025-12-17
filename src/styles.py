import streamlit as st
from pathlib import Path

def load_css(css_path: str):
    """
    Load a CSS file into the Streamlit app.

    Args:
        css_path (str): Path to the CSS file, relative or absolute.
    """
    css_file = Path(css_path)

    if not css_file.exists():
        raise FileNotFoundError(f"CSS file not found: {css_path}")

    with css_file.open() as f:
        css = f"<style>{f.read()}</style>"
        st.markdown(css, unsafe_allow_html=True)
