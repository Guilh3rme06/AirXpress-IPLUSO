import sqlite3
conexao = sqlite3.connect('airxpress-ipluso.db')
cursor = conexao.cursor()

def voo_consultar():
    id = input('Número do voo -> ')
    cursor.execute('SELECT * from voos where pk_voos = ?', (id))
    conexao.commit()

def voo_atualizar(titulo, autor, ano):
    cursor.execute('UPDATE voos SET (titulo, autor, ano) VALUES (?,?,?)', (titulo, autor, ano))
    conexao.commit()

def voo_(eliminartitulo, autor, ano):
    cursor.execute('INSERT INTO musicas (titulo, autor, ano) VALUES (?,?,?)', (titulo, autor, ano))
    conexao.commit()