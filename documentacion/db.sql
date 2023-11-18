CREATE DATABASE IF NOT EXISTS db_proyecto;
USE db_proyecto;

CREATE TABLE IF NOT EXISTS producto(
    id_producto INT(10) NOT NULL AUTO_INCREMENT,
	unidad_medida VARCHAR(20) NOT NULL,
	descripcion VARCHAR(255) NOT NULL,
	cantidad INT(10) NOT NULL,
	precio DOUBLE NOT NULL,
	tipo VARCHAR(8) NOT NULL,
	activo BOOLEAN,
	PRIMARY KEY (id_producto)
);

CREATE TABLE IF NOT EXISTS usuario(
    id_usuario INT(10) NOT NULL AUTO_INCREMENT,
    razon_social VARCHAR(255) NOT NULL,
    cuit INT(11) NOT NULL,
	username VARCHAR(255) NOT NULL,
	password VARCHAR(255) NOT NULL,
	tipo VARCHAR(5) NOT NULL,
	activo BOOLEAN,
    PRIMARY KEY (id_usuario)
);

CREATE TABLE IF NOT EXISTS cliente (
    id_cliente INT(10) NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
	apellido VARCHAR(255) NOT NULL,
	email VARCHAR(255) NOT NULL,
    dni INT(8) NOT NULL,
	activo BOOLEAN,
	id_usuario INT(10),
	FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario),
    PRIMARY KEY (id_cliente)
);

CREATE TABLE IF NOT EXISTS factura (
	id_factura INT(10) NOT NULL AUTO_INCREMENT,
	fecha DATE NOT NULL,
	imp_neto DOUBLE,
	iva DOUBLE NOT NULL,
	imp_total DOUBLE,
	PRIMARY KEY (id_factura),
	id_usuario INT(10),
	id_cliente INT(10),	
    FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario),
	FOREIGN KEY(id_cliente) REFERENCES cliente(id_cliente)
);

CREATE TABLE IF NOT EXISTS compuesta_por (
	id_factura INT(10) NOT NULL,
	id_producto INT(10) NOT NULL,
	cantidad INT(10) NOT NULL,
	precio_unitario DOUBLE NOT NULL,
	PRIMARY KEY (id_factura, id_producto),
	FOREIGN KEY(id_factura) REFERENCES factura(id_factura),
	FOREIGN KEY(id_producto) REFERENCES producto(id_producto)
);




