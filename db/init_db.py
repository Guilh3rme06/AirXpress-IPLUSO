import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

from db.database import initialize_db
from seed_data import CLIENTES, AVIOES, AEROPORTOS, VOOS, RESERVAS
from src.models.clients import insert_clientes
from src.models.planes import insert_avioes
from models.airports import insert_aeroportos
from src.models.flights import insert_voos
from src.models.bookings import insert_reservas

def seed_data():
    """
    Insere dados fictícios nas tabelas do banco de dados.
    """
    try:
        # Inserção nas tabelas
        insert_clientes(CLIENTES)
        insert_avioes(AVIOES)
        insert_aeroportos(AEROPORTOS)
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
