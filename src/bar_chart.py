from __future__ import annotations

from typing import Optional

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


def bar_chart(
    df: pd.DataFrame,
    y: str,
    x: str,
    title: str = "",
    xLabel: Optional[str] = None,
    yLabel: Optional[str] = None,
    value_format: str = "{:.2f}",
    top_n: Optional[int] = None,
    highlight_label: Optional[str] = None,
    base_color: str = "#4169E1",        # default bar color (close to your example)
    highlight_color: str = "#DC143C",   # default highlight (Doncaster red)
):
    """
    Generic horizontal bar chart, sorted highest to lowest, rendered in Streamlit.

    Args:
        df: Input dataframe.
        y: Column name for the y-axis categories (e.g. team names).
        x: Column name for the x-axis values (e.g. xPts/Game).
        title: Chart title.
        xLabel: Optional x-axis label.
        yLabel: Optional y-axis label.
        value_format: Format string for value labels.
        top_n: Optionally display only the top N rows.
        highlight_label: Optional y-value to highlight (e.g. "Doncaster Rovers").
        base_color: Default color for all bars.
        highlight_color: Color used for the highlighted bar.
    """
    # --- Validation ---
    required = [y, x]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise KeyError(f"Missing columns in dataframe: {missing}")

    plot_df = df[[y, x]].copy()
    plot_df[x] = pd.to_numeric(plot_df[x], errors="coerce")
    plot_df = plot_df.dropna(subset=[x])

    # Sort highest → lowest
    plot_df = plot_df.sort_values(by=x, ascending=False)

    # Optional top N
    if top_n is not None:
        plot_df = plot_df.head(top_n)

    # --- Figure size scales with number of bars ---
    n = len(plot_df)
    fig_h = max(6, 0.35 * n)
    fig, ax = plt.subplots(figsize=(10, fig_h))

    # ✅ Valid per-bar color list (no None values)
    colors = [base_color] * len(plot_df)
    if highlight_label is not None:
        for i, team in enumerate(plot_df[y].astype(str).values):
            if team == str(highlight_label):
                colors[i] = highlight_color

    # Plot
    ax.barh(plot_df[y], plot_df[x], color=colors)
    ax.invert_yaxis()  # highest at top

    # Title / labels
    if title:
        ax.set_title(title, pad=12)
    ax.set_xlabel(xLabel or "")
    ax.set_ylabel(yLabel or "")

    # Grid and spines
    ax.grid(True, axis="x", linewidth=0.6, alpha=0.35)
    ax.grid(False, axis="y")

    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)

    # Value labels
    max_val = plot_df[x].max() if len(plot_df) else 0
    for i, (team, val) in enumerate(zip(plot_df[y].astype(str).values, plot_df[x].values)):
        if pd.isna(val):
            continue

        label = value_format.format(val)
        inside = max_val > 0 and val > 0.15 * max_val
        is_highlight = highlight_label is not None and team == str(highlight_label)

        # slightly bolder label for highlighted team
        label_weight = "bold" if is_highlight else "normal"

        if inside:
            ax.text(
                val - (0.03 * max_val),
                i,
                label,
                va="center",
                ha="right",
                fontsize=9,
                fontweight=label_weight,
                color="white",
            )
        else:
            ax.text(
                val + (0.01 * max_val),
                i,
                label,
                va="center",
                ha="left",
                fontsize=9,
                fontweight=label_weight,
            )

    fig.tight_layout()
    st.pyplot(fig, width="content")
