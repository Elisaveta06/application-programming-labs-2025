import argparse
import pandas as pd

from data_processor import add_foto_column, filter_by_foto, sort_by_foto
from utils import get_correct_csv_path
from visualizer import plot_bild


def parser_t() -> tuple[str, str, str, float]:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=str, help="Путь к CSV файлу")
    parser.add_argument("output_plot", type=str, help="Путь для графика")
    parser.add_argument("output_csv", type=str, help="Путь для CSV")
    parser.add_argument("alpha", type=float, help="Число для фильтрации")
    args = parser.parse_args()
    return args.source, args.output_plot, args.output_csv, args.alpha


def main():
    source, output_plot, output_csv, value = parser_t()

    df = pd.read_csv(source)

    df = add_foto_column(df)
    filtered_df = filter_by_foto(df, value)
    sorted_df = sort_by_foto(filtered_df, ascending=True)

    plot_bild(sorted_df, output_plot)

    output_csv = get_correct_csv_path(output_csv)
    sorted_df.to_csv(output_csv, index=False)
    print(f"CSV сохранён в {output_csv}")


if __name__ == "__main__":
    main()
