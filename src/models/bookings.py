import logging
from db.database import execute_query, fetch_all_from_table, fetch_query

def insert_reserva(fk_cliente, fk_voo, data):
    """
    Insere uma reserva no banco de dados.
    :param fk_cliente: chave estrangeira do cliente.
    :param fk_voo: chave estrangeira do voo.
    :param data: data da reserva.
    """
    execute_query(
        "INSERT INTO reservas (fk_cliente, fk_voo, data) VALUES (?, ?, ?);",
        (fk_cliente, fk_voo, data)
    )
    logging.info("Reserva inserida com sucesso!")

def insert_reservas(reservas):
    """
    Insere reservas no banco de dados.
    :param reservas: lista de dicionários com os dados das reservas.
    """
    for reserva in reservas:
        execute_query(
            "INSERT INTO reservas (fk_cliente, fk_voo, data) VALUES (?, ?, ?);",
            (reserva["fk_cliente"], reserva["fk_voo"], reserva["data"])
        )
    logging.info(f"{len(reservas)} reservas inseridas com sucesso!")

def get_reservas():
    """
    Retorna todas as reservas cadastradas.
    :return: lista de dicionários com os dados das reservas.
    """
    return fetch_all_from_table("reservas")

def get_reserva(reserva_id):
    """
    Retorna os dados de uma reserva específica.
    :param reserva_id: id da reserva a ser retornada.
    :return: dicionário com os dados da reserva.
    """
    return fetch_query('SELECT * FROM reservas WHERE pk_reserva = ?', (reserva_id,), fetch_one=True)

def update_reserva(reserva_id, fk_cliente, fk_voo, data):
    """
    Atualiza uma reserva no banco de dados.
    :param reserva_id: id da reserva a ser atualizada.
    :param fk_cliente: chave estrangeira do cliente.
    :param fk_voo: chave estrangeira do voo.
    :param data: data da reserva.
    """
    execute_query(
        "UPDATE reservas SET fk_cliente = ?, fk_voo = ?, data = ? WHERE pk_reserva = ?;",
        (fk_cliente, fk_voo, data, reserva_id)
    )
    logging.info(f"Reserva {reserva_id} atualizada com sucesso!")
    
def delete_reserva(reserva_id):
    """
    Deleta uma reserva do banco de dados.
    :param reserva_id: id da reserva a ser deletada.
    """
    execute_query('DELETE FROM reservas WHERE pk_reserva = ?', (reserva_id,))
    logging.info(f"Reserva {reserva_id} deletada com sucesso!")