from moduls.models import Cliente, Articulo, Bono
from moduls.prueba import *




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
            if not usuario_actual.select():
                return "Usuario o contraseña no válido."
            
            else:
                loggeado = True
                return usuario_actual
            




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



def listar_articulos(): # convertimos lo que nos devuelve la base de datos en una lista iterable de objetos tipo articulo
    lista_articulos = select_all_articulos() #selecciona todos los objetos
    lista_articulos_final =[]

    for articulo in lista_articulos:
        articulo_objeto = Articulo(articulo[1], articulo[2], articulo[3], articulo[0])
        lista_articulos_final.append(articulo_objeto)

    return lista_articulos_final

def listar_bonos(): # convertimos lo que nos devuelve la base de datos en una lista iterable de objetos tipo articulo
    lista_bonos = select_all_bonos() #selecciona todos los objetos
    lista_bonos_final =[]

    for bono in lista_bonos:
        bono_objeto = Bono(bono[0], bono[1], bono[2], bono[3])
        lista_bonos_final.append(bono_objeto)

    return lista_bonos_final

def seleccionar_bonos(lista_objetos_bono, usuario):
    codigo_introducido = input("Introduce el código (8 dígitos): ")
    bono_seleccionado = None

    for bono in lista_objetos_bono:
        if bono.codigo == codigo_introducido:
            bono_seleccionado = bono
            

    if bono_seleccionado == None:
        return "Código incorrecto"
    
    elif bono_seleccionado.estado == "D":
        return "Bono caducado"

    else:
        usuario.bono = bono_seleccionado
        return f"{usuario.bono}\nBono seleccionado"
