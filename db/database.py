import sqlite3
import logging
from db.db_schemas import TABLES
from src.utils.utils import trimmer

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DatabaseManager:
    """
    Gerencia a conexão com o banco de dados utilizando o contexto do Python.

    Métodos:
        __enter__: Abre a conexão com o banco de dados.
        __exit__: Fecha a conexão ao sair do contexto.
    """
    def __init__(self, db_path='db/airxpress.db'):
        self.db_path = db_path

    def __enter__(self):
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.conn.row_factory = sqlite3.Row
            return self.conn
        except sqlite3.Error as e:
            logging.error(f"Erro ao conectar ao banco de dados: {e}")
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()

def execute_query(query, params=None, trim=False):
    """
    Executa uma query no banco de dados.
    :param query: string com a query a ser executada.
    :param params: tupla com os parâmetros da query.
    :return: cursor com os resultados da query.
    """
    with DatabaseManager() as conn:
        try:
            cursor = conn.cursor()
            if params:
                if trim:
                    params = trimmer(params)
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            conn.commit()
            logging.info(f"Query executada: {query}")
            return cursor
        except sqlite3.Error as e:
            logging.error(f"Erro ao executar query: {e}")
            raise

def fetch_query(query, params=None, fetch_one=False):
    """
    Executa uma query no banco de dados e retorna os resultados.
    :param query: string com a query a ser executada.
    :param params: tupla com os parâmetros da query.
    :param fetch_one: booleano para retornar apenas um resultado.
    :return: lista com os resultados da query.
    """
    with DatabaseManager() as conn:
        try:
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            results=  cursor.fetchone() if fetch_one else cursor.fetchall()
            if fetch_one and results:
                return dict(results)  # Retorna como um dicionário para fetch_one
            elif results:
                return [dict(row) for row in results]  # Retorna uma lista de dicionários para fetch_all
            else:
                return None
        except sqlite3.Error as e:
            logging.error(f"Erro ao buscar dados: {e}")
            return None

def initialize_db():
    """
    Inicializa o banco de dados, criando as tabelas necessárias caso ainda não existam.
    """
    with DatabaseManager() as conn:
        try:
            cursor = conn.cursor()
            conn.execute("BEGIN")
            for table_name, create_statement in TABLES.items():
                cursor.execute(create_statement)
                logging.info(f"Tabela '{table_name}' verificada/criada com sucesso.")
            conn.commit()
            logging.info("Banco de dados inicializado com sucesso!")
        except sqlite3.Error as e:
            conn.rollback() 
            logging.error(f"Erro ao inicializar banco de dados: {e}")
            raise
