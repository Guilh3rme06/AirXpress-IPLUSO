import sqlite3
conexao = sqlite3.connect('airxpress-ipluso.db')
cursor = conexao.cursor()

def criar_tabela_voos():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS voos (
        id INTEGER PRIMARY KEY,
        origem TEXT NOT NULL,
        destino TEXT NOT NULL,
        data TEXT NOT NULL, -- Formato ISO: YYYY-MM-DD
        capacidade INTEGER NOT NULL -- Capacidade como número
    )
    """)
    conexao.commit()


def inserir_voos(origem, destino, data, capacidade):
    cursor.execute('INSERT INTO voos(origem,destino,data, capacidade) VALUES (?, ?, ?, ?)', (origem, destino, data, capacidade))
voos = [
    ('Lisboa', 'Dublin', '2023-12-23', 615),
    ('Barcelona','Madrid', '2024-02-21', 215),
    ('Fortaleza','Rio de Janeiro','2019-09-25', 323),
    ('Porto','Braga','2018-08-30', 556),
    ('Liverpool','Cork','2009-01-27', 91),
    ('Porto Alegre','Florianopolis','2014-06-23', 356)
]

for voo in voos:
    inserir_voos(*voo)

def ask_flight():
    return input('Número do voo -> ')

def voo_consultar():
    id_voo = ask_flight()
    cursor.execute('SELECT * from voos where pk_voos = ?', (id_voo,))
    conexao.commit()

def voo_atualizar(titulo, autor, ano):
    id_voo = ask_flight()
    option = input(f'O que pretende mudar\n'
                   '(1) origem\n'
                   '(2) data\n'
                   '(3) hora\n'
                   '(4) capacidade\n'
                   '(5) avião\n')
    match option:
        case '1': # mudar origem
            origem = input('Nova origem -> ')
        case '2': # mudar data
            data = input('Nova data -> ')
        case '3': # mudar hora
            hora = input('Nova hora -> ')
        case '4': # mudar capacidade
            capacidade = input('Nova capacidade -> ')
        case '5': # mudar avião
            print('') # Deve fazer consulta para procurar avião
    # cursor.execute('UPDATE voos SET (titulo, autor, ano) VALUES (?,?,?)', (titulo, autor, ano))
    # Esta chamada deve depender da option
    conexao.commit()

def voo_eliminar():
    id_voo = ask_flight()
    cursor.execute('DELETE FROM voos where pk_voos = ?', (id_voo,))
    conexao.commit()