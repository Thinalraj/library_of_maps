import sqlite3

conn = sqlite3.connect('estate.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS estates (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
''')

# Initial data
estates = [
    (1, 'Diamond Jubilee Estate'),
    (2, 'East Estate')
]

cursor.executemany('INSERT OR IGNORE INTO estates (id, name) VALUES (?, ?)', estates)

conn.commit()
conn.close()

print("Database initialized and estates added.")
