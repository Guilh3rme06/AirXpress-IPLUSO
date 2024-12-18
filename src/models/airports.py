import logging

from db.database import execute_query, fetch_all_from_table, fetch_query

def insert_aeroporto(codigo, nome, cidade, pais):
    """
    Insere um aeroporto no banco de dados.
    :param codigo: Código do aeroporto.
    :param nome: Nome do aeroporto.
    :param cidade: Cidade do aeroporto.
    :param pais: País do aeroporto.
    """
    execute_query(
        "INSERT INTO aeroportos (codigo, nome, cidade, pais) VALUES (?, ?, ?, ?);",
        (codigo, nome, cidade, pais)
    )
    logging.info("Aeroporto inserido com sucesso!")

def insert_aeroportos(aeroportos):
    """
    Insere aeroportos no banco de dados.
    :param aeroportos: Lista de dicionários com os dados dos aeroportos.
    """
    for aeroporto in aeroportos:
        execute_query(
            "INSERT INTO aeroportos (codigo, nome, cidade, pais) VALUES (?, ?, ?, ?);",
            (aeroporto["codigo"], aeroporto["nome"], aeroporto["cidade"], aeroporto["pais"])
        )
    logging.info(f"{len(aeroportos)} aeroportos inseridos com sucesso!")
    
def select_aeroportos():
    """
    Seleciona todos os aeroportos do banco de dados.
    :return: Lista de dicionários com os dados dos aeroportos.
    """
    return fetch_all_from_table("aeroportos")

def select_aeroporto(pk_aeroporto):
    """
    Seleciona um aeroporto do banco de dados.
    :param pk_aeroporto: Chave primária do aeroporto.
    :return: Dicionário com os dados do aeroporto.
    """
    return fetch_query("SELECT * FROM aeroportos WHERE pk_aeroporto = ?;", (pk_aeroporto,), fetch_one=True)

def update_aeroporto(pk_aeroporto, codigo, nome, cidade, pais):
    """
    Atualiza os dados de um aeroporto no banco de dados.
    :param pk_aeroporto: Chave primária do aeroporto.
    :param codigo: Código do aeroporto.
    :param nome: Nome do aeroporto.
    :param cidade: Cidade do aeroporto.
    :param pais: País do aeroporto.
    """
    execute_query(
        "UPDATE aeroportos SET codigo = ?, nome = ?, cidade = ?, pais = ? WHERE pk_aeroporto = ?;",
        (codigo, nome, cidade, pais, pk_aeroporto)
    )
    logging.info("Aeroporto atualizado com sucesso!")
    
def delete_aeroporto(pk_aeroporto):
    """
    Remove um aeroporto do banco de dados.
    :param pk_aeroporto: Chave primária do aeroporto.
    """
    execute_query("DELETE FROM aeroportos WHERE pk_aeroporto = ?;", (pk_aeroporto,))
    logging.info("Aeroporto removido com sucesso!")
