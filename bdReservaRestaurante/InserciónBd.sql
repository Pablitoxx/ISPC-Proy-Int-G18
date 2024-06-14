USE reserva_rest;
 
 -- Inserción de datos en tabla Usuarios
INSERT INTO `usuarios` (usuario_id, email, contraseña, Nombre, Apellido, Telefono)
VALUES  (1,'pabblloocanno@gmail.com','pablo1','Pablo','Ocaño',2147483648),
		(2,'soledad.caudana@gmail.com','sole1','Soledad','Caudana',2147483649),
		(3,'fernandopajon06@gmail.com','fer1','Fernando','Pajon',2147483640),
		(4,'nachobressanini1@gmail.com','nacho1','Ignacio ','Bressanini',2147483641);
        
        
 -- Inserción de datos en tabla Restaurante
INSERT INTO restaurante (nombre, calle, numero, tipo_de_comida)
VALUES  ('Bohemia Mexican', 'Av Pueyrredon', 1345, 'Mexicana'),
		('Bohemia Chinese', 'Gral Paz', 72, 'China'),
        ('Bohemia Arabian', 'Av 24 de Septiebre', 791, 'Arabe'),
        ('Bohemia Burguer', 'Obispo Trejo', 1200, 'Hamburguesa'),
        ('Bohemia Italian', 'Av Colon', 2840, 'Italiana'),
        ('Bohemia Indian', 'Rondeu', 439, 'India'),
        ('Bohemia Grill', 'Rafael Nuñez', 3248, 'Parrilla'),
        ('Bohemia Fish & Shellfish', 'Sucre', 2504, 'Pescado y Marisco');
        
        
  -- Inserción de datos en tabla Mesa
INSERT INTO mesa (capacidad, disponibilidad, restaurante_id)
VALUES  (2, 1, 1), (4, 1, 1), (5, 1, 1), (6, 1, 1),
        (2, 1, 2), (4, 1, 2), (5, 1, 2), (6, 1, 2),
        (2, 1, 3), (4, 1, 3), (5, 1, 3), (6, 1, 3),
        (2, 1, 4), (4, 1, 4), (5, 1, 4), (6, 1, 4),
        (2, 1, 5), (4, 1, 5), (5, 1, 5), (6, 1, 5),
        (2, 1, 6), (4, 1, 6), (5, 1, 6), (6, 1, 6),
        (2, 1, 7), (4, 1, 7), (5, 1, 7), (6, 1, 7),
        (2, 1, 8), (4, 1, 8), (5, 1, 8), (6, 1, 8);
        
        
 -- Inserción de datos en tabla Reserva 
INSERT INTO reserva (reserva_id, fecha, hora, usuario_id, restaurante_id)
VALUES  (1,'2024-06-13','08:00:00',1,2),
		(2,'2024-06-13','09:00:00',2,3),
		(3,'2024-06-13','10:00:00',3,4),
		(4,'2024-06-13','11:00:00',4,5),
		(5,'2024-06-13','12:00:00',2,2),
		(6,'2024-06-13','13:00:00',3,4),
		(7,'2024-06-13','14:00:00',4,1),
		(8,'2024-06-13','15:00:00',1,3);


 