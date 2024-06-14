import conexionBD

 # Registro de usuario nuevo
def registro_usuario():
    email = input("Ingrese su correo electronico: ")
    password = input("Ingrese una contraseña: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Teléfono: ")
    
    query = "INSERT INTO Usuarios (email, contraseña, Nombre, Apellido, telefono) VALUES (%s, %s, %s, %s, %s)"
    values = (email, password, nombre, apellido, telefono)
    
    conexionBD.cursor.execute(query, values)
    conexionBD.conn.commit() #Es necesario realizar el commit(); de lo contrario, no se realizan cambios en la tabla 
    print("Usuario creado con exito")


 # Ingreso del usuario a la app
def ingreso_usuario():
    while True:
        email = input("Por favor ingrese su correo electronico: ")
        password = input("Ingrese su contraseña: ")
        query = "SELECT * FROM Usuarios WHERE email = %s and contraseña = %s "
        values = (email,password)
        conexionBD.cursor.execute(query,values)
        usuario_Unico = conexionBD.cursor.fetchone()

        if(conexionBD.cursor.rowcount == 1):
            print ("\n Su Id de usuario es: ",usuario_Unico[0])
            return True
        else:
            print(f"\n email o contrasaeña incorrectos")


 # Modifica los datos de usuario
def modificar_usuario():
    usuario_id= input("Ingrese el id del usuario a modificar: ")
    if (buscar_usuario(usuario_id)):
        password = input("Ingrese su nueva contraseña: ")
        nombre = input("ingrese su nuevo nombre: ")
        apellido = input("Ingrese su nuevo apellido: ")
        telefono = input("Ingrese su nuevo teléfono: ")

        query = "UPDATE Usuarios SET contraseña = %s, nombre = %s, apellido = %s, telefono = %s WHERE usuario_id =%s  "
        values = (password, nombre, apellido, telefono, usuario_id)
        
        conexionBD.cursor.execute(query, values)
        conexionBD.conn.commit()
        print(format("\n \033[1;32m"+ nombre + " tus datos se han actualizado con éxito." + "\033[0;m",'^50'))
    else:
        print(f"El ID {usuario_id} NO EXISTE por lo tanto no se puede modificar ")


 # Elimina usuario existente (solo los que no tienen ninguna reserva realizada)
def eliminar_usuario():
    while True:
        usuario_id = input("Ingrese el id del usuario a eliminar: ")

        if(buscar_usuario(usuario_id)):
            query = "DELETE FROM Usuarios WHERE usuario_id = %s"
            values = (usuario_id,)
        
            conexionBD.cursor.execute(query, values)
            conexionBD.conn.commit()
        
            print(format("\n \033[1;31m"+"El usuario con Id " + usuario_id + " ha sido eliminado con exito" + "\033[0;m",'^50'))
            return True
        else:
            print(f"Persona con ID {usuario_id} NO EXISTE por lo tanto no puede ser eliminada.")


 # Busqueda un usuario por su id 
def buscar_usuario(usuario_id):
    query = "SELECT * FROM Usuarios WHERE usuario_id = %s"
    values = (usuario_id,)
    conexionBD.cursor.execute(query,values)
    usuario_Unico = conexionBD.cursor.fetchone()

    if(conexionBD.cursor.rowcount == 1):
        print(usuario_Unico)
        return True
    else:
        print("Usuario inexistente")
        return False


# Muestra los usuarios registrados
def mostrar_usuarios():
    query = "SELECT * FROM Usuarios"
    conexionBD.cursor.execute(query)
    usuarios = conexionBD.cursor.fetchall()

    nombres_columnas = [descripcion[0] for descripcion in conexionBD.cursor.description] # muestra nombres de columnas
    formato = "{:<30}" * len(nombres_columnas) 

    print(formato.format(*nombres_columnas))
    print("-" * 27 * len(nombres_columnas))
    if usuarios:
        for usuario in usuarios:
            print(formato.format(*usuario))
            