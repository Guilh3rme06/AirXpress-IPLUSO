import logging

from db.db import *

PLANE_TABLE = {
    "avioes": """
        CREATE TABLE IF NOT EXISTS avioes (
            pk_aviao INTEGER PRIMARY KEY,
            modelo TEXT NOT NULL,
            capacidade INTEGER NOT NULL
        );
    """
}

def create_table(table_name):
    """
    Cria uma tabela no banco de dados.
    :param table_name: nome da tabela.
    """
    execute_query(PLANE_TABLE[table_name])
    logging.info(f"Tabela {table_name} criada com sucesso!")

def insert_aviao(modelo, capacidade):
    """
    Insere um avião no banco de dados.
    :param modelo: modelo do avião.
    :param capacidade: capacidade do avião.
    """
    execute_query(
        "INSERT INTO avioes (modelo, capacidade) VALUES (?, ?);",
        (modelo, capacidade)
    )
    logging.info("Avião inserido com sucesso!")

def insert_avioes(avioes):
    """
    Insere aviões no banco de dados.
    :param avioes: lista de dicionários com os dados dos aviões.
    """
    for aviao in avioes:
        execute_query(
            "INSERT INTO avioes (modelo, capacidade) VALUES (?, ?);",
            (aviao["modelo"], aviao["capacidade"])
        )
    logging.info(f"{len(avioes)} aviões inseridos com sucesso!")
    
def select_avioes():
    """
    Seleciona todos os aviões do banco de dados.
    :return: lista de tuplas com os aviões.
    """
    return execute_query("SELECT * FROM avioes;")

def select_aviao(pk_aviao):
    """
    Seleciona um avião do banco de dados.
    :param pk_aviao: chave primária do avião.
    :return: tupla com os dados do avião.
    """
    return execute_query("SELECT * FROM avioes WHERE pk_aviao = ?;", (pk_aviao,))
    
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