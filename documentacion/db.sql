CREATE DATABASE IF NOT EXISTS db_proyecto;
USE db_proyecto;

CREATE TABLE IF NOT EXISTS producto(
    id_producto INT(10) NOT NULL AUTO_INCREMENT,
	unidad_medida VARCHAR(20) NOT NULL,
	descripcion VARCHAR(255) NOT NULL,
	cantidad INT(10) NOT NULL,
	precio DOUBLE PRECISION NOT NULL,
	tipo VARCHAR(8) NOT NULL,
	activo BOOLEAN,
	PRIMARY KEY (id_producto)
) 

INSERT INTO person VALUES
(1, 'Juan', 'Álvarez' , 12345678, 'juan@mail.com'),
(2, 'Ana', 'Perez' , 87654321, 'ana@mail.com');

CREATE TABLE IF NOT EXISTS usuario(
    id_usuario INT(10) NOT NULL AUTO_INCREMENT,
    razon_social VARCHAR(255) NOT NULL,
    cuit INT(11) NOT NULL,
	username VARCHAR(255) NOT NULL,
	password VARCHAR(255) NOT NULL,
	tipo VARCHAR(5) NOT NULL,
	activo BOOLEAN,
    PRIMARY KEY (id_usuario)
) 

INSERT INTO users VALUES
(1, 'carlos', 'pass'),
(2, 'ana', 'pass');

CREATE TABLE IF NOT EXISTS cliente (
    id_cliente INT(10) NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
	apellido VARCHAR(255) NOT NULL,
	email VARCHAR(255) NOT NULL,
    dni INT(8) NOT NULL,
	activo BOOLEAN,
    PRIMARY KEY (id_cliente)
) 

CREATE TABLE IF NOT EXISTS client(
    id INT(10) NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id),
    id_user INT(10),
    FOREIGN KEY(id_user) REFERENCES users(id) 
) 

INSERT INTO client VALUES
(1, 'juan', 1),
(2, 'maria', 1),
(3, 'marta', 2),
(4, 'jose', 2);
