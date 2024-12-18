TABLES = {
    "clientes": """
        CREATE TABLE IF NOT EXISTS clientes (
            pk_cliente INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        );
    """,
    "avioes": """
        CREATE TABLE IF NOT EXISTS avioes (
            pk_aviao INTEGER PRIMARY KEY,
            fabricante TEXT NOT NULL,
            modelo TEXT NOT NULL,
            capacidade INTEGER NOT NULL,
            UNIQUE (fabricante, modelo)
        );
    """,
    "aeroportos":"""
        CREATE TABLE aeroportos (
            pk_aeroporto INTEGER PRIMARY KEY,
            codigo TEXT NOT NULL UNIQUE,
            nome TEXT NOT NULL,
            cidade TEXT NOT NULL,
            pais TEXT NOT NULL
        );
    """,
    "voos": """
        CREATE TABLE IF NOT EXISTS voos (
            pk_voo INTEGER PRIMARY KEY,
            codigo_voo TEXT NOT NULL UNIQUE CHECK (codigo_voo LIKE '___YYYYMMDD-___'),
            fk_origem INTEGER NOT NULL,
            fk_destino INTEGER NOT NULL,
            datahora_partida TEXT NOT NULL,
            datahora_chegada TEXT NOT NULL,
            status TEXT NOT NULL CHECK (status IN ('planejado', 'em andamento', 'concluido', 'cancelado')),
            fk_aviao INTEGER NOT NULL,
            FOREIGN KEY (fk_origem) REFERENCES aeroportos (pk_aeroporto),
            FOREIGN KEY (fk_destino) REFERENCES aeroportos (pk_aeroporto),
            FOREIGN KEY(fk_aviao) REFERENCES avioes(pk_aviao)
        );
    """,
    "reservas": """
        CREATE TABLE IF NOT EXISTS reservas (
            pk_reserva INTEGER PRIMARY KEY,
            fk_cliente INTEGER NOT NULL,
            fk_voo INTEGER NOT NULL,
            data TEXT NOT NULL,
            status TEXT NOT NULL CHECK (status IN ('confirmada', 'cancelada', 'pendente')),
            classe TEXT NOT NULL CHECK (classe IN ('econômica', 'executiva', 'primeira classe')),
            assento TEXT NOT NULL,
            FOREIGN KEY(fk_cliente) REFERENCES clientes(pk_cliente),
            FOREIGN KEY(fk_voo) REFERENCES voos(pk_voo)
        );
    """
}
