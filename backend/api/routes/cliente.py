# Importaciones
from api import app
from api.models.cliente import Cliente
from flask import jsonify, request
from api.utils import token_required, client_resource, user_resources
from api.db.db import mysql

# Rutas de la clase Cliente

# Ruta de prueba
@app.route('/test_cliente')
def test():
    return jsonify({
        "message": "Grupo 14 - Backend - UPSO - 2023",
        "ruta": "ruta client"}) 

# Ruta GET: Get a client by id 
@app.route('/user/<int:id_user>/client/<int:id_client>', methods = ['GET'])
# Decoradores de autenticacion
@token_required
@user_resources
@client_resource
def get_client_by_id(id_user, id_client):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM cliente WHERE id_cliente = {0}'.format(id_client))
    data = cur.fetchall()
    if cur.rowcount > 0:
        objClient = Cliente(data[0])
        return jsonify( objClient.to_json() )
    return jsonify( {"message": "id not found"} ), 404

# Ruta GET: Get all clients by user id
@app.route('/user/<int:id_user>/client', methods = ['GET'])
# Decoradores de autenticacion
@token_required
@user_resources
def get_all_clients_by_user_id(id_user):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM cliente WHERE id_usuario = {0}'.format(id_user))
    data = cur.fetchall()
    clientList = []
    for row in data:
        objClient = Cliente(row)
        clientList.append(objClient.to_json())
    return jsonify(clientList)

# Ruta POST: Create a new client
@app.route('/user/<int:id_user>/client', methods = ['POST'])
@token_required
@user_resources
def create_client(id_user):
    data = request.get_json()
    data["id_usuario"] = id_user
    try:
        new_client = Cliente.create_client(data)
        return jsonify( new_client ), 201
    except Exception as e:
        return jsonify( {"message": e.args[0]} ), 400


# Ruta PUT:  Update a client
@app.route('/user/<int:id_user>/client/<int:id_client>', methods = ['PUT'])
@token_required
@user_resources
@client_resource
def update_client(id_user, id_client):
    data = request.get_json()
    data["id_usuario"] = id_user
    try:
        updated_client = Cliente.update_client(id_client, data)
        return jsonify( updated_client ), 200
    except Exception as e:
        return jsonify( {"message": e.args[0]} ), 400
    

# Ruta DELETE:  Delete a client
@app.route('/user/<int:id_user>/client/<int:id_client>', methods = ['DELETE'])
@token_required
@user_resources
@client_resource
def delete_client(id_user, id_client):
    try:
        deleted_client = Cliente.delete_client(id_client)
        return jsonify( deleted_client ), 200
    except Exception as e:
        return jsonify( {"message": e.args[0]} ), 400