
from flask import Blueprint, render_template

# Criação de um Blueprint para as rotas com html
home_blueprint = Blueprint('home', __name__)

@home_blueprint.route('/register', methods=['GET'])
def register():
    resp = render_template('register.html')
    return resp


@home_blueprint.route('/login', methods=['GET'])
def login():
    resp = render_template('login.html')
    return resp