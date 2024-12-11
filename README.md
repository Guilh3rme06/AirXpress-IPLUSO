<div align="center">
  <img src="app/assets/img/logo.png" width="200">
</div>

# AirXpress

O **AirXpess** é uma aplicação web desenvolvida em Python com o framework Flask, que permite gerenciar voos, clientes e reservas de forma prática e intuitiva. A aplicação utiliza SQLite3 como banco de dados e segue boas práticas de organização de código, tornando o projeto escalável e fácil de manter.

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
- **Registo de Reservas:** Crie novas reservas vinculando clientes a voos.
- **Consulta de Reservas:** Visualize informações detalhadas das reservas realizadas.
- **Atualização de Reservas:** Modifique dados de reservas existentes.
- **Eliminação de Reservas:** Exclua reservas indesejadas.

### Outras Funcionalidades
- **Interface Web:** Interaja com a aplicação através de páginas HTML dinâmicas.
- **Armazenamento Local:** Persistência de dados utilizando o banco de dados SQLite3.
- **Organização Modular:** Código estruturado com rotas, serviços, templates e modelos.

## 🛠️ Tecnologias Utilizadas

- **Python** 🐍 — Linguagem de programação principal.
- **Flask** 🌐 — Framework web para criação de aplicações escaláveis.
- **SQLite3** 📂 — Banco de dados relacional local.
- **HTML5 + CSS3** 🎨 — Templates estilizados para a interface da aplicação.
<!--- **JavaScript** ⚡ — Scripts para interatividade e funcionalidades adicionais no front-end. -->

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

A aplicação estará disponível em: [http://127.0.0.1:5000](http://127.0.0.1:5000)

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

## 🧩 Próximos Passos

1. **Melhorar o Design:** Implementar um layout mais moderno e responsivo.
