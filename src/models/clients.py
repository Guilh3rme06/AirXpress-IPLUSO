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

def get_clientes():
    """
    Retorna todos os clientes cadastrados.
    :return: lista de dicionários com os dados dos clientes.
    """
    return execute_query("SELECT * FROM clientes;")

def update_cliente(nome, email, user_id):
    """
    Atualiza os dados de um cliente no banco de dados.
    """
    execute_query('UPDATE clientes SET nome = ?, email = ? WHERE pk_cliente = ?', (nome, email, user_id))

def get_cliente(user_id):
    """
    Retorna um cliente específico.
    """
    return execute_query('SELECT * FROM clientes WHERE pk_cliente = ?', (user_id,), fetch_one=True)

def delete_cliente(user_id):
    """
    Deleta um cliente do banco de dados.
    """
    execute_query('DELETE FROM clientes WHERE pk_cliente = ?', (user_id,))