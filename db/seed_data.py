CLIENTES = [
    {"nome": "Lucas Almeida", "email": "lucas.almeida@email.com"},
    {"nome": "Camila Costa", "email": "camila.costa@email.com"},
    {"nome": "Felipe Rocha", "email": "felipe.rocha@email.com"},
    {"nome": "Juliana Martins", "email": "juliana.martins@email.com"},
    {"nome": "Rafael Pereira", "email": "rafael.pereira@email.com"},
    {"nome": "Carla Oliveira", "email": "carla.oliveira@email.com"},
    {"nome": "Gustavo Silva", "email": "gustavo.silva@email.com"},
    {"nome": "Mariana Lima", "email": "mariana.lima@email.com"},
    {"nome": "Thiago Sousa", "email": "thiago.sousa@email.com"},
    {"nome": "Fernanda Ribeiro", "email": "fernanda.ribeiro@email.com"},
    {"nome": "Ricardo Carvalho", "email": "ricardo.carvalho@email.com"},
    {"nome": "Patrícia Dias", "email": "patricia.dias@email.com"},
    {"nome": "André Costa", "email": "andre.costa@email.com"},
    {"nome": "Beatriz Mendes", "email": "beatriz.mendes@email.com"},
    {"nome": "Daniela Silva", "email": "daniela.silva@email.com"},
    {"nome": "Eduardo Rocha", "email": "eduardo.rocha@email.com"},
    {"nome": "Sofia Souza", "email": "sofia.souza@email.com"},
    {"nome": "João Oliveira", "email": "joao.oliveira@email.com"},
    {"nome": "Isabela Santos", "email": "isabela.santos@email.com"},
    {"nome": "Marcos Lima", "email": "marcos.lima@email.com"},
    {"nome": "Larissa Alves", "email": "larissa.alves@email.com"},
    {"nome": "Leandro Gomes", "email": "leandro.gomes@email.com"},
    {"nome": "Priscila Fernandes", "email": "priscila.fernandes@email.com"},
    {"nome": "Júlio Costa", "email": "julio.costa@email.com"},
    {"nome": "Viviane Pereira", "email": "viviane.pereira@email.com"},
    {"nome": "Simone Martins", "email": "simone.martins@email.com"},
    {"nome": "Fábio Rocha", "email": "fabio.rocha@email.com"},
    {"nome": "Cláudia Gomes", "email": "claudia.gomes@email.com"},
    {"nome": "Caio Ferreira", "email": "caio.ferreira@email.com"},
    {"nome": "Aline Barbosa", "email": "aline.barbosa@email.com"}
]

AVIOES = [
    {"fabricante": "Boeing", "modelo": "747", "capacidade": 416},
    {"fabricante": "Airbus", "modelo": "A380", "capacidade": 555},
    {"fabricante": "Embraer", "modelo": "E190", "capacidade": 114},
    {"fabricante": "Bombardier", "modelo": "CRJ900", "capacidade": 90},
    {"fabricante": "Boeing", "modelo": "777", "capacidade": 396},
    {"fabricante": "Airbus", "modelo": "A320", "capacidade": 220},
    {"fabricante": "Embraer", "modelo": "E195", "capacidade": 124},
    {"fabricante": "Bombardier", "modelo": "CRJ700", "capacidade": 78},
    {"fabricante": "Boeing", "modelo": "787", "capacidade": 330},
    {"fabricante": "Airbus", "modelo": "A330", "capacidade": 290}
]

VOOS = [
    {"origem": "São Paulo", "destino": "Rio de Janeiro", "datahora_partida": "10-12-2024 14:00:00", 
     "datahora_chegada": "10-12-2024 16:00:00", "status": "planejado", "fk_aviao": 1},
    
    {"origem": "Lisboa", "destino": "Porto", "datahora_partida": "11-12-2024 09:00:00", 
     "datahora_chegada": "11-12-2024 10:30:00", "status": "em andamento", "fk_aviao": 2},
    
    {"origem": "Nova York", "destino": "Toronto", "datahora_partida": "12-12-2024 08:00:00", 
     "datahora_chegada": "12-12-2024 10:30:00", "status": "planejado", "fk_aviao": 3},
    
    {"origem": "Tóquio", "destino": "Seul", "datahora_partida": "13-12-2024 06:00:00", 
     "datahora_chegada": "13-12-2024 08:00:00", "status": "concluido", "fk_aviao": 4},
    
    {"origem": "Paris", "destino": "Londres", "datahora_partida": "14-12-2024 16:00:00", 
     "datahora_chegada": "14-12-2024 17:15:00", "status": "planejado", "fk_aviao": 2},
    
    {"origem": "Rio de Janeiro", "destino": "Buenos Aires", "datahora_partida": "15-12-2024 19:00:00", 
     "datahora_chegada": "15-12-2024 21:30:00", "status": "cancelado", "fk_aviao": 1},
    
    {"origem": "Sydney", "destino": "Auckland", "datahora_partida": "16-12-2024 07:00:00", 
     "datahora_chegada": "16-12-2024 10:00:00", "status": "em andamento", "fk_aviao": 5},
    
    {"origem": "Dubai", "destino": "Doha", "datahora_partida": "17-12-2024 20:00:00", 
     "datahora_chegada": "17-12-2024 22:00:00", "status": "concluido", "fk_aviao": 3},
    
    {"origem": "Frankfurt", "destino": "Zurique", "datahora_partida": "18-12-2024 11:00:00", 
     "datahora_chegada": "18-12-2024 11:45:00", "status": "planejado", "fk_aviao": 2},
    
    {"origem": "Los Angeles", "destino": "San Francisco", "datahora_partida": "19-12-2024 14:00:00", 
     "datahora_chegada": "19-12-2024 14:50:00", "status": "em andamento", "fk_aviao": 4}
]

