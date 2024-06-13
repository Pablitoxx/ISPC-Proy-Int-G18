import conexionBD

 # muestra los restos en pantalla para poder seleccionar el que se quiere en reserva
def mostrar_restaurantes():
    query = "SELECT * FROM Restaurante"
    conexionBD.cursor.execute(query)
    restos = conexionBD.cursor.fetchall()
    
    nombres_columnas = [descripcion[0] for descripcion in conexionBD.cursor.description] # muestra nombres de columnas
    formato = "{:<25}" * len(nombres_columnas) 

    print(formato.format(*nombres_columnas))
    print("-" * 25 * len(nombres_columnas))
    if restos:
        for resto in restos:
            print(formato.format(*resto))