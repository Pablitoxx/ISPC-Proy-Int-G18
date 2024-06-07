# ISPC-Proyecto Integrador-G18

| Integrantes          | DNI       | Email                         | Link Github personal                                   |
|----------------------|-----------|-------------------------------|--------------------------------------------------------|
| Ignacio Bressanini   | 42304213  | nachobressanini1@gmail.com    | https://github.com/NachoBressanini                     |
| Maria Soledad Caudana| 34218771  | soledad.caudana@gmail.com     | https://github.com/sole-caudana                        |
| Santiago Luesma      |           | luesma.dev@gmail.com          |                                                        |
| Pablo Ocaño          | 33222799  | pabblloocanno@gmail.com       | https://github.com/Pablitoxx                           |
| Fernando Pajon       | 34246659  | fernandopajon06@gmail.com     | https://github.com/FernandoPajon                                                       |

## Proyecto: 

App de reservas para restaurantes.

## Descripción:

Nuestro proyecto se trata de una innovadora app de reservas para restaurantes. Surge de la necesidad de modernizar y facilitar las gestiones, tanto para los clientes, como para los administradores. La idea es desarrollar una aplicación que permita a los clientes hacer reservas de manera eficiente, viendo la disponibilidad de mesas en tiempo real y crear, modificar o cancelar reservas y a los administradores les brindará herramientas para gestionar la disposición y disponibilidad de las mesas y controlar todas las reservas de manera centralizada, sencilla y efectiva. Creemos que es una aplicación que brindará comodidad y facilidad. Evitando esperas y asegurando la opción deseada. Mejorando la experiencia del cliente.

Funcionalidades:

1. Registro y Autenticación de Usuarios
Registro de Usuarios:
Los nuevos usuarios podrán crear una cuenta proporcionando su información básica, como nombre, correo electrónico y contraseña.
Se implementarán medidas de seguridad para proteger la información de los usuarios y verificar su identidad.
Inicio de Sesión: Los usuarios registrados pueden autenticarse en el sistema para acceder a sus reservas.

2. Gestión de Reservas:
Los usuarios podrán seleccionar la fecha y hora deseadas y reservar una mesa que se adapte a sus necesidades (cantidad de comensales).
Se ofrecerá una interfaz intuitiva que muestre la disponibilidad de mesas en tiempo real.
Modificación de Reservas: Los usuarios pueden cambiar la fecha, hora o cancelar una reserva existente.
Visualización de Disponibilidad: Ver la disponibilidad de mesas en tiempo real para las reservas.

3. Administración del Restaurante
Los administradores del restaurante podrán definir y ajustar la disposición de las mesas dentro del establecimiento. Podrán marcar mesas como disponibles o no disponibles según las necesidades del restaurante (por ejemplo, para eventos especiales).

## Análisis y Diseño del Proyecto: 
Algoritmo menu_reserva
	definir cant_comensales, codigo_reserva Como Entero
	definir fecha_reserva, hora_reserva, elim_reserva como cadena
	// pruebas de menu
	//codigo_reserva = 5
	//codigo = 5
	//fecha_reserva = "25/06/2024"
	//hora_reserva = "19:50"
	//cant_comensales = 6
	opcion_menu = 8
	
	escribir "Bienvenido"
	escribir "-------------------------------------"
	mientras opcion_menu < 1 o opcion_menu > 6 hacer
		escribir "Seleccione la opción que desee:"
		escribir "-------------------------------------"
		escribir "1- Reservar mesa"
		escribir "2- Consultar reserva"
		escribir "3- Modificar reserva"
		escribir "4- Eliminar reserva"
		escribir "5- Modificar datos Usuario"
		escribir "6- Salir"
		escribir "-------------------------------------"
		leer  opcion_menu
		Segun opcion_menu Hacer
			1:
				escribir "Reserva"
				escribir "-------------------------------------"
				escribir "Indique la fecha de reserva:  dd/mm/aaaa"
				leer fecha_reserva
				escribir "Indique la hora de reserva:  hh:mm"
				leer hora_reserva
				escribir "Indique el numero de comensales"
				leer cant_comensales
			2:
				escribir "Consulta tu reserva"
				escribir "-------------------------------------"
				escribir "Escriba el codigo de reserva"
				leer codigo_reserva
				si codigo_reserva = codigo Entonces
					escribir "Fecha Reserva: ", fecha_reserva
					escribir "Hora Reserva: ", hora_reserva
					escribir "Cantidad de comensales: ", cant_comensales
				SiNo
					escribir "Codigo inexistente o invalido"
				FinSi
			3:
				escribir "Modifica tu reserva"
				escribir "-------------------------------------"
				escribir "Escriba el codigo de reserva"
				leer codigo_reserva
				si codigo_reserva = codigo Entonces
					escribir "Indique la fecha de reserva:  dd/mm/aaaa"
					leer fecha_reserva
					escribir "Indique la hora de reserva:  hh:mm"
					leer hora_reserva
					escribir "Indique el numero de comensales"
					leer cant_comensales
				SiNo
					escribir "Codigo inexistente o invalido"
				FinSi
			4:
				escribir "Eliminar Reserva"
				escribir "-------------------------------------"
				escribir "Escriba el codigo de reserva"
				leer codigo_reserva
				si codigo_reserva = codigo Entonces
					Escribir "Esta seguro que desea eliminar su reserva:  si/no"
					leer elim_reserva
				SiNo
					escribir "Codigo inexistente o invalido"
				FinSi
				
			5:
				escribir "Modifica tus datos personales"
				escribir "-------------------------------------"
				
			6:
				escribir "Hasta luego"
		De Otro Modo:
			escribir "Por favor ingrese una opción valida"
			escribir "-------------------------------------"
		Fin Segun
	fin mientras
finalgoritmo


https://github.com/Pablitoxx/ISPC-Proy-Int-G18/blob/main/MenuReservaRestaurant.psc


Diagrama Entidad Relación (Notación de Chen. Convenciones vistas en la presentación utilizada en los contenidos del aula)

https://github.com/Pablitoxx/ISPC-Proy-Int-G18/assets/114536477/b3524bfe-40b1-4eec-8e30-a6795a868be3 


La aplicación está conformada por un menú principal (archivo [menú_inicio.py](https://github.com/Pablitoxx/ISPC-Proy-Int-G18/blob/main/reservaRestaurante/menu_inicio.py)), donde se puede seleccionar la opción que desea realizar el usuario. Cada opción tiene creada su función de modularización ([menú_reserva.py ](https://github.com/Pablitoxx/ISPC-Proy-Int-G18/blob/main/reservaRestaurante/menu_reserva.py) y [menú_usuario.py](https://github.com/Pablitoxx/ISPC-Proy-Int-G18/blob/main/reservaRestaurante/menu_usuario.py)) donde se realizaran todas las acciones que corresponden a la misma.

