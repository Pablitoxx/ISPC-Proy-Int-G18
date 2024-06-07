# Se importan modulos de funciones para poder utilizarlas
import menu_reserva
import menu_usuario
# Menu de opciones para seleccionar
while True:  
     print("-" * 40)                                      #menu_opcion < 1 or menu_opcion > 6:
     print(format("\033[3;35m"+"Bienvenido a Bohemia" + "\033[0;m",'=^50'))
     print("-" * 40)  
     print("Seleccione la opcion que desee: \n")
     print("1- Reservar mesa")
     print("2- Consultar reserva")
     print("3- Modificar reserva")
     print("4- Cancelar reserva")
     print("5- Modificar datos Usuario")
     print("6- Salir")
     print("-" * 40)
     menu_opcion= (input("Escribe la opción que desea escoger: "))
     print("-" * 40)

# El match funciona como un case when, de acuerdo a la opcion seleccionada realiza una acción
     match menu_opcion:
        case "1":
            print( format("Realizar reserva \n",'^40'))
            reserva= menu_reserva.reserva()
        case "2":
            print(format("Consulta tu reserva \n",'^40'))
            cod_res= int (input("Ingrese el codigo de reserva:  "))
            consulta_res= menu_reserva.consulta_reserva()
        case "3":
            print(format("Modifica tu reserva \n",'^40'))
            cod_res= int (input("Ingrese el codigo de reserva:  "))
            mod_reserva= menu_reserva.modific_reserva()
        case "4":
            print(format("Cancelar reserva \n",'^40'))
            cod_res= int (input("Ingrese el codigo de reserva que desea cancelar:  "))
            menu_reserva.cancelar_reserva()
        case "5":
             print(format("Modificar datos de usuario \n",'^40'))
             nomb_usuario= input("Ingrese el nombre del usuario a modificar:")
             mod_usurio= menu_usuario.modific_usuario()
        case "6":
             print(format("\033[1;32m"+"Hasta pronto!" + "\033[0;m",'^50'))
             break
        case _:
             print("\033[1;31m"+"Por favor ingrese una opción valida" + "\033[0;m")