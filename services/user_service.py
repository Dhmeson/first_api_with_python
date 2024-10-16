import sqlite3
import re
from flask import jsonify
from database.sqlite import get_db_connection

class UserService:
    def register(self, username, password):
        validation_error = self.validate_user_credentials(username, password)
        if validation_error:
            return validation_error

        conn = get_db_connection()

        try:
            conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
        except sqlite3.IntegrityError:
            return jsonify({'error': 'Nome de usuário já existe.'}), 400
        finally:
            conn.close()

        return jsonify({'message': 'Usuário cadastrado com sucesso!'}), 201

    def authenticate(self, username, password):
        if not username or not password:
            return jsonify({'error': 'Nome de usuário e senha são obrigatórios.'}), 400

        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        conn.close()

        if user:
            return jsonify({'message': 'Login bem-sucedido!', 'user_id': user['id']}), 200
        else:
            return jsonify({'error': 'Usuário ou senha incorretos.'}), 401

    def get_all_users(self):
        conn = get_db_connection()
        users = conn.execute('SELECT id, username FROM users').fetchall()
        conn.close()

        user_list = [{'id': user['id'], 'username': user['username']} for user in users]
        return jsonify(user_list), 200

    def validate_user_credentials(self, username, password):
        if not username or len(username) < 4:
            return jsonify({'error': 'Nome de usuário deve ter pelo menos 4 caracteres.'}), 400

        if not password or len(password) < 6:
            return jsonify({'error': 'A senha deve ter pelo menos 6 caracteres.'}), 400
        
        if not re.search(r'[A-Za-z]', password):
            return jsonify({'error': 'A senha deve conter pelo menos uma letra.'}), 400
        
        if not re.search(r'\d', password):
            return jsonify({'error': 'A senha deve conter pelo menos um número.'}), 400
        
        if not re.search(r'[\W_]', password):
            return jsonify({'error': 'A senha deve conter pelo menos um caractere especial.'}), 400

        return None  # Indica que a validação passou
