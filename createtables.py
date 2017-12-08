import sqlite3

conn = sqlite3.connect('game.db')

c = conn.cursor()

c.execute("""CREATE TABLE player (
            userName text,
            lives integer,
            level integer,
            )""")