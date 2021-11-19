import sqlite3


def get_result(name):
    con = sqlite3.connect(name)
    cur = con.cursor()
    cur.execute("""DELETE FROM films WHERE title LIKE 'Я%а'""")
    print('hello')
    con.close()
