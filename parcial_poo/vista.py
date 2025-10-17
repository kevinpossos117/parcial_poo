from vista_modelo import BibliotecaViewModel

class BibliotecaView:
    def __init__(self):
        self.vm = BibliotecaViewModel()

    def mostrar_menu(self):
        while True:
            print("\n MENÚ DE BIBLIOTECA")
            print("1. Agregar libro")
            print("2. Registrar usuario")
            print("3. Mostrar libros")
            print("4. Mostrar usuarios")
            print("5. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_libro()
            elif opcion == "2":
                self.registrar_usuario()
            elif opcion == "3":
                self.mostrar_libros()
            elif opcion == "4":
                self.mostrar_usuarios()
            elif opcion == "5":
                print(" Saliendo del sistema...")
                break
            else:
                print(" Opción inválida, intente nuevamente.")

    def agregar_libro(self):
        titulo = input("Título del libro: ")
        autor = input("Autor: ")
        print(self.vm.agregar_libro(titulo, autor))

    def registrar_usuario(self):
        nombre = input("Nombre del usuario: ")
        id_usuario = input("ID del usuario: ")
        print(self.vm.registrar_usuario(nombre, id_usuario))

    def mostrar_libros(self):
        libros = self.vm.obtener_libros()
        if libros:
            print(" Libros en Firebase:")
            for titulo, autor in libros:
                print(f"  - {titulo} ({autor})")
        else:
            print("No hay libros registrados.")

    def mostrar_usuarios(self):
        usuarios = self.vm.obtener_usuarios()
        if usuarios:
            print(" Usuarios registrados:")
            for nombre, id_usuario in usuarios:
                print(f"  - {nombre} (ID: {id_usuario})")
        else:
            print("No hay usuarios registrados.")
