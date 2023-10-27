/* 1. Crea una tabla llamada "Pedidos" con las columnas: "id" (entero, clave
primaria), "id_usuario" (entero, clave foránea de la tabla "Usuarios") y
"id_producto" (entero, clave foránea de la tabla "Productos"). */
DROP TABLE public.pedidos;
CREATE TABLE IF NOT EXISTS public.pedidos (
	id SERIAL PRIMARY KEY,
	id_usuario INT NOT NULL,
	id_producto INT NOT NULL,
	CONSTRAINT FK_id_usuario FOREIGN KEY (id_usuario) REFERENCES public.usuarios(id),
	CONSTRAINT FK_producto_id FOREIGN KEY (id_producto) REFERENCES public.productos(id)
);

/* 2. Inserta al menos tres registros en la tabla "Pedidos" que relacionen usuarios con
productos. */
INSERT INTO public.pedidos(id_usuario, id_producto) values (2, 3);
INSERT INTO public.pedidos(id_usuario, id_producto) values (2, 1);
INSERT INTO public.pedidos(id_usuario, id_producto) values (2, 4);


/*3. Realiza una consulta que muestre los nombres de los usuarios y los nombres de
los productos que han comprado, incluidos aquellos que no han realizado
ningún pedido (utiliza LEFT JOIN y COALESCE).*/
INSERT INTO public.usuarios(nombre, edad, ciudad_id) values ('Jose',29, 1);

SELECT u.nombre, COALESCE(pr.nombre ,'') producto FROM public.usuarios u
LEFT JOIN public.pedidos pe on pe.id_usuario=u.id
LEFT JOIN public.productos pr on pr.id=pe.id_producto;

/*4. Realiza una consulta que muestre los nombres de los usuarios que han
realizado un pedido, pero también los que no han realizado ningún pedido
(utiliza LEFT JOIN).
*/
SELECT u.nombre, CASE WHEN count(pe.id)=0 then 'No ha realizado pedidos' else 'Ha realizado '||  count(pe.id) ||' pedidos' end producto FROM public.usuarios u
LEFT JOIN public.pedidos pe on pe.id_usuario=u.id
LEFT JOIN public.productos pr on pr.id=pe.id_producto
group by u.nombre;

/*5. Agrega una nueva columna llamada "cantidad" a la tabla "Pedidos" y actualiza
los registros existentes con un valor (utiliza ALTER TABLE y UPDATE)
*/
ALTER TABLE public.pedidos 
ADD COLUMN cantidad INT;

UPDATE public.pedidos set cantidad=1;