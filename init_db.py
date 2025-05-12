import sqlite3

conn = sqlite3.connect('faebakery.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,S
        password TEXT NOT NULL
    )
''')

conn.commit()
conn.close()

print("Database initialized.")
