import mysql.connector
from time import sleep
from bonos_db.bonos_db_articulos import iniciar_tabla as iniciar_art
from bonos_db.bonos_db_carritos import iniciar_tabla as iniciar_car
from bonos_db.bonos_db_clientes import iniciar_tabla as iniciar_cli
from bonos_db.bonos_db_bonos import iniciar_tabla as iniciar_bonos

conexion = None

def iniciar_database():
    CONFIG = { # Configuramos los parámetros para la base de datos
    'host' : 'db',
    'port':'3306',
    'database':'bonos_db',
    'user' :'santa',
    'password' :'admin'
    }

    conexion = conexion(CONFIG)

    iniciar_bonos(conexion)
    iniciar_car(conexion)
    iniciar_cli(conexion)
    iniciar_art(conexion)

def conexion(CONFIG):

    if not conexion:
        while not conexion:
            try:
                conexion = mysql.connector.connect(**CONFIG)
            except:
                sleep(2)

        return conexion
    else:
        return conexion
    




