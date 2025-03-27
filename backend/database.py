import sqlite3

def create_db():
    conn = sqlite3.connect('videos.db')
    # create tables
    conn.close()