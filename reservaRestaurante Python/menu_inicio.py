# Se importan modulos de funciones y la DB para poder utilizarlas
import modulo_reserva
import modulo_usuario
import mysql.connector

 # menu registro y login de usuario
while True:
    print ("Bienvenido")
    ingreso_usuario = input("¿Esta usted registrado?  si/no: ")
    if ingreso_usuario == "no":
        modulo_usuario.registro_usuario()
    elif ingreso_usuario == "si":
        modulo_usuario.ingreso_usuario()

 # Menu de opciones para seleccionar
    while True:  
        print("-" * 40)                                     
        print(format("\033[3;35m"+"Bienvenido a Bohemia" + "\033[0;m",'=^50'))
        print("-" * 40)  
        print("Seleccione la opcion que desee: \n")
        print("1- Reservar mesa")
        print("2- Consultar reserva")
        print("3- Mostrar reservas")
        print("4- Modificar reserva")
        print("5- Cancelar reserva")
        print("6- Modificar datos Usuario")
        print("7- Eliminar Usuario que no tenga reserva")
        print("8- Mostrar Usuarios")
        print("9- Salir")
        print("-" * 40)
        menu_opcion= (input("Escribe la opción que desea escoger: "))
        print("-" * 40)

# El match funciona como un case when, de acuerdo a la opcion seleccionada realiza una acción
        match menu_opcion:
            case "1":
                print( format("Realizar reserva \n",'^40'))
                modulo_reserva.reserva()
            case "2":
                print(format("Consulta tu reserva \n",'^40'))
                consulta_reserva= int (input("Ingrese el codigo de reserva:  "))
                modulo_reserva.consulta_reserva(consulta_reserva)
            case "3":
                print(format("Mostrar reservas \n",'^40'))
                modulo_reserva.mostrar_reservas()
            case "4":
                print(format("Modifica tu reserva \n",'^40'))
                mod_reserva= modulo_reserva.modificar_reserva()
            case "5":
                print(format("Cancelar reserva \n",'^40'))
                modulo_reserva.cancelar_reserva()
            case "6":
                print(format("Modificar datos de usuario \n",'^40'))
                modulo_usuario.modificar_usuario()
            case "7":
                print(format("Eliminar usuario que aun no tenga reserva\n",'^40'))
                modulo_usuario.eliminar_usuario()
            case "8":
                print(format("Mostrar usuarios registrados \n",'^40'))
                modulo_usuario.mostrar_usuarios()
            case "9":
                print(format("\033[1;32m"+"Hasta pronto!" + "\033[0;m",'^50'))
                break
            case _:
                print("\033[1;31m"+"Por favor ingrese una opción valida" + "\033[0;m")
