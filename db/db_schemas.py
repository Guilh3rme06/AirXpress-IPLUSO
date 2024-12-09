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
    "voos": """
        CREATE TABLE IF NOT EXISTS voos (
            pk_voo INTEGER PRIMARY KEY,
            origem TEXT NOT NULL,
            destino TEXT NOT NULL,
            datahora_partida TEXT NOT NULL,
            datahora_chegada TEXT NOT NULL,
            status TEXT NOT NULL CHECK (status IN ('planejado', 'em andamento', 'concluido', 'cancelado')),
            fk_aviao INTEGER,
            FOREIGN KEY(fk_aviao) REFERENCES avioes(pk_aviao)
        );
    """,
    "reservas": """
        CREATE TABLE IF NOT EXISTS reservas (
            pk_reserva INTEGER PRIMARY KEY,
            fk_cliente INTEGER NOT NULL,
            fk_voo INTEGER NOT NULL,
            data TEXT NOT NULL,
            FOREIGN KEY(fk_cliente) REFERENCES clientes(pk_cliente),
            FOREIGN KEY(fk_voo) REFERENCES voos(pk_voo)
        );
    """
}
