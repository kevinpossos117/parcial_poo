# Proyecto Biblioteca (MVVM + Firebase)

Este proyecto permite **registrar libros y usuarios** conectándose a **Firebase Realtime Database**.  
Fue desarrollado en **Python** aplicando el patrón **MVVM (Modelo - Vista - VistaModelo)**.

---

## Requisitos

- Python 3.10 o superior  
- Librería Firebase Admin

Instalar con:
```bash
pip install firebase-admin
```

---

## Configuración de Firebase

1. Crea un proyecto en [Firebase Console](https://console.firebase.google.com/).  
2. Activa **Realtime Database**.  
3. Descarga la clave privada (`.json`) y colócala en la carpeta del proyecto.  
4. Ajusta la ruta y URL en `vista_modelo.py`:
   ```python
   cred = credentials.Certificate("firebase_config.json")
   firebase_admin.initialize_app(cred, {
       "databaseURL": "https://tu-proyecto.firebaseio.com/"
   })
   ```

---

## Archivos principales

- `modelo.py` → Clases **Libro** y **Usuario**  
- `vista_modelo.py` → Lógica y conexión con Firebase  
- `vista.py` → Interfaz de consola  
- `main.py` → Punto de entrada del programa

---

## Cómo ejecutar

Ejecuta el siguiente comando en la terminal:

```bash
python main.py
```

Aparecerá el menú:

```
 MENÚ DE BIBLIOTECA
1. Agregar libro
2. Registrar usuario
3. Mostrar libros
4. Mostrar usuarios
5. Salir
```

---

## Ejemplo de funcionamiento

### Terminal  
<img width="986" height="317" alt="image" src="https://github.com/user-attachments/assets/76b3f362-1821-4d2d-b5fe-ef24661d50af" />


### Firebase  
<img width="1484" height="539" alt="image" src="https://github.com/user-attachments/assets/74e7cce9-338d-4e91-8555-5586f5bec9cf" />

