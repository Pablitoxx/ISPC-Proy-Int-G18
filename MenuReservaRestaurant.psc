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
FinAlgoritmo
