# Импорт библиотеки
import sqlite3

# Подключение к БД
con = sqlite3.connect(input())

# Создание курсора
cur = con.cursor()

# Выполнение запроса и получение всех результатов
res = cur.execute("""SELECT title FROM Films 
            WHERE 1995 <= year < 2000 AND genre=(
        SELECT id FROM genres
            WHERE title = 'детектив')""").fetchall()

for elem in res:
    print(elem)

con.close()
