from flask import Flask
from database.sqlite import  init_db

from route.user import user_blueprint  # Importação do Blueprint
from route.home import home_blueprint  # Importação do Blueprint
app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

# Registra o Blueprint
app.register_blueprint(user_blueprint, url_prefix='/users')
app.register_blueprint(home_blueprint, url_prefix='/')

@app.route('/')
def index():
    return 'API de Usuários'

if __name__ == '__main__':
    init_db()  # Inicializa o banco de dados
    app.run(debug=True)

# python app.py
# flask --app hello run
# flask run --host=0.0.0.0  serve pra deixar acessivel externamente
#pip install Flask Flask-JWT-Extended
#from markupsafe import escape