import sqlite3

def init_db():
conn = sqlite3.connect('history.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS history
(id INTEGER PRIMARY KEY, phone TEXT, amount TEXT, status TEXT)''')
conn.commit()
conn.close()
