import logging
from db.database import execute_query, fetch_all_from_table, fetch_query

def insert_voo(origem, destino, datahora_partida, datahora_chegada, status, fk_aviao):
    """
    Insere um novo voo no banco de dados.
    :param origem: Local de origem.
    :param destino: Local de destino.
    :param datahora_partida: Data e hora de partida (YYYY-MM-DD HH:MM:SS).
    :param datahora_chegada: Data e hora de chegada (YYYY-MM-DD HH:MM:SS).
    :param status: Status do voo.
    :param fk_aviao: ID do avião.
    """
    execute_query(
        "INSERT INTO voos (origem, destino, datahora_partida, datahora_chegada, status, fk_aviao) VALUES (?, ?, ?, ?, ?, ?);",
        (origem, destino, datahora_partida, datahora_chegada, status, fk_aviao)
    )
    logging.info("Voo inserido com sucesso!")

def insert_voos(voos):
    """
    Insere múltiplos voos no banco de dados.
    :param voos: Lista de dicionários com os dados dos voos.
    """
    for voo in voos:
        execute_query(
            "INSERT INTO voos (origem, destino, datahora_partida, datahora_chegada, status, fk_aviao) VALUES (?, ?, ?, ?, ?, ?);",
            (voo["origem"], voo["destino"], voo["datahora_partida"], voo["datahora_chegada"], voo["status"], voo["fk_aviao"])
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

def search_voos(origem=None, destino=None):
    """
    Busca voos com base na origem e/ou destino.
    :param origem: Local de origem (opcional).
    :param destino: Local de destino (opcional).
    :return: Lista de dicionários com os voos encontrados.
    """
    query = "SELECT * FROM voos WHERE 1=1"
    params = []

    if origem:
        query += " AND origem = ?"
        params.append(origem)

    if destino:
        query += " AND destino = ?"
        params.append(destino)

    return fetch_query(query, params)

def update_voo_status(pk_voo, status):
    """
    Atualiza o status de um voo.
    :param pk_voo: ID do voo.
    :param status: Novo status do voo.
    """
    execute_query("UPDATE voos SET status = ? WHERE pk_voo = ?;", (status, pk_voo))
    logging.info(f"Status do voo com ID {pk_voo} alterado para '{status}'.")

def list_voos_by_status(status):
    """
    Lista todos os voos com base no status.
    :param status: Status do voo.
    :return: Lista de dicionários com os voos encontrados.
    """
    valid_status = ['planejado', 'em andamento', 'concluido', 'cancelado']
    if status not in valid_status:
        logging.error(f"Status inválido: {status}.")
        raise ValueError("Status inválido.")

    return fetch_query("SELECT * FROM voos WHERE status = ?;", (status,))

def list_voos_by_date_range(start_date, end_date):
    """
    Retorna voos que ocorrem dentro de um intervalo de datas.
    :param start_date: Data inicial (YYYY-MM-DD).
    :param end_date: Data final (YYYY-MM-DD).
    :return: Lista de dicionários com os voos encontrados.
    """
    return fetch_query(
        "SELECT * FROM voos WHERE datahora_partida >= ? AND datahora_partida <= ?;",
        (start_date, end_date)
    )

def count_voos_by_status():
    """
    Retorna a contagem de voos agrupados por status.
    :return: Dicionário com o status como chave e a contagem como valor.
    """
    result = fetch_query("SELECT status, COUNT(*) as total FROM voos GROUP BY status;")
    return {row["status"]: row["total"] for row in result}

def assentos_disponiveis(pk_voo):
    """
    Retorna a quantidade de assentos disponíveis em um voo.
    """
    try:
        voo = get_voo_by_id(pk_voo)
        if not voo:
            logging.error(f"Voo com ID {pk_voo} não encontrado.")
            return 0

        capacidade = fetch_query("SELECT capacidade FROM avioes WHERE pk_aviao = ?;", (voo["fk_aviao"],), fetch_one=True)
        if not capacidade:
            logging.error(f"Capacidade do avião do voo com ID {pk_voo} não encontrada.")
            return 0

        assentos_ocupados = fetch_query("SELECT COUNT(*) as total FROM passagens WHERE fk_voo = ?;", (pk_voo,), fetch_one=True)
        if not assentos_ocupados:
            logging.error(f"Erro ao buscar assentos ocupados do voo com ID {pk_voo}.")
            return 0

        return capacidade["capacidade"] - assentos_ocupados["total"]
    except Exception as e:
        logging.error(f"Erro ao calcular assentos disponíveis: {e}")
        return 0
