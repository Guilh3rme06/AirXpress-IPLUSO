import sqlite3

conn = sqlite3.connect('AIRXPRESS.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
    cliente INTEGER PRIMARY KEY AUTOINCREMENT,
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

    def atualizar_cliente(id, novo_nome, novo_email):
        conn = sqlite3.connect('airxpress.db')
        cursor = conn.cursor()

        cursor.execute('UPDATE clientes SET nome = ?, email = ? WHERE id = ?', (novo_nome, novo_email, id))

        conn.commit()
        conn.close()

    def excluir_cliente(id):
        conn = sqlite3.connect('airxpress.db')
        cursor = conn.cursor()

        cursor.execute('DELETE FROM clientes WHERE id = ?', (id,))

        conn.commit()