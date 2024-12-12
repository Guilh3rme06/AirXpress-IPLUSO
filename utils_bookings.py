import sqlite3

def verificar_reserva(fk_voo):
    # Conecta à base de dados
    conn = sqlite3.connect('airxpress.db')
    cursor = conn.cursor()

    # Consulta para obter a capacidade do voo
    cursor.execute('''
    SELECT capacidade FROM voos WHERE id = ?
    ''', (fk_voo,))
    capacidade_voo = cursor.fetchone()

    # Verifica se o voo existe
    if capacidade_voo is None:
        print(f"Erro: Voo ID {fk_voo} não encontrado.")
        conn.close()
        return False

    # Consulta para contar o número de reservas para o voo específico
    cursor.execute('''
    SELECT COUNT(*) FROM reservas WHERE fk_voo = ?
    ''', (fk_voo,))
    reservas_voo = cursor.fetchone()[0]

    # Verifica se a capacidade do voo foi atingida
    if reservas_voo >= capacidade_voo[0]:
        print(f"O voo {fk_voo} está cheio!")
        conn.close()
        return False
    else:
        print(f"O voo {fk_voo} tem espaço disponível.")
        conn.close()
        return True


from datetime import datetime


def validar_data_reserva(data_reserva):
    # Obtém a data atual no formato 'YYYY-MM-DD'
    data_atual = datetime.now().strftime('%Y-%m-%d')

    # Converte as strings de data para objetos datetime para comparação
    data_reserva_obj = datetime.strptime(data_reserva, '%Y-%m-%d')
    data_atual_obj = datetime.strptime(data_atual, '%Y-%m-%d')

    # Verifica se a data de reserva é posterior ou igual à data atual
    if data_reserva_obj < data_atual_obj:
        print(f"Erro: A data da reserva ({data_reserva}) já passou!")
        return False
    return True



