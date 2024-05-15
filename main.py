from moduls.models import *
from moduls.utils import *

PRECIO_MINIMO = 50

finalizar = False
eleccion = None
usuario = None
lista_objetos = listar_articulos()



menu_usuario = [
    "1. Login",
    "2. Crear usuario"
]

menu_compra = [
    "1. Añadir artículos",
    "2. Añadir Bono",
    "3. Salir"
]





while not finalizar:

    while not eleccion: # Presentamos las opciones de login y registro, damos a escoger y controlamos la entrada
        eleccion = presentar_menu(menu_usuario)

        if type(eleccion) == str: # Control de errores
            print(eleccion)
            eleccion = None

        else:
            while not usuario: # Hacemos el login/registro
                if eleccion == 1: # El usuario se loggea
                    usuario = login()

                elif eleccion == 2: # Registro de usuario
                    usuario = login(False)

                if type(usuario) == str: # Control de errores
                    print(usuario)
                    usuario = None

    while not eleccion:
        eleccion = presentar_menu(menu_compra)

        if type(eleccion) == str: # Control de errores
            print(eleccion)
            eleccion = None

        else:
            if eleccion == 1: # Escoge añadir articulos
                presentar_articulos(lista_objetos, usuario)

            elif eleccion == 2: # Escoge añadir bono
                pass

            else: # Escoge salir, hay que cobrarle
                pass

    
    
        
    
    

    
    


    
            
            

    