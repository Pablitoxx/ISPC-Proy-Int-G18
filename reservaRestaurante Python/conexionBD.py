import mysql.connector

HOST = 'localhost'
USER = 'root'
PASSWORD = '1234'
BD = 'reserva_rest'

# Conectarse a la base de datos
conn = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    database=BD
)

# Crear un cursor
cursor = conn.cursor()

def cerrarConexion():
    cursor.close()
    conn.close()