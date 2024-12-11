<div align="center">
  <img src="app/assets/img/logo.png" width="200">
</div>

# AirXpress

O AirXpess é um projeto desenvolvido em Python, que permite gerenciar voos, clientes e reservas de forma prática e intuitiva. A aplicação utiliza SQLite3 como banco de dados.

## 📋 Funcionalidades

### Gestão de Voos

- **Registo de Voos:** Insira informações como origem, destino, data e capacidade do avião.
- **Consulta de Voos:** Realize consultas dos voos disponíveis e suas informações.
- **Atualização de Voos:** Atualize informações de voos existentes.
- **Eliminação de Voos:** Remova voos cadastrados.

### Gestão de Clientes

- **Registo de Clientes:** Insira informações como nome e e-mail.
- **Consulta de Clientes:** Realize consultas dos clientes registados e suas informações.
- **Atualização de Clientes:** Atualize informações de clientes registados.
- **Eliminação de Clientes:** Remova informações de clientes registados.

### Gestão de Reservas

- **Registo de Reservas:** Insira informações como origem, destino, data e capacidade do avião.
- **Consulta de Reservas:** Realize consultas dos voos disponíveis e suas informações.
- **Atualização de Reservas:** Atualize informações de voos existentes.
- **Eliminação de Reservas:** Remova voos cadastrados.

###

- **Armazenamento Local:** Persistência de dados usando o banco de dados SQLite.

## 🛠️ Tecnologias Utilizadas

- Python 🐍
- SQLite3 (banco de dados local) 📂

## ⚙️ Como Executar o Projeto

### Pré-requisitos

Certifique-se de ter o **Python 3.10** ou superior instalado e as dependências necessárias.

### 1. Clone o repositório:

```bash
git clone https://github.com/Guilh3rme06/AirXpress-IPLUSO.git
cd AirXpress-IPLUSO
```

### 2. Crie um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate  # No Windows, use: .venv\Scripts\activate
```

### 3. Instale as dependências:

```bash
pip install -r requirements.txt
```

### 4. Inicialize o banco de dados

```bash
python db/init_db.py
```

### 5. Execute a aplicação

```bash
python run.py
```

## 🗂️ Estrutura do Projeto

```plaintext
📁 AirXpress-IPLUSO/
├── 📂 assets/                # Recursos estáticos, como CSS, JS, imagens
│   ├── 📂 css/
│   ├── 📂 js/
│   └── 📂 img/
├── 📂 db/                    # Banco de dados e esquemas relacionados
│   ├── __init__.py           # Arquivo para inicializar o pacote, se necessário
│   ├── database.py           # Conexão com o banco de dados e inicialização
│   ├── db_schemas.py         # Definição das tabelas e esquemas
│   └── seed_data.py          # Dados fictícios para inicialização
├── 📂 src/                   # Lógica principal e manipulação de dados
│   ├── __init__.py
│   ├── 📂 models/               # CRUD e lógica de manipulação de tabelas
│   │   ├── __init__.py
│   │   ├── clients.py        # CRUD e lógica da tabela de clientes
│   │   ├── planes.py         # CRUD e lógica da tabela de aviões
│   │   ├── flights.py        # CRUD e lógica da tabela de voos
│   │   └── bookings.py       # CRUD e lógica da tabela de reservas
│   └── 📂 utils/                # Funções auxiliares, validações e transformações
│       ├── __init__.py
│       ├── util_clients.py   # Validações e verificações para clientes
│       ├── util_planes.py    # Validações e verificações para aviões
│       ├── util_flights.py   # Validações e verificações para voos
│       └── util_bookings.py  # Validações e verificações para reservas
├── 📂 templates/             # Arquivos HTML para interação com Flask
│   ├── 📂 clients/
│   │   ├── add_user.html
│   │   ├── update_user.html
│   │   └── user.html
│   ├── 📂 flights/
│   │   ├── add_flight.html
│   │   ├── update_flight.html
│   │   └── flight.html
│   ├── 📂 bookings/
│   │   ├── add_booking.html
│   │   ├── update_booking.html
│   │   └── booking.html
│   └── index.html
├── app.py                    # Ponto de entrada do Flask
├── README.md                 # Documentação do projeto
└── requirements.txt          # Dependências do Python
```
