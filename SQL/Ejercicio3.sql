/* Nivel de dificultad: Difícil */

/*1. Crea una tabla llamada "Productos" con las columnas: "id" (entero, clave
primaria), "nombre" (texto) y "precio" (numérico). */
CREATE TABLE IF NOT EXISTS public.productos (
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(255) NOT NULL,
	precio DECIMAL
);

/*2. Inserta al menos cinco registros en la tabla "Productos". */
INSERT INTO public.productos (nombre, precio) VALUES ('Camiseta', 9.99);
INSERT INTO public.productos (nombre, precio) VALUES ('Pantalón', 15);
INSERT INTO public.productos (nombre, precio) VALUES ('Abrigo', 55.5);
INSERT INTO public.productos (nombre, precio) VALUES ('Calcetines', 4);
INSERT INTO public.productos (nombre, precio) VALUES ('Maleta', 110.5);

/*3. Actualiza el precio de un producto en la tabla "Productos". */
UPDATE public.productos SET precio=17 where id=1;

/*4. Elimina un producto de la tabla "Productos". */
DELETE from public.productos WHERE id=2;

/*5. Realiza una consulta que muestre los nombres de los usuarios junto con los
nombres de los productos que han comprado (utiliza un INNER JOIN con la
tabla "Productos").*/
-- No tenemos una tabla en la que se almacenen los pedidos de los usuarios, la creamos:
CREATE TABLE IF NOT EXISTS public.pedidos (
	id SERIAL PRIMARY KEY,
	usuario_id INT NOT NULL,
	producto_id INT NOT NULL,
	cantidad INT NOT NULL,
	fecha DATE,
	CONSTRAINT FK_usuario_id FOREIGN KEY (usuario_id) REFERENCES public.usuarios(id),
	CONSTRAINT FK_producto_id FOREIGN KEY (producto_id) REFERENCES public.productos(id)
);

INSERT INTO public.pedidos(usuario_id, producto_id, cantidad, fecha) values (2, 3, 2, now());
INSERT INTO public.pedidos(usuario_id, producto_id, cantidad, fecha) values (2, 5, 1, now());
INSERT INTO public.pedidos(usuario_id, producto_id, cantidad, fecha) values (2, 1, 3, now());
INSERT INTO public.pedidos(usuario_id, producto_id, cantidad, fecha) values (2, 4, 2, now());

SELECT u.nombre, pr.nombre, pe.fecha,pe.cantidad FROM public.usuarios u
INNER JOIN public.pedidos pe on pe.usuario_id=u.id
INNER JOIN public.productos pr on pr.id=pe.producto_id;