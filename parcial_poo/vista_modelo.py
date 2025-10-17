# VISTA MODELO: Lógica + conexión con Firebase
import firebase_admin
from firebase_admin import credentials, db
from modelo import Libro, Usuario

# Inicializar Firebase solo una vez
try:
    cred = credentials.Certificate("parcial-59236-firebase-adminsdk-fbsvc-b8754fdee9.json")
    firebase_admin.initialize_app(cred, {
        "databaseURL": "https://parcial-59236-default-rtdb.firebaseio.com/"
    })
except ValueError:
    pass  # Evita error si ya está inicializado

class BibliotecaViewModel:
    def __init__(self):
        self.ref_libros = db.reference("libros")
        self.ref_usuarios = db.reference("usuarios")

    def agregar_libro(self, titulo, autor):
        libro = Libro(titulo, autor)
        nuevo_libro = {"titulo": libro.titulo, "autor": libro.autor}
        self.ref_libros.push(nuevo_libro)
        return f"Libro '{titulo}' agregado con éxito a Firebase."

    def registrar_usuario(self, nombre, id_usuario):
        usuario = Usuario(nombre, id_usuario)
        nuevo_usuario = {"nombre": usuario.nombre, "id_usuario": usuario.id_usuario}
        self.ref_usuarios.push(nuevo_usuario)
        return f"Usuario '{nombre}' registrado correctamente en Firebase."

    def obtener_libros(self):
        datos = self.ref_libros.get()
        if datos:
            return [(info["titulo"], info["autor"]) for info in datos.values()]
        return []

    def obtener_usuarios(self):
        datos = self.ref_usuarios.get()
        if datos:
            return [(info["nombre"], info["id_usuario"]) for info in datos.values()]
        return []
