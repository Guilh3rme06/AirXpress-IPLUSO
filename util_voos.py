import sqlite3
conexao = sqlite3.connect('airxpress-ipluso.db')
cursor = conexao.cursor()

def voo_consultar():
    id_voo = input('Número do voo -> ')
    cursor.execute('SELECT * from voos where pk_voos = ?', (id_voo))
    conexao.commit()

def voo_atualizar(titulo, autor, ano):
    id_voo = input('Número do voo -> ')
    option = input(f'O que pretende mudar\n'
                   '(1) origem\n'
                   '(2) data\n'
                   '(3) hora\n'
                   '(4) capacidade\n'
                   '(5) avião\n')
    match option:
        case '1':
           # mudar origem
        case '2':
            # mudar data
        case '3':
            # mudar data
        case '4':
            # mudar data
        case '5':
            # mudar data
    # cursor.execute('UPDATE voos SET (titulo, autor, ano) VALUES (?,?,?)', (titulo, autor, ano))
    conexao.commit()

def voo_(eliminartitulo, autor, ano):
    # cursor.execute('INSERT INTO musicas (titulo, autor, ano) VALUES (?,?,?)', (titulo, autor, ano))
    conexao.commit()