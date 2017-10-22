import sqlite3

conn = sqlite3.connect('game.db')

c = conn.cursor()

c.execute("""CREATE TABLE player (
            userName text,
            lives integer,
            level integer,
            currentScore integer
            )""")

c.execute("""CREATE TABLE firstLevel (
            userName text,
            score integer
            )""")

c.execute("""CREATE TABLE secondLevel (
            userName text,
            score integer
            )""")

c.execute("""CREATE TABLE thirdLevel (
            userName text,
            score integer
            )""")

c.execute("""CREATE TABLE totalScores (
            userName text,
            score integer
            )""")

