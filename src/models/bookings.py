import logging
from db.database import execute_query

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