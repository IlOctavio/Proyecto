--
-- Base de datos: `db_proyecto`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

-- CREATE TABLE `cliente` (
--  `id_cliente` int(10) NOT NULL,
--  `nombre` varchar(255) NOT NULL,
--  `apellido` varchar(255) NOT NULL,
--  `email` varchar(255) NOT NULL,
-- `dni` int(8) NOT NULL,
--  `activo` tinyint(1) DEFAULT NULL
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------
INSERT INTO cliente VALUES
(1, 'Juan', 'Álvarez' , 'juan@mail.com',   12345678, 1,1),
(2, 'Ana', 'Perez' , 'ana@mail.com', 87654321,1,1),
(3, 'Noelia','Cruz', 'noe@mail.com',12345678,1,2),
(4, 'Octavio', 'Chañe', 'octa@mail.com',23456789,1,3),
(5, 'Diego Manuel', 'Chañe', 'diego@mail.com', 34567890, 1,3);



--
-- Estructura de tabla para la tabla `compuesta_por`
--

-- CREATE TABLE `compuesta_por` (
--   `id_factura` int(10) NOT NULL,
--   `id_producto` int(10) NOT NULL,
--   `cantidad` int(10) NOT NULL,
--   `precio_unitario` double NOT NULL
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `factura`
--

-- CREATE TABLE `factura` (
--  `id_factura` int(10) NOT NULL,
--  `fecha` date NOT NULL,
--  `imp_neto` double DEFAULT NULL,
--  `iva` double NOT NULL,
--  `imp_total` double DEFAULT NULL,
--  `id_usuario` int(10) DEFAULT NULL,
--  `id_cliente` int(10) DEFAULT NULL
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------


--
-- Estructura de tabla para la tabla `producto`
--

-- CREATE TABLE `producto` (
--  `id_producto` int(10) NOT NULL,
--  `unidad_medida` varchar(20) NOT NULL,
--  `descripcion` varchar(255) NOT NULL,
--  `cantidad` int(10) NOT NULL,
--  `precio` double NOT NULL,
--  `tipo` varchar(8) NOT NULL,
--  `activo` tinyint(1) DEFAULT NULL
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO producto VALUES
(1,'un','monitor 19"','Monitor LCD marca Pirulo',20,25000,'producto',1),
(2,'un','gabinete ATX','Gabinete ATX con fuente 450W',30,10000,'producto',1),
(3,'un','core i3 11500','Procesador Intel Core I3 11500',25,50000,'producto',1),
(4,'un','DDR4 8GB', ' gabinete ATX','Gabinete ATX con fuente 450W',30,3000,'producto',1),
(5,'un','armado','armado de pc',100,12000,'servicio',1),
(6,'un','instalacion S.O.', 'instalacion del S. O.', 100,10000,'servicio',1),
(7,'un','formateo','formateo e inst. S.O.',100,15000,'servicio',1);






-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

-- CREATE TABLE `usuario` (
--  `id_usuario` int(10) NOT NULL,
--  `razon_social` varchar(255) NOT NULL,
--  `cuit` int(11) NOT NULL,
--  `username` varchar(255) NOT NULL,
-- `password` varchar(255) NOT NULL,
--  `tipo` varchar(5) NOT NULL,
--  `activo` tinyint(1) DEFAULT NULL
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO usuario VALUES
(1, 'Empresa SRL', 12345678901, 'user1', 'contra123', 'user', 1),
(2, 'Sociedad SA', 23456654321, 'user2', '123cont', 'user',1),
(3, 'local', 22334455667, 'admin', 'admin1234', 'admin' ,1);

