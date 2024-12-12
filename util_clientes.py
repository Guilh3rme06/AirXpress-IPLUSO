import sqlite3

conn = sqlite3.connect('AIRXPRESS.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients(
    cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE
    )
''')
conn.commit()

def client_regist(name, email):
    for i in range(name):
        name = input("Write your name: ")
        email = int(input("Write your email: "))

    cursor.execute('INSERT INTO clients (username, age) VALUES (?, ?)', (name, email))
    conn.commit()
    print(f"User {name} successfully created!")

# Consultar uma lista de clientes registados
def find_all_clients():
    '''
    Função para encontrar todos os clientes na tabela 'clients'.
    :return: Uma lista com todos os clientes.
    '''
    cursor.execute('SELECT * FROM clients')
    return cursor.fetchall()