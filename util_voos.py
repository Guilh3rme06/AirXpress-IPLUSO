import sqlite3
conexao = sqlite3.connect('airxpress-ipluso.db')
cursor = conexao.cursor()

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