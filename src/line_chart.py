from typing import Optional
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def line_chart(
    df: pd.DataFrame,
    x: str,
    series1: str,
    series2: Optional[str] = None,
    title: str = "",
    series1Label: Optional[str] = None,
    series2Label: Optional[str] = None,
    show_zero_line: bool = False,
):
    required = [x, series1]
    if series2:
        required.append(series2)

    missing = [c for c in required if c not in df.columns]
    if missing:
        raise KeyError(f"Missing columns in dataframe: {missing}")

    plot_df = df.sort_values(by=x)

    fig, ax = plt.subplots(figsize=(10, 4.8))

    ax.plot(
        plot_df[x],
        plot_df[series1],
        linewidth=2,
        label=series1Label or series1,
    )

    if series2:
        ax.plot(
            plot_df[x],
            plot_df[series2],
            linewidth=2,
            label=series2Label or series2,
        )

    if show_zero_line:
        ax.axhline(0, linestyle="--", linewidth=1, alpha=0.6)

    if title:
        ax.set_title(title, pad=12)

    ax.grid(True, axis="y", linewidth=0.6, alpha=0.35)
    ax.grid(False, axis="x")

    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)

    if series1Label:
        ax.legend(frameon=False, loc="best")
    ax.set_xlabel("")

    # ✅ Force integer ticks on x-axis (e.g. match numbers)
    ax.xaxis.set_major_locator(MultipleLocator(1))

    fig.tight_layout()
    st.pyplot(fig, width="content")
