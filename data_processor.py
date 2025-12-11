import pandas as pd
import cv2
import numpy as np


def add_foto_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Добавляет столбик width для каждого файла.
    """
    df["width"] = 0

    for i, path in enumerate(df["absolute_path"]):
        try:
            img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), cv2.IMREAD_COLOR)
            width = img.shape[1]
            df.loc[i, "width"] = width
        except Exception as e:
            raise Exception(f"Ошибка при чтении {path}: {e}")

    return df


def filter_by_foto(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    """
    Фильтрует DataFrame по width > threshold (порог).
    """
    filtered_df = df[df["width"] > threshold].reset_index(drop=True)
    filtered_df.index += 1
    return filtered_df


def sort_by_foto(df: pd.DataFrame, ascending: bool = True) -> pd.DataFrame:
    """
    Сортирует DataFrame по width.
    """
    sorted_df = df.sort_values("width", ascending=ascending).reset_index(drop=True)
    sorted_df.index += 1
    return sorted_df
