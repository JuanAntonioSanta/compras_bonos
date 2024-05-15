import mysql.connector

CONFIG = { # Configuramos los parámetros para la base de datos
    'host' : 'db',
    'port':'3306',
    'database':'bonos_db',
    'user' :'root',
    'password' :'admin'
    }

conexion = mysql.connector.connect(**CONFIG)


def select_all_articulos():
    cursor = conexion.cursor()
    resultado = cursor.execute("select * from articulos;")

    return resultado