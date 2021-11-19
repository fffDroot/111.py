import sqlite3

con = sqlite3.connect(input())
cur = con.cursor()
res = cur.execute("""SELECT DISTINCT title FROM genres WHERE id 
IN (SELECT genre FROM films WHERE year > 2009 AND year < 2012)""").fetchall()

for elem in res:
    print(elem[0])

con.close()
