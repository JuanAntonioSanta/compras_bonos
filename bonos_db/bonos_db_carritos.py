import mysql.connector
from moduls.models import Carrito

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
    resultado = cursor.execute("select * from carritos;")
    if not resultado:
        cursor.execute("drop table if exists carritos;",
                       "create table carritos (id int primary key, lista_articulos varchar(500));") # Una lista de objetos en python
        
def insertar_carrito(carrito):
    id = carrito.id
    lista_articulos = []
    for objeto in carrito.lista:
        lista_articulos.append(objeto.__str__)

    lista_art_imprimir = ",".join(lista_articulos)

    cursor = conexion.cursor()

    try:
        cursor.execute(f"insert into carritos values ({id}, {lista_art_imprimir})")
    except:
        return "Ha habido un error al añadir el carrito"
    
    return "Carrito añadido"


                       