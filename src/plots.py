import pandas as pd
from typing import Optional, Tuple
import plotly.express as px

# Global style
sns.set_theme(context="talk", style="white", font_scale=0.4)

def scatter_with_labels(
    df: pd.DataFrame,
    x: str,
    y: str,
    title: str,
    xLabel: Optional[str] = None,
    yLabel: Optional[str] = None,
    highlight_team: Optional[str] = None,
    figsize: Tuple[int, int] = (8, 6),
):
    """
    Generic scatter plot with labelled points and optional highlighting,
    implemented using Plotly.

    Parameters
    ----------
    df : DataFrame
        Must contain columns 'Team', x, y (plus any other metrics you want in hover).
    x : str
        Column for x-axis.
    y : str
        Column for y-axis.
    title : str
        Chart title.
    xLabel : str, optional
        Friendly label for x-axis (defaults to the column name).
    yLabel : str, optional
        Friendly label for y-axis (defaults to the column name).
    highlight_team : str, optional
        Team name to highlight (different colour and larger marker).
    figsize : (int, int)
        Logical figure size; used to derive Plotly width/height in pixels.
    """

    df_plot = df.copy()

    # Highlight logic: colour + size
    if highlight_team:
        df_plot["_highlight"] = df_plot["Team"].eq(highlight_team)
        df_plot["_group"] = df_plot["_highlight"].map(
            {True: "Highlight", False: "Other"}
        )
        df_plot["_size"] = df_plot["_highlight"].map(
            {True: 18, False: 10}   # highlight bigger marker
        )
        color_col = "_group"
        color_map = {"Other": "#4169E1", "Highlight": "#DC143C"}  # royalblue / crimson
    else:
        df_plot["_group"] = "Other"
        df_plot["_size"] = 10
        color_col = None
        color_map = None

    # Decide what to show in hover (everything except internal columns)
    hover_exclude = {"_highlight", "_group", "_size"}
    hover_cols = [c for c in df_plot.columns if c not in hover_exclude]

    # Convert figsize (inches-ish) to pixels for Plotly
    width = int(figsize[0] * 100)
    height = int(figsize[1] * 100)

    fig = px.scatter(
        df_plot,
        x=x,
        y=y,
        color=color_col,
        color_discrete_map=color_map,
        size="_size",
        size_max=18,
        hover_name="Team",        # big name at top of hover
        hover_data=hover_cols,    # show underlying stats
        text="Team",              # label points with team name
    )

    # Axis titles and general layout
    fig.update_layout(
        title=title,
        xaxis_title=xLabel if xLabel else x,
        yaxis_title=yLabel if yLabel else y,
        showlegend=False,
        width=width,
        height=height,
        margin=dict(l=40, r=20, t=60, b=40),
    )

    # Position + style for text labels on the plot
    fig.update_traces(
        textposition="top center",
        textfont=dict(size=9),
        marker=dict(line=dict(width=0.5, color="black")),
    )

    # Quadrant mean lines
    x_mean = df_plot[x].mean()
    y_mean = df_plot[y].mean()
    fig.add_vline(x=x_mean, line_dash="dash", line_width=1, line_color="grey")
    fig.add_hline(y=y_mean, line_dash="dash", line_width=1, line_color="grey")

    # Tidy axes (thin border, no grid)
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
