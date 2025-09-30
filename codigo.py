class biblioteca():
    def __init__(self):
        pass
    

#crearemos la clase usuarios en la cuañ estaran los nombres y edad de los usuarios 
class usuarios():
    def __init__(self, nombre, edad):
        self.nombre= nombre
        self.edad = edad

#crearemos la funcion para registrar nuevos usuarios en el cual le pediremos los datos a los usuarios 
    def registrar_ususarios(self,nombre ,edad):
        self.nombre= input("ingresa tu nombre: ")
        self.edad = int(input("ingresa tu edad "))


#creamos la clase libros la cual contendra el nombre de los libros y la categoria a la que pertenece 
class libros():
    def __init__(self, libros, categorias):
        self.libros = libros
        self.categorias= ["terror","accion","fantacia"]

#creamos la funcion para agregar nuevos libros en el cual pediremos los datos 
    def registrar_libros(self, libros, categorias):
        self.libros = input("nombre del libro: ")
        categorias = input("en que categoria se encuentra el libro: 1.(terror) 2.(accion) 3.(fantacia)")
        if categorias == 1:
            print("el libro se añadio a terror")
        elif categorias == 2:
            print("el lirbo se agrego a accion")
        elif categorias == 3:
            print("el libro se agrefo a fantacia")
        else:
            print("numero invalido")
    
            
