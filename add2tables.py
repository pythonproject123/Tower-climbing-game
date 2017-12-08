import sqlite3

conn = sqlite3.connect('game.db')

c = conn.cursor()

def addUser(userName,lives = 3,level = 1):
    with conn:
        c.execute("INSERT INTO player VALUES(userName,lives,level) VALUES(?, ?, ?, ?)",
                  (userName,lives,level))


def updatePlayer(userName, lives, level):
    with conn:
        c.execute("""UPDATE player SET lives = ? AND level = ? 
                    WHERE userName = ?""" ,
                    (lives,level,userName))

"""def getPlayer():
    with conn:
        c.execute("SELECT userName, lives, text FROM player WHERE )"""

