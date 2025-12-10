import matplotlib.pyplot as plt
import pandas as pd


def plot_bild(df: pd.DataFrame, output_plot: str) -> None:
    """
    Выводит график отсортированных данных
    """
    _, ax = plt.subplots(figsize=(12, 6))

    ax.plot(
        df.index,
        df["widht"],
        marker="o",
        linestyle="-",
        linewidth=2,
        color="blue",
    )

    ax.set_xlabel("Номер картинки", fontsize=12, fontweight="bold")
    ax.set_ylabel("Ширина", fontsize=12, fontweight="bold")
    ax.set_title("График отсортированного датафрейма", fontsize=14, fontweight="bold")
    ax.grid(True, alpha=0.3)

    ax.set_xticks(df.index)
    ax.set_yticks(df["widht"].values)

    plt.tight_layout()
    plt.savefig(output_plot, dpi=300, bbox_inches="tight")
    print(f"График сохранён в {output_plot}")
    plt.show()