RESERVAS = [
    {"fk_cliente": 1, "fk_voo": 1, "data": "05-12-2024 10:00:00"},
    {"fk_cliente": 2, "fk_voo": 2, "data": "06-12-2024 12:00:00"},
    {"fk_cliente": 3, "fk_voo": 3, "data": "07-12-2024 14:00:00"},
    {"fk_cliente": 4, "fk_voo": 4, "data": "08-12-2024 16:00:00"},
    {"fk_cliente": 5, "fk_voo": 5, "data": "09-12-2024 18:00:00"},
    {"fk_cliente": 6, "fk_voo": 6, "data": "10-12-2024 08:00:00"},
    {"fk_cliente": 7, "fk_voo": 7, "data": "11-12-2024 13:00:00"},
    {"fk_cliente": 8, "fk_voo": 8, "data": "12-12-2024 15:00:00"},
    {"fk_cliente": 9, "fk_voo": 9, "data": "13-12-2024 10:00:00"},
    {"fk_cliente": 10, "fk_voo": 10, "data": "14-12-2024 17:00:00"},
    {"fk_cliente": 1, "fk_voo": 2, "data": "15-12-2024 09:00:00"},
    {"fk_cliente": 2, "fk_voo": 3, "data": "16-12-2024 14:00:00"},
    {"fk_cliente": 3, "fk_voo": 4, "data": "17-12-2024 18:00:00"},
    {"fk_cliente": 4, "fk_voo": 5, "data": "18-12-2024 08:30:00"},
    {"fk_cliente": 5, "fk_voo": 6, "data": "19-12-2024 10:00:00"},
    {"fk_cliente": 6, "fk_voo": 7, "data": "20-12-2024 13:45:00"},
    {"fk_cliente": 7, "fk_voo": 8, "data": "21-12-2024 16:20:00"},
    {"fk_cliente": 8, "fk_voo": 9, "data": "22-12-2024 19:00:00"},
    {"fk_cliente": 9, "fk_voo": 10, "data": "23-12-2024 20:30:00"},
    {"fk_cliente": 10, "fk_voo": 1, "data": "24-12-2024 07:00:00"},
    {"fk_cliente": 1, "fk_voo": 5, "data": "25-12-2024 15:00:00"},
    {"fk_cliente": 6, "fk_voo": 10, "data": "26-12-2024 17:45:00"},
    {"fk_cliente": 4, "fk_voo": 2, "data": "27-12-2024 09:30:00"},
    {"fk_cliente": 8, "fk_voo": 6, "data": "28-12-2024 12:15:00"},
    {"fk_cliente": 3, "fk_voo": 7, "data": "29-12-2024 20:50:00"},
    {"fk_cliente": 5, "fk_voo": 2, "data": "01-01-2025 10:15:00"},
    {"fk_cliente": 6, "fk_voo": 3, "data": "02-01-2025 13:30:00"},
    {"fk_cliente": 7, "fk_voo": 4, "data": "03-01-2025 11:00:00"},
    {"fk_cliente": 8, "fk_voo": 5, "data": "04-01-2025 17:00:00"},
    {"fk_cliente": 9, "fk_voo": 6, "data": "05-01-2025 08:45:00"},
    {"fk_cliente": 10, "fk_voo": 7, "data": "06-01-2025 09:30:00"},
    {"fk_cliente": 1, "fk_voo": 8, "data": "07-01-2025 12:20:00"},
    {"fk_cliente": 2, "fk_voo": 9, "data": "08-01-2025 14:50:00"},
    {"fk_cliente": 3, "fk_voo": 10, "data": "09-01-2025 11:15:00"},
    {"fk_cliente": 4, "fk_voo": 1, "data": "10-01-2025 13:30:00"},
    {"fk_cliente": 5, "fk_voo": 2, "data": "11-01-2025 15:00:00"},
    {"fk_cliente": 6, "fk_voo": 3, "data": "12-01-2025 10:45:00"},
    {"fk_cliente": 7, "fk_voo": 4, "data": "13-01-2025 16:10:00"},
    {"fk_cliente": 8, "fk_voo": 5, "data": "14-01-2025 17:30:00"},
    {"fk_cliente": 9, "fk_voo": 6, "data": "15-01-2025 20:00:00"},
    {"fk_cliente": 10, "fk_voo": 7, "data": "16-01-2025 09:20:00"},
    {"fk_cliente": 1, "fk_voo": 8, "data": "17-01-2025 12:40:00"},
    {"fk_cliente": 2, "fk_voo": 9, "data": "18-01-2025 14:00:00"}
]
