/*1. Crear una tabla llamada "Clientes" con las columnas: id (entero, clave primaria),
nombre (texto) y email (texto).*/
CREATE TABLE IF NOT EXISTS public.clientes (
	id	SERIAL PRIMARY KEY,
	nombre varchar(255) NOT NULL,
	email varchar(255)
);

/*2. Insertar un nuevo cliente en la tabla "Clientes" con id=1, nombre="Juan" y
email="juan@example.com".*/
INSERT INTO public.clientes (nombre, email) values ('Juan', 'juan@example.com');

/* 3. Actualizar el email del cliente con id=1 a "juan@gmail.com". */
UPDATE public.clientes SET email='juan@gmail.com' WHERE id=1;

/* 4. Eliminar el cliente con id=1 de la tabla "Clientes". */
DELETE FROM public.clientes WHERE id=1;

/*5. Crear una tabla llamada "Pedidos" con las columnas: id (entero, clave primaria),
cliente_id (entero, clave externa referenciando a la tabla "Clientes"), producto (texto) y cantidad (entero).*/
CREATE TABLE IF NOT EXISTS public.pedidos (
	id	SERIAL PRIMARY KEY,
	cliente_id INT NOT NULL,
	producto varchar(255),
	cantidad INT,
	CONSTRAINT FK_cliente_id_pedidos FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

/*6. Insertar un nuevo pedido en la tabla "Pedidos" con id=1, cliente_id=1,
producto="Camiseta" y cantidad=2. */
INSERT INTO public.pedidos (cliente_id, producto, cantidad) VALUES (1,'Camiseta',2);

/* 7. Actualizar la cantidad del pedido con id=1 a 3. */
UPDATE public.pedidos SET cantidad=3 where id=1;

/* 8. Eliminar el pedido con id=1 de la tabla "Pedidos". */
DELETE from public.pedidos where id=1;

/* 9. Crear una tabla llamada "Productos" con las columnas: id (entero, clave primaria), nombre (texto) y precio (decimal). */
CREATE TABLE IF NOT EXISTS public.productos (
	id	SERIAL PRIMARY KEY,
	nombre varchar(255),
	precio DECIMAL
);

/* 10. Insertar varios productos en la tabla "Productos" con diferentes valores. */
insert into public.productos(nombre, precio) values ('Camiseta', 9.99);
insert into public.productos(nombre, precio) values ('Pantalón', 25);
insert into public.productos(nombre, precio) values ('Guantes', 12);
insert into public.productos(nombre, precio) values ('Calcetines', 3.95);
insert into public.productos(nombre, precio) values ('Abrigo', 55.5);

/* 11. Consultar todos los clientes de la tabla "Clientes".*/
select * from public.clientes;

/*2. Consultar todos los pedidos de la tabla "Pedidos" junto con los nombres de los clientes correspondientes. */
select p.* , c.nombre from public.pedidos p
left join public.clientes c on p.cliente_id=c.id;

/* 13. Consultar los productos de la tabla "Productos" cuyo precio sea mayor a $50. */
select * from public.productos p where p.precio>50;

/* 14.Consultar los pedidos de la tabla "Pedidos" que tengan una cantidad mayor o igual a 5. */
select * from public.pedidos p where p.cantidad>=5;

/* 15. Consultar los clientes de la tabla "Clientes" cuyo nombre empiece con la letra "A". */
select * from public.clientes c where nombre ILIKE 'A%';

/* 16. Realizar una consulta que muestre el nombre del cliente y el total de pedidos realizados por cada cliente. */
select c.nombre, sum(COALESCE(p.cantidad,0)) from public.clientes c
left join public.pedidos p on c.id=p.cliente_id
group by c.nombre;

/* 17. Realizar una consulta que muestre el nombre del producto y la cantidad total de pedidos de ese producto. */
select p.producto , SUM(COALESCE(p.cantidad,0)) from public.pedidos p
group by p.producto;

/* 18. Agregar una columna llamada "fecha" a la tabla "Pedidos" de tipo fecha. */
ALTER TABLE public.pedidos
ADD COLUMN fecha DATE;

/* 19. Agregar una clave externa a la tabla "Pedidos" que haga referencia a la tabla "Productos" en la columna "producto". */
ALTER TABLE public.productos
ADD CONSTRAINT AK_nombre UNIQUE(nombre);

ALTER TABLE public.pedidos 
ADD CONSTRAINT FK_producto_id FOREIGN KEY(producto) REFERENCES public.productos(nombre);

/* 20. Realizar una consulta que muestre los nombres de los clientes, los nombres de los productos y las cantidades de los pedidos donde coincida la clave externa. */
SELECT c.nombre, p.producto, p.cantidad from public.clientes c
inner join public.pedidos p on c.id=p.cliente_id;
