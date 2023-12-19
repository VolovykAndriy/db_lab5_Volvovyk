import csv
import psycopg2
from psycopg2 import sql

# З'єднання з базою даних PostgreSQL
username = 'AAVOLOVYK'
password = '111'
database = 'lab6'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

# Створення курсора
cur = conn.cursor()

# Шлях до CSV-файлу
csv_file_path = "vgsales.csv"

clear_query = '''
DELETE FROM Platform_has_game;
DELETE FROM global_sales;
DELETE FROM game;
DELETE FROM platform;
DELETE FROM publisher;
'''

cur.execute(clear_query)

# Відкриття CSV-файлу та імпорт даних в кожну таблицю
with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Пропустити заголовок CSV-файлу
    for row in csv_reader:
        # Вибірка даних зі строки для подальшої вставки
        rank, name, platform, year, genre, publisher, na_sales, eu_sales, jp_sales, other_sales, global_sales = row
        list_listov = [[].append(rank), [].append(name), [].append(platform), [].append(year), [].append(genre), [].append(publisher), [].append(global_sales)]
        # Вставка даних в таблицю Platform
        cur.execute("INSERT INTO Platform (platform_id, Platform_Name) VALUES (%s, %s) ON CONFLICT (platform_id) DO NOTHING",
                    (rank, platform))

        # Вставка даних в таблицю Publisher
        cur.execute("INSERT INTO Publisher (publisher_id, Publisher_Name) VALUES (%s, %s) ON CONFLICT (publisher_id) DO NOTHING",
                    (rank, publisher))

        # Вставка даних в таблицю Game
        cur.execute("INSERT INTO Game (game_id, Name, Year, Genre, platform_id, publisher_id) VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (game_id) DO NOTHING",
                    (rank, name, year, genre, rank, rank))

        # Вставка даних в таблицю global_sales
        cur.execute("INSERT INTO global_sales (gs_id, game_id, sales, year_of_update) VALUES (%s, %s, %s, %s) ON CONFLICT (gs_id) DO NOTHING",
                    (rank, rank, float(global_sales.replace(';', '')), year))

        # Вставка даних в таблицю Platform_has_game
        cur.execute("INSERT INTO Platform_has_game (game_id, platform_id) VALUES (%s, %s) ON CONFLICT (game_id, platform_id) DO NOTHING",
                    (rank, rank))
        if rank == '5000':
            break

# Збереження змін та закриття курсора та з'єднання
conn.commit()
cur.close()
conn.close()

