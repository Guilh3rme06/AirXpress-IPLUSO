import csv
import logging
from db.database import fetch_all_from_table
from db.db_schemas import TABLES

def export_table_to_csv(table_name, output_file):
    """
    Exporta os dados de uma tabela SQLite para um arquivo CSV.
    :param table_name: Nome da tabela a ser exportada.
    :param output_file: Caminho do arquivo CSV de saída.
    """
    try:
        # Validar se a tabela existe
        if table_name not in TABLES.keys():
            raise ValueError(f"Tabela '{table_name}' não permitida. Tabelas válidas: {', '.join(TABLES.keys())}")
        
        # Buscar os dados da tabela usando fetch_all_from_table
        rows = fetch_all_from_table(table_name)

        # Verificar se há dados
        if not rows:
            print(f"A tabela '{table_name}' está vazia. Nenhum dado foi exportado.")
            return

        # Buscar os nomes das colunas (do primeiro registro)
        column_names = rows[0].keys()

        # Escrever os dados em um arquivo CSV
        with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=column_names)
            writer.writeheader()  # Escreve o cabeçalho
            writer.writerows(rows)  # Escreve os dados

        logging.info(f"Tabela '{table_name}' exportada com sucesso para '{output_file}'.")
    except ValueError as ve:
        logging.error(f"Erro ao exportar tabela '{table_name}': {ve}")
    except Exception as e:
        logging.error(f"Erro ao exportar tabela '{table_name}': {e}")
