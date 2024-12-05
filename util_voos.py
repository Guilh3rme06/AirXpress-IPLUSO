import sqlite3

conexao = sqlite3.connect('airxpress.db')
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

def consultar_voo(id_voo):
    cursor.execute('''
    SELECT origem, destino, data, capacidade
    FROM voos
    WHERE id = ?
    ''', (id_voo,))
    voo = cursor.fetchone()
    return voo

def fechar_conexao():
    cursor.close()
    conexao.close()


criar_tabela_voos()
voo = consultar_voo(1)  # Testando com o ID 1
print(voo)

fechar_conexao()
