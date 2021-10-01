import sqlite3
pas=sqlite3.connect('Pass.db')
cur=pas.cursor()

def create():
    query='CREATE TABLE Pass_Word(ACC_NAME TEXT NOT NULL,PASSWORD TEXT NOT NULL);'
    cur.execute(query)
