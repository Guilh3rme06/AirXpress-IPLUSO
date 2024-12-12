import logging

from db.database import execute_query, fetch_query

def insert_aviao(fabricante, modelo, capacidade):
    """
    Insere um avião no banco de dados.
    :param modelo: modelo do avião.
    :param capacidade: capacidade do avião.
    """
    execute_query(
        "INSERT INTO avioes (fabricante, modelo, capacidade) VALUES (?, ?, ?);",
        (fabricante, modelo, capacidade)
    )
    logging.info("Avião inserido com sucesso!")

def insert_avioes(avioes):
    """
    Insere aviões no banco de dados.
    :param avioes: lista de dicionários com os dados dos aviões.
    """
    for aviao in avioes:
        execute_query(
            "INSERT INTO avioes (fabricante, modelo, capacidade) VALUES (?, ?, ?);",
            (aviao["fabricante"], aviao["modelo"], aviao["capacidade"])
        )
    logging.info(f"{len(avioes)} aviões inseridos com sucesso!")
    
def select_avioes():
    """
    Seleciona todos os aviões do banco de dados.
    :return: lista de tuplas com os aviões.
    """
    return fetch_query("SELECT * FROM avioes;")

def select_aviao(pk_aviao):
    """
    Seleciona um avião do banco de dados.
    :param pk_aviao: chave primária do avião.
    :return: tupla com os dados do avião.
    """
    return fetch_query("SELECT * FROM avioes WHERE pk_aviao = ?;", (pk_aviao,), fetch_one=True)
    
def update_aviao(pk_aviao, modelo, capacidade):
    """
    Atualiza os dados de um avião no banco de dados.
    :param pk_aviao: chave primária do avião.
    :param modelo: modelo do avião.
    :param capacidade: capacidade do avião.
    """
    execute_query(
        "UPDATE avioes SET modelo = ?, capacidade = ? WHERE pk_aviao = ?;",
        (modelo, capacidade, pk_aviao)
    )
    logging.info("Avião atualizado com sucesso!")
    
def delete_aviao(pk_aviao):
    """
    Remove um avião do banco de dados.
    :param pk_aviao: chave primária do avião.
    """
    execute_query("DELETE FROM avioes WHERE pk_aviao = ?;", (pk_aviao,))
    logging.info("Avião removido com sucesso!")
