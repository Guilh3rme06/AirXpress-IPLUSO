import logging
from db.database import execute_query, fetch_all_from_table, fetch_query
from src.utils import generate_flight_code

def insert_voo(origem, destino, datahora_partida, datahora_chegada, status, fk_aviao):
    """
    Insere um voo no banco de dados.
    :param origem: ID do aeroporto de origem.
    :param destino: ID do aeroporto de destino.
    :param datahora_partida: Data e hora da partida.
    :param datahora_chegada: Data e hora da chegada.
    :param status: Status do voo.
    :param fk_aviao: ID do avião.
    """
    codigo_voo = generate_flight_code(origem, datahora_partida[:10])
    execute_query(
        "INSERT INTO voos (codigo_voo, origem, destino, datahora_partida, datahora_chegada, status, fk_aviao) VALUES (?, ?, ?, ?, ?, ?, ?);",
        (codigo_voo, origem, destino, datahora_partida, datahora_chegada, status, fk_aviao)
    )
    logging.info("Voo inserido com sucesso!")

def insert_voos(voos):
    """
    Insere múltiplos voos no banco de dados.
    :param voos: Lista de dicionários com os dados dos voos.
    """
    for voo in voos:
        execute_query(
            "INSERT INTO voos (codigo_voo, origem, destino, datahora_partida, datahora_chegada, status, fk_aviao) VALUES (?, ?, ?, ?, ?, ?, ?);",
            (voo["codigo_voo"], voo["origem"], voo["destino"], voo["datahora_partida"], voo["datahora_chegada"], voo["status"], voo["fk_aviao"])
        )
    logging.info(f"{len(voos)} voos inseridos com sucesso!")

def get_voos():
    """
    Retorna todos os voos cadastrados no banco de dados.
    :return: Lista de dicionários com os dados dos voos.
    """
    return fetch_all_from_table("voos")

def get_voo_by_id(pk_voo):
    """
    Retorna os detalhes de um voo com base no ID.
    :param pk_voo: ID do voo.
    :return: Dicionário com os dados do voo.
    """
    return fetch_query("SELECT * FROM voos WHERE pk_voo = ?;", (pk_voo,), fetch_one=True)

def update_voo(pk_voo, **fields):
    """
    Atualiza campos de um voo com base no ID.
    :param pk_voo: ID do voo.
    :param fields: Dicionário com os campos a serem atualizados.
    """
    if not fields:
        logging.warning("Nenhum campo foi passado para atualizar.")
        return

    columns = ", ".join([f"{key} = ?" for key in fields.keys()])
    values = list(fields.values()) + [pk_voo]

    execute_query(f"UPDATE voos SET {columns} WHERE pk_voo = ?;", values)
    logging.info(f"Voo com ID {pk_voo} atualizado com sucesso!")

def update_voo(pk_voo, origem, destino, datahora_partida, datahora_chegada, status, fk_aviao):
    execute_query('UPDATE voos SET origem = ?, destino = ?, datahora_partida = ?, datahora_chegada = ?, status = ?, fk_aviao = ? WHERE pk_voo = ?',
                  (origem, destino, datahora_partida, datahora_chegada, status, fk_aviao, pk_voo))
    logging.info(f"Voo com ID {pk_voo} atualizado com sucesso!")

def delete_voo(pk_voo):
    """
    Remove um voo do banco de dados com base no ID.
    :param pk_voo: ID do voo.
    """
    execute_query("DELETE FROM voos WHERE pk_voo = ?;", (pk_voo,))
    logging.info(f"Voo com ID {pk_voo} deletado com sucesso!")
    
def count_voos():
    """
    Retorna a quantidade total de voos cadastrados.
    :return: Total de voos.
    """
    return fetch_query("SELECT COUNT(*) as total FROM voos;", fetch_one=True)["total"]

def count_voos_ativos():
    """
    Retorna a quantidade de voos ativos (planejados ou em andamento).
    :return: Total de voos ativos.
    """
    return fetch_query("SELECT COUNT(*) as total FROM voos WHERE status IN ('planejado', 'em andamento');", fetch_one=True)["total"]
