# Importaciones
from api import app
from flask import request, jsonify
from api.db.db import mysql
import jwt
import datetime

# Rutas de la clase Usuario

# Ruta /login
@app.route('/login', methods = ['POST'])
def login():
    
    auth = request.authorization
    #print("auth: ",auth)

    """ Control: existen valores para la autenticacion? """
    if not auth or not auth.username or not auth.password:
        return jsonify({"message": "No autorizado"}), 401       
            
    """ Control: existe y coincide el usuario en la BD? """
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuario WHERE username = %s AND password = %s', (auth.username, auth.password))
    row = cur.fetchone()
    
    # Se pregunta si trajo algun registro la consulta
    if not row:
       return jsonify({"message": "No autorizado"}), 401  
    
    """ El usuario existe en la BD y coincide su contraseña """
    # minutes = 600 -> 10 horas
    token = jwt.encode({'id': row[0],
                        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=600)}, app.config['SECRET_KEY'])

    return jsonify({"token": token, "username": auth.username , "id": row[0]})
