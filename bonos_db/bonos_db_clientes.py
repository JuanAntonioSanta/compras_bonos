import mysql.connector

CONFIG = { # Configuramos los parámetros para la base de datos
    'host' : 'db',
    'port':'3306',
    'database':'bonos_db',
    'user' :'root',
    'password' :'admin'
    }

conexion = mysql.connector.connect(**CONFIG)


def iniciar_tabla():
    cursor = conexion.cursor()
    resultado = cursor.execute("select * from clientes;")
    if not resultado:
        cursor.execute("drop table if exists clientes;",
                       "create table clientes (nombre_usuario varchar(50) primary key, passwd varhcar(100));"
                       "insert into clientes values ('Mowgli', 'estoyTOloco');",
                       "insert into clientes values ('Balu', 'estaTOloco');")
                       