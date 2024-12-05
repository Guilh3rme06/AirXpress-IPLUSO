import sqlite3

conn = sqlite3.connect('AIREXPRESS.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
    )
''')
conn.commit()

def userRegist(name, email):
    for i in range(name):
        name = input("Write your name: ")
        age = int(input("Write your age: "))
        weight = float(input("Write your current weight: "))
        height = float(input("Write your current height: "))

    cursor.execute('INSERT INTO users (username, age) VALUES (?, ?)', (name, email))
    conn.commit()
    print(f"User {name} successfully created!")