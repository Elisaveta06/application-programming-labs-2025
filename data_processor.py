import pandas as pd
import cv2


def add_amplitude_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Добавляет столбик widht для каждого файла
    """
    df["widht"] = 0

    for i, path in enumerate(df["absolute_path"]):
        try:
            img = cv2.imread(path)
            widht = img.shape[1]
            df.loc[i, "widht"] = widht
        except Exception as e:
            print(f"Ошибка при чтении {path}: {e}")

    return df


def filter_by_amplitude(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    """
    Фильтрует DataFrame по widht > threshold
    """
    filtered_df = df[df["widht"] > threshold].reset_index(drop=True)
    filtered_df.index += 1
    return filtered_df


def sort_by_amplitude(df: pd.DataFrame, ascending: bool = True) -> pd.DataFrame:
    """
    Сортирует DataFrame по widht
    """
    sorted_df = df.sort_values("widht", ascending=ascending).reset_index(drop=True)
    sorted_df.index += 1
    return sorted_df
