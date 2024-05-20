from bonos_db.iniciar_db import conexion


def iniciar_tabla():
    con = conexion()
    cursor = con.cursor()
    resultado = cursor.execute("select * from carritos;")
    if not resultado:
        cursor.execute("drop table if exists carritos;",
                       "create table carritos (id int primary key, lista_articulos varchar(500));") # Una lista de objetos en python     


def insertar_carrito(carrito):
    con = conexion()
    id = carrito.id
    lista_articulos = []

    for objeto in carrito.lista_articulos:
        lista_articulos.append(objeto.__str__)

    lista_art_imprimir = ",".join(lista_articulos)

    cursor = con.cursor()

    try:
        cursor.execute(f"insert into carritos values ({id}, {lista_art_imprimir});")
    except:
        return "Ha habido un error al añadir el carrito"
    
    return "Carrito añadido"


def update_carrito(carrito):
    con = conexion()
    id = carrito.id
    lista = []

    for objeto in carrito.lista_articulos:
        lista.append(objeto.__str__)

    lista_art_imprimir = ",".join(lista)

    cursor = con.cursor()
    cursor.execute(f"update table carritos set lista_articulos = {lista_art_imprimir} where carritos.id = {id};")



                       