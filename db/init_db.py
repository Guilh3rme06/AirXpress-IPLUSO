import logging
from db import initialize_db, execute_query
from seed_data import CLIENTES, AVIOES, VOOS, RESERVAS
from src.planes import insert_avioes

# Configuração de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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

def insert_voos(voos):
    """
    Insere voos no banco de dados.
    :param voos: lista de dicionários com os dados dos voos.
    """
    for voo in voos:
        execute_query(
            "INSERT INTO voos (origem, destino, data_partida, data_chegada, fk_aviao) VALUES (?, ?, ?, ?, ?);",
            (voo["origem"], voo["destino"], voo["data_partida"], voo["data_chegada"], voo["fk_aviao"])
        )
    logging.info(f"{len(voos)} voos inseridos com sucesso!")

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

def seed_data():
    """
    Insere dados fictícios nas tabelas do banco de dados.
    """
    try:
        # Inserção nas tabelas
        insert_clientes(CLIENTES)
        insert_avioes(AVIOES)
        insert_voos(VOOS)
        insert_reservas(RESERVAS)

        logging.info("Dados fictícios inseridos com sucesso!")
    except Exception as e:
        logging.error(f"Erro ao inserir dados fictícios: {e}")
        raise

if __name__ == "__main__":
    # Inicializa o banco de dados
    logging.info("Inicializando o banco de dados...")
    initialize_db()

    # Popula o banco de dados com dados fictícios
    logging.info("Populando o banco de dados com dados fictícios...")
    seed_data()
