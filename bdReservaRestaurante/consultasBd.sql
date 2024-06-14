
    
    -- Inserción en tabla restaurante 
INSERT INTO restaurante (nombre, calle, numero, tipo_de_comida)
VALUES  ('Bohemia Vegan', 'Av Patria', 1275, 'Vegana');

 
 
-- Cambio de atributo en tabla Restaurante 
UPDATE restaurante 
SET calle = 'Av del Trabajo'
WHERE restaurante_id = 9;


 -- Eliminación de una fila de la tabla Restaurante
DELETE FROM restaurante
WHERE restaurante_id= 9;


-- Selección de reservas con INNER JOIN
SELECT 
    r.reserva_id,
    us.apellido,
    us.nombre,
    r.fecha,
    r.hora,
    res.nombre,
    res.tipo_de_comida AS tipoComida,
    res.calle AS Direccion
FROM
    reserva r
        INNER JOIN
    usuarios us ON r.usuario_id = us.usuario_id
        INNER JOIN
    restaurante res ON r.restaurante_id = res.restaurante_id;
    

-- Consulta de mesas en distintos restauranates con inner
SELECT res.nombre, res.calle, res.numero, me.mesa_id as NumMesa, me.capacidad FROM restaurante res 
INNER JOIN mesa me ON res.restaurante_id = me.restaurante_id;



-- consulta de reserva unica con INNER JOIN y WHERE
SELECT r.reserva_id, us.apellido, us.nombre,r.fecha, r.hora, res.nombre, res.tipo_de_comida as tipoComida,
res.calle as Direccion, res.numero FROM reserva r 
INNER JOIN usuarios us  ON r.usuario_id = us.usuario_id 
INNER JOIN restaurante res ON r.restaurante_id = res.restaurante_id
WHERE r.reserva_id= 4;


select * from reserva;

