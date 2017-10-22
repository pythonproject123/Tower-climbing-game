import sqlite3

conn = sqlite3.connect('game.db')

c = conn.cursor()

def addUser(userName,lives = 0,level = 0, currentScore = 0):
    with conn:
        c.execute("INSERT INTO player VALUES(?, ?, ?, ?)",(userName,lives,level,currentScore))

def addScore(userName,score):
    with conn:
        c.execute("INSERT INTO player totalScores(?, ?)",(userName,score))

def updateScore(userName, lives, score):
    with conn:
        c.execute("""UPDATE player SET lives = ? AND currentScore = ?
                    WHERE userName = ?""" ,
                    (lives,score,userName))

def addFirstLevel(userName,score):
    with conn:
        c.execute("INSERT INTO firstLevel(?, ?)",(userName,score))

def addSecondLevel(userName,score):
    with conn:
        c.execute("INSERT INTO secondLevel(?, ?)",(userName,score))

def addThirdLevel(userName,score):
    with conn:
        c.execute("INSERT INTO thirdLevel(?, ?)",(userName,score))
