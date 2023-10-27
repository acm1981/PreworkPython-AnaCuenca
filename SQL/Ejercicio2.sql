/* Nivel de dificultad: Fácil*/
/* 1. Crea una base de datos llamada "MiBaseDeDatos". */
CREATE DATABASE MiBaseDeDatos;

/* 2. Crea una tabla llamada "Usuarios" con las columnas: "id" (entero, clave
primaria), "nombre" (texto) y "edad" (entero). */
CREATE TABLE IF NOT EXISTS public.Usuarios (
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(255) NOT NULL,
	edad INT
);

/* 3. Inserta dos registros en la tabla "Usuarios".*/
INSERT INTO public.Usuarios (nombre, edad) VALUES ('Ana', 42);
INSERT INTO public.Usuarios (nombre, edad) VALUES ('Fernando', 75);

/* 4. Actualiza la edad de un usuario en la tabla "Usuarios".*/
UPDATE public.Usuarios SET edad=57 where id=2;

/* 5. Elimina un usuario de la tabla "Usuarios". */
DELETE FROM public.Usuarios WHERE id=1;

/* Nivel de dificultad: Moderado */
/* 1. Crea una tabla llamada "Ciudades" con las columnas: "id" (entero, clave
primaria), "nombre" (texto) y "pais" (texto).*/
CREATE TABLE IF NOT EXISTS public.Ciudades (
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(255) NOT NULL,
	pais VARCHAR(255)
);

/* 2. Inserta al menos tres registros en la tabla "Ciudades".*/
INSERT INTO public.Ciudades (nombre, pais) VALUES ('Madrid', 'España');
INSERT INTO public.Ciudades (nombre, pais) VALUES ('Paris', 'Francia');
INSERT INTO public.Ciudades (nombre, pais) VALUES ('Bilbao', 'España');
INSERT INTO public.Ciudades (nombre, pais) VALUES ('Desconocido', 'Desconocido');

/* 3. Crea una foreign key en la tabla "Usuarios" que se relacione con la columna "id"
de la tabla "Ciudades".*/
ALTER TABLE public.usuarios
ADD COLUMN ciudad_id INT DEFAULT 4 NOT NULL;

ALTER TABLE public.Usuarios
ADD CONSTRAINT FK_Usuarios_id FOREIGN KEY (ciudad_id) REFERENCES public.Ciudades(id);

/* 4. Realiza una consulta que muestre los nombres de los usuarios junto con el
nombre de su ciudad y país (utiliza un LEFT JOIN).*/
SELECT u.nombre, c.nombre ciudad, c.pais FROM public.usuarios u
LEFT JOIN public.ciudades c on u.ciudad_id=c.id;

/* 5. Realiza una consulta que muestre solo los usuarios que tienen una ciudad
asociada (utiliza un INNER JOIN). */
SELECT u.* FROM public.usuarios u
INNER JOIN public.ciudades c on u.ciudad_id=c.id;
