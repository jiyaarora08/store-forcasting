import matplotlib.pyplot as plt
import os

# Constant Colors
COLORS = [
    "#66C2A5",
    "#FC8D62",
    "#8DA0CB",
    "#E78AC3",
    "#A6D854",
    "#FFD92F",
]


def set_labels(title, xlabel, ylabel="Frequency"):
    """Set title, xlabel, and ylabel for a matplotlib plot."""
    title = title.title()
    xlabel = xlabel.title()
    fontdict = {"fontsize": 12, "fontweight": "bold"}
    plt.title(title, fontdict=fontdict)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)



def highlight_max_bar(ax):
    """Highlight the highest bar in a barplot."""
    max_val = max(bar.get_height() for bar in ax.patches)
    for bar in ax.patches:
        if bar.get_height() == max_val:
            bar.set_color("red")


def save_fig(fig, output_path):
    """Save and close a matplotlib figure."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)