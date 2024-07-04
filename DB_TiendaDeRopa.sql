#usuarios

-- Creacion de la base de datos --
create database DB_TiendaDeRopa


-- Explicacion configuraciones de las tablas --
	-- engine = InnoDB (declaración CREATE TABLE de MySQL especifica el motor de almacenamiento que se utilizará)
	-- default charset = utf8mb4 (soporta caracteres de 4 bytes, acepta caracteres especiales)
	-- collate = utf8mb4_unicode_ci (insensible a mayúsculas, minúsculas y acentos y sigue las reglas de Unicode)

-- Creacion de tablas --
create table Usuarios (
	id int primary key auto_increment,
    nombre varchar(50) not null, 
    apellido varchar(50) not null, 
    fecha_nacimiento date not null, 
    email varchar(60) unique not null, 
    `password` varchar(250) not null,
    telefono varchar(20) not null,
	nacionalidad varchar(50) not null,
	domicilio varchar(100) not null,
	rol enum('empleado','cliente') not null default 'cliente'
) engine = InnoDB auto_increment = 18 default charset = utf8mb4 collate = utf8mb4_unicode_ci; 

create table Categorias (
cod_categoria int primary key,
nom_categoria varchar(50) not null
) engine = InnoDB default charset = utf8mb4 collate = utf8mb4_unicode_ci; 


create table Productos (
cod_producto int primary key auto_increment, 
cod_categoria int not null,
foreign key (cod_categoria) references Categorias(cod_categoria),
tipo_producto varchar(80) not null,
nom_producto varchar(80) not null,
precio_unitario decimal(10,2) not null,
img_producto varchar(1000), 
stock_pro int not null, 
descripcion_pro varchar(100)
) engine = InnoDB default charset = utf8mb4 collate = utf8mb4_unicode_ci; 

-- Ingreso de datos --
insert into Usuarios values 
(16,'Cliente','Cliente','1990-01-01','cliente@example.com','scrypt:32768:8:1$f90GaPAMf0RaxmSa$79907cd31f13c5ffd644f197c4739b9291b6f5b3a148cfd45649797476c836352cd843bb28ec759b678f3625b9d56c0a436b13a478f08663754fcaab828bdba5','123456789','Argentino','Calle principal 123','cliente'),
(17,'Empleado','Empleado','1990-01-01','empleado@example.com','scrypt:32768:8:1$WtQYEvknXEIXA8OV$25da648bacd7bb868c59fba4cc7a5f7e64e7be0b1c5e3d636f069193562a62c2ad719732ba7fa527d5e50e825960959a28cc16579d76ea823584bb45221e745d','123456789','Argentino','Calle principal 123','empleado');

insert into Categorias values
(1,'Niños'),
(2, 'Mujeres'),
(3, 'Hombres'),
(4, 'Calzado');

insert into Productos (cod_producto, cod_categoria, tipo_producto, nom_producto, precio_unitario, img_producto, stock_pro, descripcion_pro) values
(1, 1, 'Conjunto', 'Conjunto verano', 10.50, '../static/img/niños-1.webp', 50, 'Remera manga cortas y pantalon corto, color verde'),
(2, 1, 'Buzo', 'Simple black', 15.75, '../static/img/niños-10.webp', 30, 'Buzo sin capucha, color negro'),
(3, 2, 'Buzo', 'Billabong', 15.75, '../static/img/abrigo5.png', 30, 'Buzo sin capucha, color verde'),
(4, 2, 'Pantalon', 'Cargo nueva temporada', 15.75, '../static/img/pantalon-6.png', 30, 'Pantalon cargo, color negro, mas vendido'),
(5, 3, 'Pantalon', 'Cargo con puños', 15.75, '../static/img/pantalon-3.webp', 30, 'Pantalon cargo, color verde'),
(6, 3, 'Remera', 'Musculosa verano 2024', 15.75, '../static/img/Remera2.png', 30, 'Remera ultimo verano, color blanca'),
(7, 4, 'Zapatillas', 'Vans high black', 15.75, '../static/img/zapatilla-11.jpg', 30, 'Zapatillas vans, altas tipo botita'),
(8, 4, 'Zapatillas', 'Vans deportivas', 15.75, '../static/img/zapatilla-1.jpg', 30, 'Zapatillas vans, color negro, ultimos talles')