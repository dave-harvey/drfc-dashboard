import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from adjustText import adjust_text
from typing import Optional, Tuple

# Global style
sns.set_theme(context="talk", style="white", font_scale=0.7)

def scatter_with_labels(
    df: pd.DataFrame,
    x: str,
    y: str,
    title: str,
    xLabel: Optional[str] = None,
    yLabel: Optional[str] = None,
    highlight_team: Optional[str] = None,
    figsize: Tuple[int, int] = (8, 6),
) -> plt.Figure:
    """
    Generic scatter plot with labelled points and optional highlighting.

    Parameters
    ----------
    df : DataFrame
        Must contain columns 'Team', x, y
    x : str
        Column for x-axis
    y : str
        Column for y-axis
    title : str
        Chart title
    xLabel : str, optional
        Friendly label for x-axis (defaults to the column name)
    yLabel : str, optional
        Friendly label for y-axis (defaults to the column name)
    highlight_team : str, optional
        Team name to highlight
    figsize : tuple
        Matplotlib figure size

    Returns
    -------
    matplotlib.figure.Figure
    """

    df_plot = df.copy()

    # Handle highlight or fallback to uniform styling
    if highlight_team:
        df_plot["_color"] = df_plot["Team"].eq(highlight_team).map(
            {True: "crimson", False: "royalblue"}
        )
        df_plot["_size"] = df_plot["Team"].eq(highlight_team).map(
            {True: 120, False: 50}
        )
    else:
        df_plot["_color"] = "royalblue"
        df_plot["_size"] = 50

    fig, ax = plt.subplots(figsize=figsize)

    sns.scatterplot(
        data=df_plot,
        x=x,
        y=y,
        hue="_color" if highlight_team else None,
        palette=["royalblue", "crimson"] if highlight_team else None,
        size="_size",
        sizes=(50, 120),
        legend=False,
        edgecolor="black",
        linewidth=0.6,
        ax=ax,
    )

    # Labels for each team
    texts = []
    for _, row in df_plot.iterrows():
        texts.append(
            ax.text(
                row[x],
                row[y],
                row["Team"],
                fontsize=8,
            )
        )

    adjust_text(
        texts,
        ax=ax,
        arrowprops=dict(arrowstyle="-", lw=0.5, color="gray", alpha=0.8),
    )

    # Mean reference lines
    ax.axvline(df_plot[x].mean(), ls="--", color="gray", lw=1)
    ax.axhline(df_plot[y].mean(), ls="--", color="gray", lw=1)

    # Friendly axis labels (fallback to raw names)
    ax.set_xlabel(xLabel if xLabel else x)
    ax.set_ylabel(yLabel if yLabel else y)

    ax.set_title(title)
    ax.grid(False)

    plt.tight_layout()
    return fig
