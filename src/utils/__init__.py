from db.database import fetch_query

def trimmer(*args):
    """
    Remove espaços em branco de strings e retorna uma tupla.
    :param args: strings a serem tratadas.
    :return: tupla com as strings tratadas.
    """
    return tuple(s.strip() if isinstance(s, str) else s for s in args)

def generate_flight_code(origem, data):
    """
    Gera um código de voo com base no aeroporto de origem e na data.
    :param origem: Código do aeroporto de origem.
    :param data: Data do voo.
    :return: Código do voo.
    """
    cod_origem = fetch_query("SELECT codigo FROM aeroportos WHERE pk_aeroporto = ?;", (origem,), fetch_one=True)["codigo"]
    data = data.replace('-', '')
    count = fetch_query("SELECT COUNT(*) as total FROM voos WHERE codigo_voo LIKE ?;", (f"{cod_origem}{data}%",), fetch_one=True)["total"]
    return f"{cod_origem}{data}-{count + 1:03d}"