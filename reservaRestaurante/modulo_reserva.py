import conexionBD
import buscar_restaurante
from datetime import datetime

 # Realización de reserva
def reserva():
    
    fecha = input("Ingrese fecha:  (DD-MM-AAAA)  ")
    fecha_formateada = datetime.strptime(fecha, '%d-%m-%Y').strftime('%Y-%m-%d') # transforma el formato de la para poder insertarla en la tabla

    hora = input("Ingrese la Hora:   (HH:MM) ")
    if len(hora) == 5: # le agrega el SS al formato hora
        hora += ":00"
    hora_formateada = datetime.strptime(hora, '%H:%M:%S').strftime('%H:%M:%S')  # transforma el formato de hora para poder insertarla en la tabla

    usuario_id = input("ingrese su ID de Uruario: \n")

    buscar_restaurante.mostrar_restaurantes()
    restaurante_id = input("\n Por favor ingrese el id del restaurante que desea:  ")
    
    query = "INSERT INTO Reserva(fecha, hora, usuario_id, restaurante_id) VALUES (%s, %s, %s, %s)"
    values = (fecha_formateada, hora_formateada, usuario_id, restaurante_id)
    
    conexionBD.cursor.execute(query, values)
    conexionBD.conn.commit() # commit() para realizar cambios en la tabla 
    print(format("\n \033[1;32m"+"Reserva realizada con exito!" + "\033[0;m",'^50'))


def consulta_reserva():
    print ("Modulo consulta reserva")


def modific_reserva():
    print("Modulo de modificación de reserva")

def cancelar_reserva():
    print("Modulo de cancelación de reserva")




