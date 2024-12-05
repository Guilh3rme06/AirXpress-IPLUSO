import sqlite3

def criar_tabela_reservas():
    # Conecta ou cria o ficheiro da base de dados SQLite
    conn = sqlite3.connect('airxpress.db')
    cursor = conn.cursor()

    # Criação da tabela 'reservas'
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS reservas (
        pk_reserva INTEGER PRIMARY KEY AUTOINCREMENT,
        pk_cliente INTEGER,
        pk_voo INTEGER,
        data_reserva TEXT,
        FOREIGN KEY(cliente_id) REFERENCES clientes(id),
        FOREIGN KEY(voo_id) REFERENCES voos(id)
    )
    ''')

    # Confirmar as alterações
    conn.commit()
    conn.close()

from utils_bookings import verificar_reserva, validar_data_reserva  # Certifique-se de que as funções estão importadas corretamente

def adicionar_reserva(fk_cliente, fk_voo, data_reserva):
    # 1. Verifica se a data da reserva é válida (não pode ser uma data no passado)
    if not validar_data_reserva(data_reserva):
        return  # Se a data for inválida, a reserva não será feita

    # 2. Verifica se o voo tem espaço disponível
    if not verificar_reserva(fk_voo):
        print("Não é possível adicionar a reserva, o voo está cheio!")
        return  # Se o voo estiver cheio, a reserva não será feita

    # 3. Se as condições forem válidas, adiciona a reserva à base de dados
    conn = sqlite3.connect('airxpress.db')
    cursor = conn.cursor()

    # Adiciona a nova reserva na tabela 'reservas'
    cursor.execute('''
    INSERT INTO reservas (fk_cliente, fk_voo, data_reserva)
    VALUES (?, ?, ?)
    ''', (fk_cliente, fk_voo, data_reserva))

    conn.commit()
    conn.close()

    print(f"Reserva adicionada: Cliente ID {fk_cliente} -> Voo ID {fk_voo}, Data: {data_reserva}")

def listar_reservas():
    conn = sqlite3.connect('airxpress.db')
    cursor = conn.cursor()

    # Consulta para listar todas as reservas com os dados do cliente e voo
    cursor.execute('''
    SELECT reservas.pk_reserva, clientes.nome, clientes.email, voos.origem, voos.destino, reservas.data
    FROM reservas
    JOIN clientes ON reservas.fk_cliente = pk_clientes
    JOIN voos ON reservas.fk_voo = pk_voos
    ''')

    reservas = cursor.fetchall()
    conn.close()

    # Exibe todas as reservas
    for reserva in reservas:
        print(f"Reserva ID: {reserva[0]}, Cliente: {reserva[1]}, Email: {reserva[2]}, Voo: {reserva[3]} -> {reserva[4]}, Data: {reserva[5]}")

def eliminar_reserva(pk_reserva):
    conn = sqlite3.connect('airxpress.db')
    cursor = conn.cursor()

    # Deleta a reserva com o id correspondente
    cursor.execute('''
    DELETE FROM reservas WHERE pk_reserva = ?
    ''', (pk_reserva,))

    conn.commit()
    conn.close()

    return f"Reserva {pk_reserva} removida com sucesso!"

def listar_reservas_cliente(fk_cliente):
    conn = sqlite3.connect('airxpress.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT reservas.pk_reserva, voos.origem, voos.destino, reservas.data_reserva
    FROM reservas
    JOIN voos ON reservas.fk_voo = voos.id
    WHERE reservas.fk_cliente = ?
    ''', (fk_cliente,))

    reservas = cursor.fetchall()
    conn.close()

    return  reservas

