drop database if exists catering;
create database catering; 

use catering; 

create table persona(
	dni int, 
    primer_nombre varchar(20),
    segundo_nombre varchar(20),
    apellido_paterno varchar(20),
    apellido_materno varchar(20),
    correo varchar(50),
    telefono integer,
    primary key (dni)
);

create table cliente (
	dni int,
    departamento varchar(20),
    ciudad varchar(20),
    notas_adicionales varchar(100),
    primary key (dni)	
);

create table empleado (
	dni int, 
    fecha_contratacion date,
	puesto varchar(20),
    direccion varchar(50),
    salario int, 
    id_evento int,
    primary key (dni)
);

create table horario_trabajo(
	id_horario int, 
    horario_inicio time, 
    horario_fin time,
    fecha date, 
    dni_empleado int,
    primary key(id_horario)
);

create table feedback_cliente (
	id_feedback int ,
    comentario varchar(100),
    calificacion char(1),
    fecha_feedback date,
    dni_cliente int,
    primary key (id_feedback)
);

create table factura(
	id_factura int, 
    fecha_emision datetime, 
    metodo_pago varchar(20),
    monto_total int,
    id_pedido int,
    dni_cliente int,
    primary key(id_factura)
);

create table pedido (
	id_pedido int, 
    fecha_pedido datetime,
    precio_total int, 
    cantidad_personas int,
    id_evento int,
    primary key (id_pedido)
);

create table evento(
	id_evento int, 
    nombre_evento varchar(80),
    fecha_evento date,
	hora_inicio time,
    hora_fin time, 
    tipo_evento varchar(40),
    ubicacion_evento varchar(50),
    dni_cliente int,
    primary key (id_evento)
);

create table tipo_contratacion(
	id_tipo_contratacion int, 
    cantidad int,
    fecha_reserva date, 
    tipo_servicio varchar(20),
    id_evento int,
    primary key(id_tipo_contratacion)
);

create table menu(
	id_menu int, 
    precio_persona int, 
    nombre_menu varchar(30),
    id_evento int,
    primary key (id_menu)
);

create table ingredientes(
	id_ingrediente int, 
    precio_unidad decimal(5,2), 
    unidad_medida varchar(20),
    cantidad_requerida int, 
    nombre_ingrediente varchar(20),
    id_menu int,
    id_proveedor int,
    primary key(id_ingrediente)
);

create table proveedor(
	id_proveedor int, 
    nombre_proveedor varchar(50),
    telefono int, 
    correo varchar(50),
    cantidad_disponible int, 
    direccion varchar(50),
    departamento varchar(20),
    ciudad varchar(20),
    primary key(id_proveedor)
);
alter table proveedor drop column cantidad_disponible;
create table inventario(
	id_inventario int, 
    nombre_producto varchar(20),
    cantidad_disponible int, 
    unidad_medida varchar(20), 
    precio_unidad int, 
    id_proveedor int,
    primary key (id_inventario)
);

-- LLAVES FORANEAS 

alter table cliente add foreign key (dni) references persona(dni);
alter table empleado add foreign key (dni) references persona(dni);
alter table empleado add foreign key(id_evento) references evento(id_evento);
alter table horario_trabajo add foreign key (dni_empleado) references empleado (dni);
alter table feedback_cliente  add foreign key (dni_cliente) references cliente(dni);
alter table factura add foreign key (dni_cliente) references cliente(dni);
alter table factura add foreign key (id_pedido) references pedido(id_pedido);
alter table pedido add foreign key (id_evento) references evento(id_evento);
alter table evento add foreign key (dni_cliente) references cliente(dni);
alter table tipo_contratacion add foreign key (id_evento) references evento(id_evento);
alter table menu add foreign key (id_evento) references evento(id_evento);
alter table ingredientes add foreign key (id_menu) references menu(id_menu);
alter table ingredientes add foreign key (id_proveedor) references proveedor(id_proveedor);
alter table inventario add foreign key (id_proveedor) references proveedor(id_proveedor);


-- INSERTANDO VALORES 
-- 1)
insert into persona (dni,primer_nombre,segundo_nombre,apellido_paterno,apellido_materno,correo,telefono) 
values 
	(74863840,'kerin','sebastian','larico','huillca','y_4_1_0@hotmail.com',988860462),
    (29614137,'marco','sandro','sifuentes','lopez','tdcoatibb@gmail.com',965822374);
select * from persona;

-- 2)
insert into cliente(dni,departamento,ciudad,notas_adicionales) 
values 
	(74863840,'arequipa','arequipa','solo pido que sean puntuales nada mas gracias');
select * from cliente ;

-- 3)
insert into feedback_cliente(id_feedback,comentario,calificacion,fecha_feedback,dni_cliente)
values
	(100,'el servicio fue estupendo, la comida estaba buena y fueron puntuales',5,'2023-09-22',74863840);
select * from feedback_cliente;

-- 4)
insert into evento(id_evento, nombre_evento, fecha_evento, hora_inicio, hora_fin, tipo_evento, ubicacion_evento, dni_cliente)
values 
	(200,'boda de miguel y maria','2024-09-28','19:00:00','03:00:00','boda','av dolores 123',74863840);
select * from evento;

-- 5)
insert into empleado(dni,fecha_contratacion,puesto,direccion,salario,id_evento)
values 
	(29614137,'2024-05-01','mozo','av bolognesi 1003',2000,200);
select * from empleado;

-- 6)
insert into horario_trabajo(id_horario,horario_inicio,horario_fin,fecha,dni_empleado)
values 
	(300,'19:00:00','03:00:00','2024-09-28',29614137);
    
-- 7) 
insert into tipo_contratacion(id_tipo_contratacion,cantidad,fecha_reserva,tipo_servicio,id_evento)
values 
	(400,2,'2024-03-01','movilidad',200);
select * from tipo_contratacion;

-- 8)
insert into menu(id_menu, precio_persona, nombre_menu,id_evento)
values 
	(500,40,'sabor peruano',200);
select * from menu;

-- 9)
insert into ingredientes(id_ingrediente, precio_unidad, unidad_medida, cantidad_requerida, nombre_ingrediente, id_menu)
values 
	(600,03.50,'kilogramos',20,'cebolla',500);
select * from ingredientes;

-- 10)
insert into pedido(id_pedido, fecha_pedido, precio_total, cantidad_personas, id_evento)
values 
	(700, '2024-09-28',800,20,200);
select * from pedido;

-- 11) 
insert into proveedor(id_proveedor, nombre_proveedor, telefono, correo, direccion, departamento, ciudad)
values 
	(800,'Sabores Andinos Distribuciones Gastronómicas',973154648,'sabores.andinos.distribuciones@gmail.com','los incas 220','arequipa','arequipa');
select * from proveedor;

-- 12) 
insert into inventario(id_inventario, nombre_producto, cantidad_disponible, unidad_medida, precio_unidad, id_proveedor)
values 
	(900,'cebolla', 120,'kilogramos',03.50,800);
select * from inventario; 

-- 13) 
insert into factura(id_factura, fecha_emision, metodo_pago, monto_total, id_pedido, dni_cliente)
values	
	(1000, '2024-09-28', 'tarjeta de credito', 800, 700, 74863840);
select * from factura;