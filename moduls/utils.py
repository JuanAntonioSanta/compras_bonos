from moduls.models import Cliente, Articulo
from moduls.bonos_db import select_all_articulos



def presentar_menu(menu):
    eleccion_correcta = False

    for opcion in menu:
        print(opcion)


    while not eleccion_correcta:
        eleccion = input("Introduzca una opción: ")
        
        try:
            int(eleccion)
            if 1 > eleccion > len(menu):
                return "Introduzca un número de las opciones."
            else:
                eleccion_correcta = True
                return eleccion
        except ValueError:
            return "Valor no válido"


def login(registrado = True):
    loggeado = False

    while not loggeado:
        name = input("Introduzca nombre de usuario: ")
        passwd = input("Introduzca contraseña: ")

        usuario_actual = Cliente(name, passwd)

        if not registrado:
            usuario_actual.insert()
            return usuario_actual
        
        else:
            if not usuario_actual.select(): #El usuario no existe, hay que crearlo
                return "Usuario o contraseña no válido."
            
            else:
                loggeado = True
                return usuario_actual
            

def listar_articulos(): # convertimos lo que nos devuelve la base de datos en una lista iterable de objetos tipo articulo
    lista_articulos = select_all_articulos() #selecciona todos los objetos
    lista_articulos_final =[]

    for articulo in lista_articulos:
        articulo = Articulo(nombre, descripcion, precio, id)
        lista_articulos_final.append(articulo)

    return lista_articulos_final


def presentar_articulos(lista_articulos, usuario):
    anyadir_otro = True

    while anyadir_otro:
        for articulo in lista_articulos:
            print(articulo)

        nombre_articulo = input("Introduce el nombre del artículo que quieras añadir: ")

        for articulo in lista_articulos:
            if articulo.nombre == nombre_articulo:
                usuario.carrito.add_articulo(articulo)

        if input("¿Quiere añadir otro? (s/n)") == "n":
            anyadir_otro = False


    