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
├── 📂 app/
│   ├── 📂 assets/         # Recursos estáticos como CSS, JS e imagens
│   ├── 📂 routes/         # Arquivos de rotas para organizar endpoints
│   ├── 📂 services/       # Lógica de negócio organizada em serviços
│   ├── 📂 templates/      # Arquivos HTML utilizados pela aplicação
│   └── __init__.py        # Inicialização da aplicação Flask
├── 📂 db/                 # Banco de dados e scripts de inicialização
├── 📂 src/                # CRUD e utilitários para manipulação de dados
├── requirements.txt       # Dependências do projeto
├── run.py                 # Ponto de entrada principal da aplicação
└── README.md              # Documentação do projeto
```
