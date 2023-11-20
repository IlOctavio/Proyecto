# Importaciones
from api.db.db import mysql, DBError
from flask import jsonify

# Clase Cliente
class Cliente():
    # Esquema para validar los datos 
    schema = {
        "id_cliente": int,
        "nombre": str,
        "apellido": str,
        "email": str,
        "dni": int,
        "activo": int,
        "id_usuario": int
    }
    
    # Metodo para validar el esquema de los datos
    def check_data_schema(data):
        if data == None or type(data) != dict:
            return False
        # check if data contains all keys of schema
        for key in Cliente.schema:
            if key not in data:
                return False
            # check if data[key] has the same type as schema[key]
            if type(data[key]) != Cliente.schema[key]:
                return False
        return True

    # Constructor de la clase
    def __init__(self, row):
        self._id_cliente = row[0]
        self._nombre = row[1]
        self._apellido = row[2]
        self._email = row[3]
        self._dni = row[4]
        self._activo = row[5]
        self._id_usuario = row[6]
        
    # Metodo para convertir los datos en formato JSON
    def to_json(self):
        return {
            "id_cliente": self._id_cliente,
            "nombre": self._nombre,
            "apellido": self._apellido,
            "email": self._email,
            "dni": self._dni,
            "activo": self._activo,
            "id_usuario": self._id_usuario
        }
    
    # Metodo para preguntar si existe un cliente en la BD
    def client_exists(dni):
        cur = mysql.connection.cursor()
        
        cur.execute('SELECT * FROM cliente WHERE dni = {0}'.format(dni))
        cur.fetchall()
        
        return cur.rowcount > 0

    # Metodo para la creación de un Cliente en la BD 
    def create_client(data):
        if Cliente.check_data_schema(data):
            # check if client already exists
            if Cliente.client_exists(data["dni"]):
                raise DBError("Error creating client - El cliente ya existe")
            cur = mysql.connection.cursor()
            cur.execute('INSERT INTO cliente (nombre, apellido, email, dni, activo, id_usuario) VALUES (%s, %s, %s, %s, %s, %s )', (data["nombre"], data["apellido"], data["email"], data["dni"], data["activo"], data["id_usuario"]))
            mysql.connection.commit()
            if cur.rowcount > 0:
                # get the id of the last inserted row
                cur.execute('SELECT LAST_INSERT_ID()')
                res = cur.fetchall()
                id = res[0][0]
                return Cliente((id, data["nombre"], data["apellido"], data["email"], data["dni"], data["activo"], data["id_usuario"])).to_json()
            raise DBError("Error creating client - no row inserted")
        raise TypeError("Error creating client - wrong data schema")
    
    # Metodo para la actualización de un Cliente en la BD
    def update_client(id, data):
        if Cliente.check_data_schema(data):
            cur = mysql.connection.cursor()
            cur.execute('UPDATE cliente SET nombre = %s, apellido = %s, email = %s, dni = %s, activo= %s, id_usuario = %s WHERE id_cliente = %s', (data["nombre"], data["apellido"], data["email"], data["dni"], data["activo"], data["id_usuario"], id))
            mysql.connection.commit()
            if cur.rowcount > 0:
                return Cliente.get_client_by_id(id)
            raise DBError("Error updating client - no row updated")
        raise TypeError("Error updating client - wrong data schema")
    
    # Metodo para obtener un cliente por su id 
    def get_client_by_id(id):
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM cliente WHERE id_cliente = {0}'.format(id))
        data = cur.fetchall()
        if cur.rowcount > 0:
            #print("data[0]: ", data[0])
            return Cliente(data[0]).to_json()
        raise DBError("Error getting client by id - no row found")
    
    # Metodo para eliminar a un cliente de la BD
    def delete_client(id):
        data = Cliente.get_client_by_id(id)
        cur = mysql.connection.cursor()
        cur.execute('UPDATE cliente SET nombre = %s, apellido = %s, email = %s, dni = %s, activo= %s, id_usuario = %s WHERE id_cliente = %s', (data["nombre"], data["apellido"], data["email"], data["dni"], 0, data["id_usuario"], id))
        mysql.connection.commit()
        if cur.rowcount > 0:
            return Cliente.get_client_by_id(id)
        raise DBError("Error deleting client - no row updated")
        