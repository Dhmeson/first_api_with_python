# API de Usuários

Este projeto é uma API de registro e autenticação de usuários utilizando Flask e SQLite. Ele inclui rotas para registro, login e listagem de usuários, além de páginas HTML simples para interagir com a API.


## Funcionalidades

- **Registro de Usuário**: Permite que novos usuários se registrem com um nome de usuário e senha.
- **Login de Usuário**: Permite que usuários registrados façam login com suas credenciais.
- **Listar Usuários**: Permite visualizar todos os usuários registrados.
- **Validação de Credenciais**: Valida se o nome de usuário possui pelo menos 4 caracteres e se a senha atende a critérios específicos (mínimo de 6 caracteres, pelo menos um número, uma letra e um caractere especial).

## Pré-requisitos

- Python 3.6 ou superior
- Flask
- SQLite

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/Dhmeson/first_api_with_python.git
   cd seu_projeto

## Crie um ambiente virtual (opcional, mas recomendado):

python -m venv venv

source venv/bin/activate  # Para Linux ou Mac

venv\Scripts\activate     # Para Windows

## install lib
pip install Flask Flask-JWT-Extended python-dotenv bcrypt

## Execute a aplicação:
python app.py


# Exemplo de Uso da API

## Registrar um Usuário:
POST /users/register
{
    "username": "novo_usuario",
    "password": "senhaSegura123!"
}

## Login:
POST /users/login
{
    "username": "novo_usuario",
    "password": "senhaSegura123!"
}

## Listar Usuários:
GET /users/users


