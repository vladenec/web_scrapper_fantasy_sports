"""Пример использования TableScraper"""

from src.scraper import TableScraper
from src.utils import clean_dataframe, save_to_csv


def main():
    """Главная функция"""
    
    # Инициализация скрейпера
    scraper = TableScraper()
    
    # Пример 1: Извлечение первой таблицы
    url = "https://fantasy-h2h.ru/analytics/fantasy_team_players/seria_a_2025"  # Замени на реальный URL
    
    print("Загрузка таблицы...")
    df = scraper.extract_first_table(url)
    
    if df is not None:
        print(f"Таблица загружена успешно!")
        print(f"Размер: {df.shape}")
        print(f"\nПервые строки:")
        print(df.head())
        
        # Очистка данных
        df_clean = clean_dataframe(df)
        
        # Сохранение в CSV
        save_to_csv(df_clean, r"C:/Users/baske/vlad_scripts/web_scraper/output.csv")
    else:
        print("Не удалось загрузить таблицу")
    
    # Пример 2: Извлечение всех таблиц со страницы
    # all_tables = scraper.extract_all_tables(url)
    # for i, table in enumerate(all_tables):
    #     print(f"Таблица {i}: {table.shape}")
    
    # Пример 3: Извлечение таблицы по ID
    # df_by_id = scraper.extract_table_by_id(url, "table-id")


if __name__ == "__main__":
    main()
