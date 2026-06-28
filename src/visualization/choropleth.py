

import matplotlib.pyplot as plt

def plot_property_score_map(gdf):

    fig, ax = plt.subplots(1, 1, figsize=(12, 8))

    gdf.plot(
        column="property_score",
        cmap="YlOrRd",
        legend=True,
        ax=ax
    )

    ax.set_title("Ontario Property Intelligence Score Map", fontsize=14)
    ax.axis("off")

    plt.show()