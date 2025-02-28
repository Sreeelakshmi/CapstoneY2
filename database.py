import sqlite3
import os

DB_PATH = "Dataset and Database/scores.db"

def init_db():
    # Create the folder if it doesn't exist
    folder = os.path.dirname(DB_PATH)
    if not os.path.exists(folder):
        os.makedirs(folder)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS scores (id INTEGER PRIMARY KEY, points INTEGER)''')
    conn.commit()
    conn.close()

def save_score(points):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO scores (points) VALUES (?)", (points,))
    conn.commit()
    conn.close()

def get_high_score():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT MAX(points) FROM scores")
    result = c.fetchone()[0]
    conn.close()
    return result if result else 0
