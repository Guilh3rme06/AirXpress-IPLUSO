from datetime import datetime
import logging
from flask import render_template, request, redirect, url_for
from src.models.flights import delete_voo, get_voo_by_id, get_voos_com_detalhes, insert_voo, update_voo

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

VALID_STATUSES = {'planejado', 'em andamento', 'concluido', 'cancelado'}

def index_flights():
    """
    Rota para a página inicial de voos.
    """
    flights = get_voos_com_detalhes()
    return render_template('flights/flights.html', flights=flights, title='Voos | AirXpress')

def add_flights():
    if request.method == 'POST':
        origem = request.form['origem']
        destino = request.form['destino']
        datahora_partida_str = request.form['datahora_partida']
        datahora_chegada_str = request.form['datahora_chegada']
        status = request.form['status']
        
        # Converte as strings de data para objetos datetime
        datahora_partida = datetime.fromisoformat(datahora_partida_str)
        datahora_chegada = datetime.fromisoformat(datahora_chegada_str)
        
        # Formata as datas no formato desejado
        formatted_datahora_partida = datahora_partida.strftime('%d-%m-%Y %H:%M:%S')
        formatted_datahora_chegada = datahora_chegada.strftime('%d-%m-%Y %H:%M:%S')
        
        insert_voo(origem, destino, formatted_datahora_partida, formatted_datahora_chegada, status, 1)
        return redirect(url_for('flights.index_flights_route'))
    return render_template('flights/add_flight.html', title='Adicionar Voo | AirXpress')

def update_flights(voos_id):
    if request.method == 'POST':
        origem = request.form['origem'].strip()
        destino = request.form['destino'].strip()
        datahora_partida_str = request.form['datahora_partida']
        datahora_chegada_str = request.form['datahora_chegada']
        status = request.form['status']
        
        # Converte as strings de data para objetos datetime
        datahora_partida = datetime.fromisoformat(datahora_partida_str)
        datahora_chegada = datetime.fromisoformat(datahora_chegada_str)
        
        # Formata as datas no formato desejado
        formatted_datahora_partida = datahora_partida.strftime('%d-%m-%Y %H:%M:%S')
        formatted_datahora_chegada = datahora_chegada.strftime('%d-%m-%Y %H:%M:%S')
        
        update_voo(voos_id, origem, destino, formatted_datahora_partida, formatted_datahora_chegada, status, 1)
        return redirect(url_for('flights.index_flights_route'))
    
    flight = get_voo_by_id(voos_id)
    flight['datahora_partida'] = datetime.strptime(flight['datahora_partida'], '%d-%m-%Y %H:%M:%S').strftime('%Y-%m-%dT%H:%M')
    flight['datahora_chegada'] = datetime.strptime(flight['datahora_chegada'], '%d-%m-%Y %H:%M:%S').strftime('%Y-%m-%dT%H:%M')
    return render_template('flights/update_flight.html', flight=flight, title='Atualizar Voo | AirXpress')

def delete_flights(voos_id):
    """
    Rota para deletar um voo.
    """
    delete_voo(voos_id)
    return redirect(url_for('flights.index_flights_route')) 

def obter_status_validos():
    """
    Retorna os status válidos disponíveis para os voos.
    :return: Lista de status válidos.
    """
    return list(VALID_STATUSES)

def validar_status(status):
    """
    Valida se o status é válido. Loga uma mensagem de erro em caso de falha.

    :param status: O status a ser validado.
    :raises ValueError: Caso o status seja inválido.
    """
    if status not in VALID_STATUSES:
        logging.error(f"Status inválido: '{status}'. Status permitido: {', '.join(VALID_STATUSES)}")
        raise ValueError(f"Status inválido: {status}.")
    else:
        logging.info(f"Status '{status}' validado com sucesso.")

def duracao_estimada(datahora_partida, datahora_chegada):
    """
    Calcula a duração estimada do voo em horas e minutos.
    
    :param datahora_partida: Data e hora de partida (formato: 'YYYY-MM-DD HH:MM:SS').
    :param datahora_chegada: Data e hora de chegada (formato: 'YYYY-MM-DD HH:MM:SS').
    :return: String representando a duração no formato 'Xh Ym'.
    :raises ValueError: Caso as datas sejam inválidas ou inconsistentes.
    """
    try:
        partida = datetime.strptime(datahora_partida, '%Y-%m-%d %H:%M:%S')
        chegada = datetime.strptime(datahora_chegada, '%Y-%m-%d %H:%M:%S')

        if chegada < partida:
            raise ValueError("Data de chegada não pode ser anterior à data de partida.")

        duracao = chegada - partida
        horas, resto = divmod(duracao.seconds, 3600)
        minutos = resto // 60

        return f"{horas}h {minutos}m"
    except Exception as e:
        logging.error(f"Erro ao calcular duração estimada: {e}")
        raise

def capacidade_disponivel(total_assentos, assentos_reservados):
    """
    Calcula a capacidade disponível de assentos em um voo.
    
    :param total_assentos: Número total de assentos no avião.
    :param assentos_reservados: Número de assentos já reservados.
    :return: Número de assentos disponíveis.
    :raises ValueError: Caso os valores sejam inválidos.
    """
    if total_assentos < 0 or assentos_reservados < 0:
        logging.error("Total de assentos ou assentos reservados não pode ser negativo.")
        raise ValueError("Os valores não podem ser negativos.")

    if assentos_reservados > total_assentos:
        logging.error("O número de assentos reservados excede a capacidade total.")
        raise ValueError("Assentos reservados não podem exceder a capacidade total.")

    capacidade = total_assentos - assentos_reservados
    logging.info(f"Capacidade disponível calculada: {capacidade} assentos.")
    return capacidade

def validar_datas(datahora_partida, datahora_chegada):
    """
    Valida as datas de partida e chegada.
    
    :param datahora_partida: Data e hora de partida.
    :param datahora_chegada: Data e hora de chegada.
    :raises ValueError: Caso as datas sejam inválidas.
    """
    try:
        partida = datetime.strptime(datahora_partida, '%Y-%m-%d %H:%M:%S')
        chegada = datetime.strptime(datahora_chegada, '%Y-%m-%d %H:%M:%S')

        if chegada < partida:
            logging.error("Data de chegada não pode ser anterior à data de partida.")
            raise ValueError("Data de chegada inválida.")
        logging.info("Datas de partida e chegada validadas com sucesso.")
    except Exception as e:
        logging.error(f"Erro ao validar datas: {e}")
        raise
