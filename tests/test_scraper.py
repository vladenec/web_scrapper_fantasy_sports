"""Тесты для модуля TableScraper"""

import unittest
from src.scraper import TableScraper
from src.utils import clean_dataframe
import pandas as pd


class TestTableScraper(unittest.TestCase):
    """Тестовый класс для TableScraper"""
    
    def setUp(self):
        """Подготовка к тестам"""
        self.scraper = TableScraper()
    
    def test_scraper_initialization(self):
        """Тест инициализации скрейпера"""
        self.assertEqual(self.scraper.timeout, 10)
        self.assertIsNotNone(self.scraper.headers)
    
    def test_clean_dataframe(self):
        """Тест очистки DataFrame"""
        df = pd.DataFrame({
            'A': [1, 2, None],
            'B': [None, None, None],
            'C': [4, 5, 6]
        })
        
        df_clean = clean_dataframe(df)
        
        # Проверяем, что пустой столбец удален
        self.assertNotIn('B', df_clean.columns)
        # Проверяем, что оставлись остальные столбцы
        self.assertIn('A', df_clean.columns)
        self.assertIn('C', df_clean.columns)


if __name__ == '__main__':
    unittest.main()
