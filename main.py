from moduls.models import *
from moduls.utils import *
from bonos_db.iniciar_db import iniciar_database


PRECIO_MINIMO = 50

finalizar = False
eleccion = None
usuario = None

iniciar_database()

lista_objetos_articulo = listar_articulos()
lista_objetos_bono = listar_bonos()



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
                presentar_articulos(lista_objetos_articulo, usuario)

            elif eleccion == 2: # Escoge añadir bono
                print(seleccionar_bonos(lista_objetos_bono, usuario))

            else: # Escoge salir, hay que cobrarle
                precio_total, descontado, precio_final = usuario.finalizar_compra()
                print(f"El precio total es:  {precio_total}€")
                print(f"Se le ha descontado:  {descontado}€")
                print(f"El precio final es:  {precio_final}€")
                finalizar = True

    
    
        
    
    

    
    


    
            
            

    