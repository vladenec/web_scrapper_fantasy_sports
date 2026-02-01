# Web Table Scraper

Простой проект для скрейпинга таблиц со веб-страниц и преобразования их в pandas DataFrame.

## Описание

Проект позволяет:
- Загружать веб-страницы по URL
- Извлекать таблицы из HTML
- Преобразовывать таблицы в pandas DataFrame
- Очищать и преобразовывать данные
- Сохранять результаты в CSV/Excel

## Структура проекта

```
web_scraper/
├── src/
│   ├── __init__.py          # Инициализация пакета
│   ├── scraper.py           # Основной класс TableScraper
│   └── utils.py             # Вспомогательные функции
├── tests/
│   ├── __init__.py
│   └── test_scraper.py      # Юнит-тесты
├── requirements.txt         # Зависимости
├── main.py                  # Пример использования
└── README.md                # Этот файл
```

## Установка

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Использование

### Базовый пример

```python
from src.scraper import TableScraper

# Инициализация скрейпера
scraper = TableScraper()

# Загрузка первой таблицы со страницы
df = scraper.extract_first_table("https://example.com/table")

# Вывод результата
print(df)
```

### Извлечение всех таблиц

```python
# Получить все таблицы со страницы
all_tables = scraper.extract_all_tables("https://example.com/table")

for i, table in enumerate(all_tables):
    print(f"Таблица {i}:")
    print(table)
```

### Извлечение таблицы по ID

```python
# Получить таблицу по ID
df = scraper.extract_table_by_id("https://example.com/table", "my-table")
```

### Очистка и сохранение данных

```python
from src.utils import clean_dataframe, save_to_csv

# Очистить DataFrame
df_clean = clean_dataframe(df)

# Сохранить в CSV
save_to_csv(df_clean, "output.csv")
```

## API

### TableScraper

#### Методы:

- `extract_first_table(url)` - Извлечь первую таблицу со страницы
- `extract_all_tables(url)` - Извлечь все таблицы со страницы
- `extract_table_by_index(url, index)` - Извлечь таблицу по индексу
- `extract_table_by_id(url, table_id)` - Извлечь таблицу по ID атрибута

### Utils

- `clean_dataframe(df)` - Очистить DataFrame от пустых строк и столбцов
- `convert_dtypes(df, type_mapping)` - Преобразовать типы данных
- `save_to_csv(df, filepath)` - Сохранить в CSV
- `save_to_excel(df, filepath)` - Сохранить в Excel

## Зависимости

- **requests** - Загрузка веб-страниц
- **beautifulsoup4** - Парсинг HTML
- **pandas** - Работа с данными
- **lxml** - Парсер для beautifulsoup

## Примеры

Полный пример использования см. в файле `main.py`

## Запуск тестов

```bash
python -m unittest discover -s tests
```

## Лицензия

MIT
