# src/plots.py

from typing import Optional, Tuple, List

import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io as pio
import matplotlib.pyplot as plt
from adjustText import adjust_text

# Optional: nice clean default for Plotly
pio.templates.default = "plotly_white"


def _scatter_plotly(
    df: pd.DataFrame,
    x: str,
    y: str,
    title: str,
    xLabel: Optional[str],
    yLabel: Optional[str],
    highlight_team: Optional[str],
    height: int = 600,
):
    df_plot = df.copy()

    # Highlight logic
    if highlight_team:
        df_plot["_highlight"] = df_plot["Team"].eq(highlight_team)
        df_plot["_group"] = df_plot["_highlight"].map(
            {True: "Highlight", False: "Other"}
        )
        df_plot["_size"] = df_plot["_highlight"].map(
            {True: 12, False: 6}   # tweak sizes here
        )
        color_col = "_group"
        color_map = {"Other": "#4169E1", "Highlight": "#DC143C"}
    else:
        df_plot["_group"] = "Other"
        df_plot["_size"] = 6
        color_col = None
        color_map = None

    # Hover: show all useful columns except internals
    hover_exclude = {"_highlight", "_group", "_size"}
    hover_cols: List[str] = [c for c in df_plot.columns if c not in hover_exclude]

    fig = px.scatter(
        df_plot,
        x=x,
        y=y,
        color=color_col,
        color_discrete_map=color_map,
        size="_size",
        size_max=12,
        hover_name="Team",
        hover_data=hover_cols,
        text="Team",        # labels on points
    )

    # Layout
    fig.update_layout(
        title=title,
        xaxis_title=xLabel if xLabel else x,
        yaxis_title=yLabel if yLabel else y,
        showlegend=False,
        height=height,
        margin=dict(l=40, r=20, t=60, b=40),
    )

    # Label styling & marker outline
    fig.update_traces(
        textposition="top center",
        textfont=dict(size=9),
        marker=dict(line=dict(width=0.5, color="black")),
    )

    # Quadrant lines
    x_mean = df_plot[x].mean()
    y_mean = df_plot[y].mean()
    fig.add_vline(x=x_mean, line_dash="dash", line_width=1, line_color="grey")
    fig.add_hline(y=y_mean, line_dash="dash", line_width=1, line_color="grey")

    # Axes style
    fig.update_xaxes(
        showgrid=False,
        zeroline=False,
        showline=True,
        linewidth=0.5,
        linecolor="black",
    )
    fig.update_yaxes(
        showgrid=False,
        zeroline=False,
        showline=True,
        linewidth=0.5,
        linecolor="black",
    )

    return fig


def _scatter_matplotlib(
    df: pd.DataFrame,
    x: str,
    y: str,
    title: str,
    xLabel: Optional[str],
    yLabel: Optional[str],
    highlight_team: Optional[str],
    figsize: Tuple[int, int] = (6, 6),
):
    fig, ax = plt.subplots(figsize=figsize)

    # Base points
    ax.scatter(df[x], df[y], color="royalblue", s=30, alpha=0.8, zorder=2)

    # Highlighted team
    if highlight_team:
        h = df[df["Team"] == highlight_team]
        ax.scatter(h[x], h[y], color="crimson", s=80, zorder=3)

    # Labels with adjustText
    texts = []
    for _, row in df.iterrows():
        colour = "crimson" if row["Team"] == highlight_team else "black"
        texts.append(
            ax.text(
                row[x],
                row[y],
                row["Team"],
                fontsize=7,
                color=colour,
            )
        )

    adjust_text(
        texts,
        ax=ax,
        arrowprops=dict(arrowstyle="-", color="grey", lw=0.5),
    )

    # Quadrant lines
    ax.axvline(df[x].mean(), linestyle="--", linewidth=0.7, color="grey")
    ax.axhline(df[y].mean(), linestyle="--", linewidth=0.7, color="grey")

    ax.set_title(title, fontsize=12)
    ax.set_xlabel(xLabel or x, fontsize=10)
    ax.set_ylabel(yLabel or y, fontsize=10)
    ax.tick_params(axis="both", labelsize=8)

    ax.grid(False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    for spine in ax.spines.values():
        spine.set_linewidth(0.4)

    plt.tight_layout()
    return fig


def scatter_plot(
    df: pd.DataFrame,
    x: str,
    y: str,
    title: str,
    xLabel: Optional[str] = None,
    yLabel: Optional[str] = None,
    highlight_team: Optional[str] = None,
    figsize: Tuple[int, int] = (6, 6),
    interactive_default: bool = True,
    key: Optional[str] = None,
    use_container_width: bool = True,
):
    """
    Renders a scatter plot in Streamlit using either Plotly (interactive)
    or Matplotlib (static), selected via a radio button.

    This function handles:
    - the Streamlit radio widget
    - generating the appropriate figure
    - rendering it in the app
    """
    options = ["Interactive", "Static"]
    default_index = 0 if interactive_default else 1


    interactive = st.toggle(
        "Interactive chart",
        value=interactive_default,
        key=key
    )

    if interactive:
        fig = _scatter_plotly(
            df=df,
            x=x,
            y=y,
            title=title,
            xLabel=xLabel,
            yLabel=yLabel,
            highlight_team=highlight_team,
            height=int(figsize[1] * 100),  # simple conversion: inches → px
        )
        st.plotly_chart(fig, use_container_width=use_container_width)
    else:
        fig = _scatter_matplotlib(
            df=df,
            x=x,
            y=y,
            title=title,
            xLabel=xLabel,
            yLabel=yLabel,
            highlight_team=highlight_team,
            figsize=(8, 6),
        )
        st.pyplot(fig, use_container_width=False)