# Importaciones
from api.db.db import mysql, DBError
from flask import jsonify

# Clase Producto
class Producto():
    # Esquema para validar los datos 
    schema = {
        "id_producto": int,
        "unidad_medida": str,
        "descripcion": str,
        "cantidad": int,
        "precio": float,
        "tipo": str,
        "activo": int
     }
    
    # Metodo para validar el esquema de los datos
    def check_data_schema(data):
        if data == None or type(data) != dict:
            return False
        # check if data contains all keys of schema
        for key in Producto.schema:
            if key not in data:
                return False
            # check if data[key] has the same type as schema[key]
            if type(data[key]) != Producto.schema[key]:
                return False
        return True

    # Constructor de la clase
    def __init__(self, row):
        self._id_producto = row[0]
        self._unidad_medida = row[1]
        self._descripcion = row[2]
        self._cantidad = row[3]
        self._precio = row[4]
        self._tipo = row[5]
        self._activo = row[6]

    # Metodo para convertir los datos en formato JSON
    def to_json(self):
        return {
            "id_producto": self._id_producto,
            "unidad_medida": self._unidad_medida,
            "descripcion": self._descripcion,
            "cantidad": self._cantidad,
            "precio": self._precio,
            "tipo": self._tipo,
            "activo": self._activo
        }
    
    # Metodo para preguntar si existe un producto en la BD
    def product_exists(descrip):
        cur = mysql.connection.cursor()
        
        cur.execute('SELECT * FROM producto WHERE descripcion  = %s', (descrip))
        cur.fetchall()
        
        return cur.rowcount > 0

    # Metodo para la creación de un Producto en la BD 
    def create_product(data):
        if Producto.check_data_schema(data):
            # check if product already exists
            if Producto.product_exists(data["descripcion"]):
                raise DBError("Error creating product - El producto ya existe")
            cur = mysql.connection.cursor()
            cur.execute('INSERT INTO producto (unidad_medida, descripcion, cantidad, precio,tipo, activo) VALUES (%s, %s, %s, %s, %s, %s )', (data["unidad_medida"], data["descripcion"], data["cantidad"], data["precio"], data["tipo"], data["activo"]))
            mysql.connection.commit()
            if cur.rowcount > 0:
                # get the id of the last inserted row
                cur.execute('SELECT LAST_INSERT_ID()')
                res = cur.fetchall()
                id = res[0][0]
                return Producto((id, data["unidad_medida"], data["descripcion"], data["cantidad"], data["precio"], data["tipo"], data["activo"])).to_json()
            raise DBError("Error creating product - no row inserted")
        raise TypeError("Error creating product - wrong data schema")
    
    # Metodo para la actualización de un Producto en la BD
    def update_product(id, data):
        if Producto.check_data_schema(data):
            cur = mysql.connection.cursor()
            cur.execute('UPDATE producto SET unidad_medida = %s, descripcion = %s, cantidad = %s, precio = %s, tipo= %s, activo = %s WHERE id_producto = %s', (data["unidad_medida"], data["descripcion"], data["cantidad"], data["precio"], data["tipo"], data["activo"], id))
            mysql.connection.commit()
            if cur.rowcount > 0:
                return Producto.get_product_by_id(id)
            raise DBError("Error updating product - no row updated")
        raise TypeError("Error updating product - wrong data schema")
    
    # Metodo para obtener un producto por su id 
    def get_product_by_id(id):
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM producto WHERE id_producto = {0}'.format(id))
        data = cur.fetchall()
        if cur.rowcount > 0:
            #print("data[0]: ", data[0])
            return Producto(data[0]).to_json()
        raise DBError("Error getting product by id - no row found")
    
    # Metodo para eliminar a un producto de la BD
    def delete_product(id):
        data = Producto.get_product_by_id(id)
        cur = mysql.connection.cursor()
        cur.execute('UPDATE producto SET activo=0 WHERE id_producto = {0}'.format(id))
        mysql.connection.commit()
        if cur.rowcount > 0:
            return Producto.get_product_by_id(id)
        raise DBError("Error deleting product - no row updated")
        