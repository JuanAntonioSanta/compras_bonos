from moduls.iniciar_db import iniciar_database

conexion = iniciar_database()


def iniciar_tabla():
    con = conexion()
    cursor = con.cursor()

    resultado = cursor.execute("select * from articulos;")

    if not resultado:
        cursor.execute("drop table if exists articulos;",
                       "create table articulos (id int primary key, nombre varchar(20), descripcion varchar(100), precio numeric(4,2));"
                       "insert into articulos values (1, 'Manzana', 'Fruta del manzano', 2.50);",
                       "insert into articulos values (2, 'Banana', 'Fruta del banano', 1.99);",
                       "insert into articulos values (3, 'Miel', 'Natural del chino', 5.20);",
                       "insert into articulos values (4, 'Mostaza', 'No sabia que poner', 0.99);")
        
    


def select_all_articulos():
    con = conexion()
    cursor = con.cursor()
    resultado = cursor.execute("select * from articulos;")

    return resultado