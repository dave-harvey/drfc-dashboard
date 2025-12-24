from typing import Optional
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def line_chart(
    df: pd.DataFrame,
    x: str,
    series1: str,
    series2: Optional[str] = None,
    title: str = "",
    series1Label: str = "",
    series2Label: Optional[str] = None,
    show_zero_line: bool = False,
):
    """
    Create a Matplotlib line chart from one or two dataframe series.

    Assumes all metrics (e.g. rolling averages) are already present in df.
    """
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

    ax.legend(frameon=False, loc="best")
    ax.set_xlabel("")

    fig.tight_layout()
    st.pyplot(fig, use_container_width=True)
