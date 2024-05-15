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
    resultado = cursor.execute("select * from articulos;")
    if not resultado:
        cursor.execute("drop table if exists articulos;",
                       "create table articulos (id int primary key, nombre varchar(20), descripcion varchar(100), precio numeric(4,2));"
                       "insert into articulos values (1, 'Manzana', 'Fruta del manzano', 2.50);",
                       "insert into articulos values (2, 'Banana', 'Fruta del banano', 1.99);",
                       "insert into articulos values (3, 'Miel', 'Natural del chino', 5.20);",
                       "insert into articulos values (4, 'Mostaza', 'No sabia que poner', 0.99);")
        
    


def select_all_articulos():
    cursor = conexion.cursor()
    resultado = cursor.execute("select * from articulos;")

    return resultado