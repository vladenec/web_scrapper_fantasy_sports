"""Вспомогательные функции"""

import pandas as pd
from typing import Optional


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Очистить DataFrame от пустых строк и столбцов
    
    Args:
        df: Исходный DataFrame
        
    Returns:
        Очищенный DataFrame
    """
    # Удалить полностью пустые строки
    df = df.dropna(how='all')
    
    # Удалить полностью пустые столбцы
    df = df.dropna(axis=1, how='all')
    
    return df


def convert_dtypes(df: pd.DataFrame, type_mapping: Optional[dict] = None) -> pd.DataFrame:
    """
    Преобразовать типы данных в DataFrame
    
    Args:
        df: Исходный DataFrame
        type_mapping: Словарь для преобразования типов {колонка: тип}
        
    Returns:
        DataFrame с преобразованными типами
    """
    if type_mapping:
        for col, dtype in type_mapping.items():
            if col in df.columns:
                try:
                    df[col] = df[col].astype(dtype)
                except ValueError as e:
                    print(f"Ошибка при преобразовании колонки '{col}': {e}")
    
    return df


def save_to_csv(df: pd.DataFrame, filepath: str, **kwargs) -> None:
    """
    Сохранить DataFrame в CSV
    
    Args:
        df: DataFrame для сохранения
        filepath: Путь до файла
        **kwargs: Дополнительные параметры для to_csv
    """
    df.to_csv(filepath, index=False, **kwargs)
    print(f"DataFrame сохранен в {filepath}")


def save_to_excel(df: pd.DataFrame, filepath: str, **kwargs) -> None:
    """
    Сохранить DataFrame в Excel
    
    Args:
        df: DataFrame для сохранения
        filepath: Путь до файла
        **kwargs: Дополнительные параметры для to_excel
    """
    df.to_excel(filepath, index=False, **kwargs)
    print(f"DataFrame сохранен в {filepath}")
