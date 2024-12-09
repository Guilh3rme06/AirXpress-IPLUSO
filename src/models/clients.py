import logging
from db.database import execute_query

def insert_cliente(nome, email):
    """
    Insere um cliente no banco de dados.
    :param nome: nome do cliente.
    :param email: email do cliente.
    """
    execute_query(
        "INSERT INTO clientes (nome, email) VALUES (?, ?);",
        (nome, email)
    )
    logging.info("Cliente inserido com sucesso!")
    
def insert_clientes(clientes):
    """
    Insere clientes no banco de dados.
    :param clientes: lista de dicionários com os dados dos clientes.
    """
    for cliente in clientes:
        execute_query(
            "INSERT INTO clientes (nome, email) VALUES (?, ?);",
            (cliente["nome"], cliente["email"])
        )
    logging.info(f"{len(clientes)} clientes inseridos com sucesso!")