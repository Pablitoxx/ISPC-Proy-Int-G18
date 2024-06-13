import conexionBD

 # muestra los restos en pantalla para poder seleccionar el que se quiere en reserva
def mostrar_restaurantes():
    query = "SELECT * FROM Restaurante"
    conexionBD.cursor.execute(query)
    restos = conexionBD.cursor.fetchall()
    
    if restos:
        for resto in restos:
            print(resto)