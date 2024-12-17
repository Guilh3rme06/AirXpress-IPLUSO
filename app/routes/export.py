import os
import logging
from flask import Blueprint, send_file, flash, redirect, url_for
from src.utils.util_export import export_table_to_csv

export_bp = Blueprint('export', __name__)

EXPORT_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'exports')

os.makedirs(EXPORT_FOLDER, exist_ok=True)

@export_bp.route('/export/<table_name>', methods=['GET'])
def export_table(table_name):
    """
    Exporta os dados de uma tabela para um arquivo CSV e permite o download.
    """
    try:
        output_file = os.path.join(EXPORT_FOLDER, f"{table_name}.csv")
        
        export_table_to_csv(table_name, output_file)

        # Retorna o arquivo como download
        return send_file(output_file, as_attachment=True)
    except ValueError as ve:
        flash(f"Erro: {ve}", 'error')
        logging.error(f"Erro ao exportar tabela: {ve}")
        return redirect(url_for('main.index_route'))
    except Exception as e:
        flash(f"Erro inesperado: {e}", 'error')
        logging.error(f"Erro inesperado ao exportar tabela: {e}")
        return redirect(url_for('main.index_route'))
