import mysql.connector
from time import sleep

conexion = None

CONFIG = { # Configuramos los parámetros para la base de datos
    'host' : 'db',
    'port':'3306',
    'database':'bonos_db',
    'user' :'root',
    'password' :'admin'
    }

while not conexion:
    try:
        conexion = mysql.connector.connect(**CONFIG)
        
    except:
        sleep(2)

def iniciar_database():
    
    iniciar_bonos()
    iniciar_car()
    iniciar_cli()
    iniciar_art()
    

######### ARTICULOS ############


def iniciar_art():
  
    cursor = conexion.cursor()

    try:
        resultado = cursor.execute("select * from articulos;")

    except:
        cursor.execute("drop table if exists articulos;")
        cursor.execute("create table articulos (id int primary key, nombre varchar(20), descripcion varchar(100), precio numeric(4,2));")
        cursor.execute("insert into articulos values (1, 'Manzana', 'Fruta del manzano', 2.50);")
        cursor.execute( "insert into articulos values (2, 'Banana', 'Fruta del banano', 1.99);")
        
    


def select_all_articulos():
    
    cursor = conexion.cursor()
    resultado = cursor.execute("select * from articulos;")

    return resultado


################ BONOS #######################

def iniciar_bonos():
   
    cursor = conexion.cursor()

    try:
        cursor.execute("select * from bonos;")

    except:
        cursor.execute("drop table if exists bonos;")
        cursor.execute("create table bonos (codigo char(8) primary key, fecha_caducidad date, descuento numeric(3,2), estado char(1));")
        cursor.execute("insert into bonos values ('11111111', '2024/08/25', 0.2, 'A');")

def select_all_bonos(conexion):
    con = conexion()
    cursor = con.cursor()

    resultado = cursor.execute("select * from bonos_db.bonos;")
    return resultado


############### CLIENTES #################

def iniciar_cli():

    cursor = conexion.cursor()
    try:
        resultado = cursor.execute("select * from clientes;")
    except:
        cursor.execute("drop table if exists clientes;")
        cursor.execute("create table clientes (nombre_usuario varchar(50) primary key, passwd varhcar(100));")
        cursor.execute("insert into clientes values ('Mowgli', 'estoyTOloco');")
        cursor.execute("insert into clientes values ('Balu', 'estaTOloco');")
                       
def insertar_cliente(cliente):

    cursor = conexion.cursor()
    cursor.execute(f"insert into clientes values ('{cliente.username}', '{cliente.passwd}');")

def seleccionar_usuario(cliente):

    cursor = conexion.cursor()
    resultado = cursor.execute(f"select * from clientes where nombre_usuario like '{cliente.username}' and passwd like '{cliente.passwd}';")
    return resultado


############## CARRITO ###################iniciar_tabla

def iniciar_car():
    cursor = conexion.cursor()

    try:
        resultado = cursor.execute("select * from carritos;")

    except:
        cursor.execute("drop table if exists carritos;")
        cursor.execute("create table carritos (id int primary key, lista_articulos varchar(500));") # Una lista de objetos en python     


def insertar_carrito(carrito):
    id = carrito.id
    lista_articulos = []

    for objeto in carrito.lista_articulos:
        lista_articulos.append(objeto.__str__)

    lista_art_imprimir = ",".join(lista_articulos)

    cursor = conexion.cursor()

    try:
        cursor.execute(f"insert into carritos values ({id}, {lista_art_imprimir});")
    except:
        return "Ha habido un error al añadir el carrito"
    
    return "Carrito añadido"


def update_carrito(carrito):
    id = carrito.id
    lista = []

    for objeto in carrito.lista_articulos:
        lista.append(objeto.__str__)

    lista_art_imprimir = ",".join(lista)

    cursor = conexion.cursor()
    cursor.execute(f"update table carritos set lista_articulos = {lista_art_imprimir} where carritos.id = {id};")

