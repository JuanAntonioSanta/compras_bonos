from bonos_db.bonos_db_carritos import insertar_carrito, update_carrito

        


class Articulo():
    # Es la clase base de mi programa
    id = 0

    def __init__ (self, nombre, descripcion, precio, id = None):
        # Constructor
        if not id:
            self.__id = Articulo.id +1

        else:
            self.__id = id

        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio = precio

        Articulo.id += 1
    
    # Getters y Setters
    @property
    def id(self):
        return self.__id
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, text):
        self.__nombre = text
    
    @property
    def descripcion(self):
        return self.__descripcion
    
    @descripcion.setter
    def descripcion(self, text):
        self.__descripcion = text

    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, decimal):
        self.__precio = decimal

    # Representacion textual
    def __str__(self):
        return f"{self.__nombre}: {self.__descripcion}   {self.__precio}€"



    # Métodos de base de datos
    def insert(self):
        db_insert(self.__id)

    def select_id(self):
        db_select(self.__id)

class Bono():
    #creamos la clase bono rescatándola de la base de datos
    def __init__(self, codigo, fecha, porcentaje, estado):
        self.__codigo = codigo
        self.__fecha = fecha
        self.__porcentaje = porcentaje
        self.__estado = estado

    # Getters/Setters

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, valor):
        self.__codigo = valor

    @property
    def fecha(self):
        return self.__fecha
    
    @fecha.setter
    def fecha(self, nueva_fecha):
        self.__fecha = nueva_fecha

    @property
    def porcentaje(self):
        return self.__porcentaje
    
    @porcentaje.setter
    def porcentaje(self, descuento):
        self.__porcentaje = descuento

    @property
    def estado(self):
        return self.__estado
    
    @porcentaje.setter
    def estado(self, estado_nuevo):
        self.__estado = estado_nuevo

    #Representacion textual

    def __str__(self):
        return f"{self.codigo}  Descuento:{self.descuento} Válido hasta:{self.fecha}"

    # Métodos de base de datos

    def insert(self):
        db_insert(self.__id)

    def select_id(self):
        db_select(self.__id)
    
    def update(self):
        #selecionamos todos los articulos de la base de datos
        db_update(self.__id)
        
    
class Carrito():
    id = 0
    
    def __init__(self, lista_articulos):
        self.__id = Carrito.id + 1
        self.__lista_articulos = lista_articulos
        self.insert()

        Carrito.id += 1
    
    @property
    def id(self):
        return self.__id

    @property
    def lista_articulos(self):
        return self.__lista_articulos
    
    @lista_articulos.setter
    def lista_articulos(self, lista_articulos_nueva):
        self.__lista_articulos = lista_articulos_nueva

    # Métodos con el articulo
        
    def add_articulo(self, articulo):
        self.__lista_articulos.append(articulo)

    # Métodos de base de datos

    def insert(self):
        insertar_carrito(self)

    def update(self):
        update_carrito(self)

    # def select(self):
    #     db_select(self)

class Cliente():

    def __init__(self, nombre_usuario, passwd):
        self.__username = nombre_usuario
        self.__passwd = passwd
        self.__carrito = Carrito([]) # cada cliente tiene su carrito de compra creado en vacio
        self.__bono = None

    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, nombre):
        self.__username = nombre

    @property
    def passwd(self):
        return self.__passwd
    
    @passwd.setter
    def passwd(self, passwd):
        self.__passwd = passwd

    @property
    def carrito(self):
        return self.__carrito
    
    @carrito.setter
    def carrito(self, lista):
        self.__carrito = lista.copy()

    @property
    def bono(self):
        return self.__bono
    
    @bono.setter
    def bono(self, valor):
        self.__bono = valor
        

    # Métodos de base de datos

    def select(self):
        # Devuelve true of false dependiendo de si el usuario existe o no
        db_select(self)

    def insert(self):
        db_insert(self)

    def update(self):
        db_update(self)


# class Categoria():
#     id = 0

#     def __init__(self, categoria):
#         self.__id = Categoria.id + 1
#         self.__categoria = categoria

#         Categoria.id += 1

#     @property
#     def id(self):
#         return self.__id
    
#     @property
#     def categoria(self):
#         return self.__categoria
    
#     @categoria.setter
#     def categoria(self, categoria):
#         self.__categoria = categoria

#     # Métodos de base de datos

#     def select(self):
#         db_select(self)

#     def insert(self):
#         insert(self)

#     def update(self):
#         update(self)
    
    
