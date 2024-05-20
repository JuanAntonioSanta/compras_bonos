from moduls.iniciar_db import iniciar_database

conexion = iniciar_database()

def iniciar_tabla():
    con = conexion()
    cursor = con.cursor()
    resultado = cursor.execute("select * from clientes;")
    if not resultado:
        cursor.execute("drop table if exists clientes;",
                       "create table clientes (nombre_usuario varchar(50) primary key, passwd varhcar(100));"
                       "insert into clientes values ('Mowgli', 'estoyTOloco');",
                       "insert into clientes values ('Balu', 'estaTOloco');")
                       
def insertar_cliente(cliente):
    con = conexion()
    cursor = con.cursor()
    cursor.execute(f"insert into clientes values ('{cliente.username}', '{cliente.passwd}');")

def seleccionar_usuario(cliente):
    con = conexion()
    cursor = con.cursor()
    resultado = cursor.execute(f"select * from clientes where nombre_usuario like '{cliente.username}' and passwd like '{cliente.passwd}';")
    return resultado