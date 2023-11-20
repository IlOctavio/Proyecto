from functools import wraps
from flask import request, jsonify
import jwt
from api import app
from api.db.db import mysql


# Decorador para verificar el token
def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        #print(kwargs)
        token = None
        #print("request.headers: ", request.headers)
        # Se verifica si el token viene en el header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return jsonify({"message": "Falta el token"}), 401
        
        user_id = None
        # Se verifica si el user-id viene en el header
        if 'user-id' in request.headers:
            user_id = request.headers['user-id']

        if not user_id:
            return jsonify({"message": "Falta el usuario"}), 401
        
        try:
            # Se decodifica el token
            data = jwt.decode(token , app.config['SECRET_KEY'], algorithms = ['HS256'])
            
            token_id = data['id']
            # Se verifica que el id del token sea igual al id del usuario
            if int(user_id) != int(token_id):
                return jsonify({"message": "Error de id"}), 401
            
        except Exception as e:
            print(e)
            return jsonify({"message": str(e)}), 401

        return func(*args, **kwargs)
    return decorated

# Decorador para verificar que el id del usuario pasado por el headers sea igual al id del usuario del cliente en la bd
def client_resource(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        #print("Argumentos en client_resource: ", kwargs)
        id_cliente = kwargs['id_client']
        cur = mysql.connection.cursor()
        cur.execute('SELECT id_usuario FROM cliente WHERE id_cliente = {0}'.format(id_cliente)) 
        data = cur.fetchone()
        if data:
            """ print(data) """
            id_prop = data[0]
            user_id = request.headers['user-id']
            if int(id_prop) != int(user_id):
                return jsonify({"message": "No tiene permisos para acceder a este recurso"}), 401
        return func(*args, **kwargs)
    return decorated

# Decorador para verificar que el id del usuario pasado por el headers sea igual al id del usuario pasado por la ruta
def user_resources(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        #print("Argumentos en user_resources: ", kwargs)
        id_user_route = kwargs['id_user']
        user_id = request.headers['user-id']
        if int(id_user_route) != int(user_id):
            return jsonify({"message": "No tiene permisos para acceder a este recurso"}), 401
        return func(*args, **kwargs)
    return decorated
