import sqlite3

"""Если база ещё не поднята запустить скрипт"""


def create_db():
    conn = sqlite3.connect('sqlite_python.db')
    query_create_table = '''
    create virtual table movie
     USING FTS5 (rating,name,release_date,director)
    '''
    cur = conn.cursor()
    cur.execute(query_create_table)
    conn.commit()


create_db()
