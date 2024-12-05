# AirXpress 
<img src="AirXpress.png" alt="logo"/>

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
bash
git clone https://github.com/kalebeccs/calcula-imc-ipluso.git
cd calcula-imc-ipluso
### 2. Crie um ambiente virtual:
bash
python -m venv venv
source venv/bin/activate  # No Windows, use: venv\Scripts\activate
### 3. Instale as dependências:
bash
pip install -r requirements.txt
### 4. Execute a aplicação:
bash
python src/app.py
## 🗂️ Estrutura do Projeto
plaintext
📁 calcula-imc-ipluso
├── 📂 assets                 # Recursos visuais
├── 📂 db
│   ├── db.py                 # Funções para manipulação do banco de dados
├── 📂 src
│   ├── app.py                # Arquivo principal da aplicação
│   ├── interface.py          # Funções da interface gráfica
│   ├── users.py              # Gerenciamento de usuários
│   └── utils.py              # Funções auxiliares
├── README.md                 # Documentação do projeto
└── requirements.txt          # Dependências do projeto
## 📊 Cálculo de IMC

O cálculo de IMC é realizado pela fórmula:
> IMC = Peso (kg) / [Altura (m)]²

### Classificação do IMC:
| Faixa de IMC         | Classificação            |
|-----------------------|--------------------------|
| Abaixo de 18,5       | Abaixo do peso           |
| 18,5 – 24,9          | Peso normal             |
| 25,0 – 29,9          | Sobrepeso               |
| 30,0 – 34,9          | Obesidade Grau I        |
| 35,0 – 39,9          | Obesidade Grau II       |
| Acima de 40,0        | Obesidade Grau III      |

## Preview
![Preview](assets/preview.png)
