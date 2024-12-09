from datetime import datetime
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

VALID_STATUSES = {'planejado', 'em andamento', 'concluido', 'cancelado'}

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
