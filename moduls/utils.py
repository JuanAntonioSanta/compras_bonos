from moduls.models import Cliente

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