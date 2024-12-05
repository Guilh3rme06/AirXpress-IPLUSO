import sqlite3

conn = sqlite3.connect('airxpress.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
    cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE
    )
''')
conn.commit()

def userRegist(name, email):
    for i in range(name):
        name = input("Write your name: ")
        email = int(input("Write your email: "))

    cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    print(f"User {name} successfully created!")

#Pedro e Tiago
    # Consultar uma lista de clientes registados
    def find_all_clients():
        '''
        Função para encontrar todos os clientes na tabela 'clients'.
        :return: Uma lista com todos os clientes.
        '''
        cursor.execute('SELECT * FROM clients')
        return cursor.fetchall()

    #Atualiza uma lista de clientes registado
    def update_client(client_id,new_name,new_email):
        id = int(input('Type client id: '))
        new_name = input('Write new name: ')
        new_email = input('Write new email: ')
        cursor.execute('SELECT * FROM users WHERE email = ? ', (new_email, ))
        existing_email = cursor.fetchone()

        if existing_email:
            print('Email already exists.')
        else:
            cursor.execute('''
            UPDATE users SET name = ?, email = ? WHERE client = ? ''', (new_name,new_email,client_id))
            print(f'User {new_name} created with success!')
        conn.commit()

    #Exclui um userid de uma lista
    def delete_client():
        id_exc = int(input('Write the userid that you want to delete: '))

        cursor.execute('DELETE FROM clients WHERE id = ?', (id_exc,))
        print(f'User with id {id_exc} success delete! ')

        conn.commit()