# routes/user_routes.py
from flask import Blueprint, request
from services.user_service import UserService

user_service = UserService()

# Criação de um Blueprint para as rotas de usuário
user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    return user_service.register(username, password)

@user_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    return user_service.authenticate(username, password)

@user_blueprint.route('/', methods=['GET'])
def get_users():
    return user_service.get_all_users()
