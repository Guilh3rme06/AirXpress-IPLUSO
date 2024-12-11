import logging
from db.database import execute_query, fetch_query
from src.utils.util_flights import validar_status

def insert_voo(origem, destino, datahora_partida, datahora_chegada, status, fk_aviao):
    """
    Insere um voo no banco de dados.
    """
    if datahora_partida >= datahora_chegada:
        logging.error("Data de partida não pode ser posterior ou igual à data de chegada.")
        raise ValueError("Data de partida deve ser anterior à data de chegada.")
    
    try:
        execute_query(
            "INSERT INTO voos (origem, destino, datahora_partida, datahora_chegada, status, fk_aviao) VALUES (?, ?, ?, ?, ?, ?);",
            (origem, destino, datahora_partida, datahora_chegada, status, fk_aviao)
        )
        logging.info("Voo inserido com sucesso!")
    except Exception as e:
        logging.error(f"Erro ao inserir voo: {e}")
        raise

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
