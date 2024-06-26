import conexionBD
import modulo_restaurante
from datetime import datetime

 # Realización de reserva
def reserva():
    
    fecha = input("Ingrese fecha:  (DD-MM-AAAA)  ")
    fecha_formateada = datetime.strptime(fecha, '%d-%m-%Y').strftime('%Y-%m-%d') # transforma el formato de la para poder insertarla en la tabla

    hora = input("Ingrese la Hora:   (HH:MM) ")
    if len(hora) == 5: # le agrega el SS al formato hora
        hora += ":00"
    hora_formateada = datetime.strptime(hora, '%H:%M:%S').strftime('%H:%M:%S')  # transforma el formato de hora para poder insertarla en la tabla

    usuario_id = input("ingrese su ID de Uruario: ")

    modulo_restaurante.mostrar_restaurantes()
    restaurante_id = input("\n Por favor ingrese el id del restaurante que desea:  ")
    
    query = "INSERT INTO Reserva(fecha, hora, usuario_id, restaurante_id) VALUES (%s, %s, %s, %s)"
    values = (fecha_formateada, hora_formateada, usuario_id, restaurante_id)
    
    conexionBD.cursor.execute(query, values)
    conexionBD.conn.commit() # commit() para realizar cambios en la tabla 
    print(format("\n \033[1;32m"+"Reserva realizada con exito!" + "\033[0;m",'^50'))



 # Consulta de una reserva
def consulta_reserva(reserva_id):
    query = "select us.apellido, us.nombre,r.fecha, r.hora,  res.nombre as nombreRest, res.tipo_de_comida as tipoComida, res.calle as Direccion, res.numero from reserva r inner join usuarios us  on r.usuario_id = us.usuario_id inner join restaurante res on r.restaurante_id = res.restaurante_id WHERE reserva_id = %s"
    values = (reserva_id,)
    conexionBD.cursor.execute(query,values)
    reserva_Unica = conexionBD.cursor.fetchone()

    if(conexionBD.cursor.rowcount == 1):
        nombres_columnas = [descripcion[0] for descripcion in conexionBD.cursor.description] # para mostrar nombres de columnas
        formato = "{:<30}" * len(nombres_columnas) 
        formato = "{:<15} {:<15} {:<15} {:<15} {:<20} {:<15} {:<25} {:<15}"
        print(formato.format(*nombres_columnas))
        print("-" * 20 * len(nombres_columnas))
        
        fecha_formateada = reserva_Unica[2].strftime('%Y-%m-%d')
        tiempo_formateado = str(reserva_Unica[3])
        print(formato.format(reserva_Unica[0], reserva_Unica[1], fecha_formateada, tiempo_formateado, reserva_Unica[4], reserva_Unica[5], reserva_Unica[6], reserva_Unica[7]))
        return True
    else:
        print("No existe reserva con ese Id")
        return False


 # Muestra de reservas realizadas
def mostrar_reservas():
    query = "select us.apellido, us.nombre,r.fecha, r.hora,  res.nombre as nombreRest, res.tipo_de_comida as tipoComida, res.calle as Direccion, res.numero from reserva r inner join usuarios us  on r.usuario_id = us.usuario_id inner join restaurante res on r.restaurante_id = res.restaurante_id"
    conexionBD.cursor.execute(query)
    reservas = conexionBD.cursor.fetchall()

    nombres_columnas = [descripcion[0] for descripcion in conexionBD.cursor.description] # para mostrar nombres de columnas
    formato = "{:<30}" * len(nombres_columnas) 
    formato = "{:<15} {:<15} {:<15} {:<11} {:<16} {:<15} {:<30} {:<15}"
    
    print(formato.format(*nombres_columnas))
    print("-" * 20 * len(nombres_columnas))
    for reserva in reservas:
        fecha_formateada = reserva[2].strftime('%Y-%m-%d')
        tiempo_formateado = str(reserva[3])
        print(formato.format(reserva[0], reserva[1], fecha_formateada, tiempo_formateado, reserva[4], reserva[5], reserva[6], reserva[7]))


 # Modifica una reserva hecha
def modificar_reserva():
    reserva_id= input("\n Ingrese el id de la reserva a modificar: ")
    if (consulta_reserva(reserva_id)):
       
        fecha = input("Ingrese nueva fecha:  (DD-MM-AAAA)  ")
        fecha_formateada = datetime.strptime(fecha, '%d-%m-%Y').strftime('%Y-%m-%d') # transforma el formato de la para poder insertarla en la tabla

        hora = input("Ingrese la nueva Hora:   (HH:MM) ")
        if len(hora) == 5: # le agrega el SS al formato hora
            hora += ":00"
        hora_formateada = datetime.strptime(hora, '%H:%M:%S').strftime('%H:%M:%S')  # transforma el formato de hora para poder insertarla en la tabla

        usuario_id = input("ingrese su ID de Uruario: ")

        modulo_restaurante.mostrar_restaurantes()
        restaurante_id = input("\n Por favor ingrese el id del nuevo restaurante que desea:  ")

        query = "UPDATE Reserva SET fecha = %s, hora = %s, usuario_id = %s, restaurante_id = %s WHERE reserva_id= %s"
        values = (fecha_formateada, hora_formateada, usuario_id, restaurante_id, reserva_id)
        
        conexionBD.cursor.execute(query, values)
        conexionBD.conn.commit()
        print(format("\n \033[1;32m"+ "La reserva con id " + reserva_id + " se ha actualizado con éxito." + "\033[0;m",'^50'))
    else:
        print(f"El ID {reserva_id} NO EXISTE por lo tanto no se puede modificar ")
 
 
 # Elimina reserva ya cargada
def cancelar_reserva():
    while True:
        reserva_id = input("Ingrese el id de la reserva a eliminar: ")

        if(consulta_reserva(reserva_id)):
            query = "DELETE FROM Reserva WHERE reserva_id = %s"
            values = (reserva_id,)
        
            conexionBD.cursor.execute(query, values)
            conexionBD.conn.commit()
        
            print(format("\n \033[1;31m"+"La reserva con Id " + reserva_id + " ha sido eliminada con exito" + "\033[0;m",'^50'))
            return True
        else:
            print(f"La reserva con ID {reserva_id} NO EXISTE por lo tanto no puede ser eliminada.")




