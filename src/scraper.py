"""Основной модуль для скрейпинга таблиц"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from typing import List, Optional, Union


class TableScraper:
    """Класс для извлечения таблиц со веб-страниц"""
    
    def __init__(self, timeout: int = 10, headers: Optional[dict] = None):
        """
        Инициализация скрейпера
        
        Args:
            timeout: Таймаут для запросов (секунды)
            headers: Кастомные HTTP заголовки
        """
        self.timeout = timeout
        self.headers = headers or {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def fetch_page(self, url: str) -> Optional[BeautifulSoup]:
        """
        Загрузить страницу по URL
        
        Args:
            url: URL страницы
            
        Returns:
            BeautifulSoup объект или None если ошибка
        """
        try:
            response = requests.get(url, timeout=self.timeout, headers=self.headers)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'lxml')
        except requests.RequestException as e:
            print(f"Ошибка при загрузке страницы: {e}")
            return None
    
    def extract_all_tables(self, url: str) -> List[pd.DataFrame]:
        """
        Извлечь все таблицы со страницы
        
        Args:
            url: URL страницы
            
        Returns:
            Список DataFrame объектов
        """
        soup = self.fetch_page(url)
        if not soup:
            return []
        
        tables = soup.find_all('table')
        dataframes = []
        
        for table in tables:
            try:
                df = pd.read_html(str(table))[0]
                dataframes.append(df)
            except Exception as e:
                print(f"Ошибка при парсинге таблицы: {e}")
                continue
        
        return dataframes
    
    def extract_first_table(self, url: str) -> Optional[pd.DataFrame]:
        """
        Извлечь первую таблицу со страницы
        
        Args:
            url: URL страницы
            
        Returns:
            DataFrame или None
        """
        tables = self.extract_all_tables(url)
        return tables[0] if tables else None
    
    def extract_table_by_index(self, url: str, index: int = 0) -> Optional[pd.DataFrame]:
        """
        Извлечь таблицу по индексу
        
        Args:
            url: URL страницы
            index: Индекс таблицы (начиная с 0)
            
        Returns:
            DataFrame или None
        """
        tables = self.extract_all_tables(url)
        if index >= len(tables):
            print(f"Таблица с индексом {index} не найдена")
            return None
        return tables[index]
    
    def extract_table_by_id(self, url: str, table_id: str) -> Optional[pd.DataFrame]:
        """
        Извлечь таблицу по ID
        
        Args:
            url: URL страницы
            table_id: ID таблицы в HTML
            
        Returns:
            DataFrame или None
        """
        soup = self.fetch_page(url)
        if not soup:
            return None
        
        table = soup.find('table', {'id': table_id})
        if not table:
            print(f"Таблица с ID '{table_id}' не найдена")
            return None
        
        try:
            df = pd.read_html(str(table))[0]
            return df
        except Exception as e:
            print(f"Ошибка при парсинге таблицы: {e}")
            return None
