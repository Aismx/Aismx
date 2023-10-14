import tkinter as tk
from tkinter import messagebox
import subprocess
import random
import ctypes


class RegistroVentana(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Registro de Usuario calculadora Say fil")
        self.geometry("300x250")
        self.configure(bg="black")

        self.usuarios_registrados = master.usuarios_registrados
        self.nombre_registro = tk.StringVar()
        self.contraseña_registro = tk.StringVar()
        self.confirmar_contraseña = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Agregamos los widgets necesarios
        self.label_nombre_registro = tk.Label(
            self, text="Nombre de Usuario:", bg="black", fg="white")
        self.label_nombre_registro.pack()
        self.entry_nombre_registro = tk.Entry(
            self, textvariable=self.nombre_registro)
        self.entry_nombre_registro.pack()

        self.label_contraseña_registro = tk.Label(
            self, text="Contraseña:", bg="black", fg="white")
        self.label_contraseña_registro.pack()
        self.entry_contraseña_registro = tk.Entry(
            self, show="*", textvariable=self.contraseña_registro)
        self.entry_contraseña_registro.pack(pady=10)

        self.label_confirmar_contraseña = tk.Label(
            self, text="Confirmar Contraseña:", bg="black", fg="white")
        self.label_confirmar_contraseña.pack()
        self.entry_confirmar_contraseña = tk.Entry(
            self, show="*", textvariable=self.confirmar_contraseña)
        self.entry_confirmar_contraseña.pack(pady=10)

        self.btn_mostrar_contraseña = tk.Button(
            self, text="Mostrar Contraseña", bg="#1E90FF", fg="white", command=self.mostrar_contraseña)
        self.btn_mostrar_contraseña.pack(pady=10)

        self.btn_registrar = tk.Button(
            self, text="Registrar Usuario", bg="#1E90FF", fg="white", command=self.registrar_usuario)
        self.btn_registrar.pack(pady=10)

        self.label_recomendaciones = tk.Label(
            self, text="Recomendaciones de Contraseña:", bg="black", fg="white")
        self.label_recomendaciones.pack(pady=10)

        self.btn_recomendacion_usuario = tk.Button(
            self, text="Recomendación Usuario", bg="#1E90FF", fg="white", command=self.recomendar_usuario)
        self.btn_recomendacion_usuario.pack(pady=5)

        self.btn_recomendacion_contraseña = tk.Button(
            self, text="Recomendación Contraseña", bg="#1E90FF", fg="white", command=self.recomendar_contraseña)
        self.btn_recomendacion_contraseña.pack(pady=5)

        # Deshabilitar el copiado y pegado en la confirmación de contraseña
        self.entry_confirmar_contraseña.config(validate="key", validatecommand=(self.entry_confirmar_contraseña.register(
            self.validar_confirmar_contraseña), '%d', '%i', '%S', '%P', '%s', '%v', '%V', '%W'))

    def registrar_usuario(self):
        usuario = self.nombre_registro.get()
        contraseña = self.contraseña_registro.get()
        confirmar_contraseña = self.confirmar_contraseña.get()

        if usuario.strip() and contraseña.strip() and confirmar_contraseña.strip():
            if usuario in self.usuarios_registrados:
                messagebox.showerror("Registro Fallido",
                                     "El usuario ya está registrado.")
            elif contraseña != confirmar_contraseña:
                messagebox.showerror("Registro Fallido",
                                     "Las contraseñas no coinciden.")
            else:
                self.usuarios_registrados[usuario] = contraseña
                messagebox.showinfo("Registro Exitoso",
                                    "Usuario registrado correctamente.")
                self.nombre_registro.set("")
                self.contraseña_registro.set("")
                self.confirmar_contraseña.set("")
                self.destroy()
        else:
            messagebox.showerror(
                "Registro Fallido", "Por favor ingrese un usuario, contraseña y confirmar contraseña válidos.")

    def mostrar_contraseña(self):
        if self.entry_contraseña_registro.cget('show') == '':
            self.entry_contraseña_registro.configure(show='*')
        else:
            self.entry_contraseña_registro.configure(show='')
        if self.master.entry_contraseña.cget('show') == '':
            self.master.entry_contraseña.configure(show='*')
        else:
            self.master.entry_contraseña.configure(show='')
        if self.entry_confirmar_contraseña.cget('show') == '':
            self.entry_confirmar_contraseña.configure(show='*')
        else:
            self.entry_confirmar_contraseña.configure(show='')

   

    def recomendar_usuario(self):
        primer_nombre = ["Luis", "Pedro", "Juan", "María", "Ana",
                         "Gustavo", "Sandra", "Rodrigo", "Verónica", "Jorge"]
        apellido_paterno = ["García", "López", "Pérez", "Martínez",
                            "González", "Hernández", "Jiménez", "Díaz", "Torres", "Rivera"]
        numero_random = str(random.randint(1, 1000))
        usuario_recomendado = (random.choice(
            primer_nombre) + "." + random.choice(apellido_paterno) + numero_random)
        self.nombre_registro.set(usuario_recomendado)

    def recomendar_contraseña(self):
        letras = "abcdefghijklmnopqrstuvwxyz"
        numeros = "0123456789"
        simbolos = "!@#$%^&*()_+[]{}/;,<.>?\'\":|-="
        categoria = [letras, numeros, simbolos]
        longitud = random.randint(8, 16)
        contraseña_recomendada = ""
        for _ in range(longitud):
            categoria_elegida = random.choice(categoria)
            caracter_elegido = random.choice(categoria_elegida)
            contraseña_recomendada += caracter_elegido
        self.contraseña_registro.set(contraseña_recomendada)


class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicación de Inicio de Sesión")
        self.geometry("400x400")
        self.configure(bg="black")

        self.usuarios_registrados = {"root": "1234"}  # Usuario: Contraseña
        self.usuario_actual = tk.StringVar()
        self.contraseña_actual = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        self.label_bienvenida = tk.Label(
            self, text="Bienvenido, por favor inicie sesión", bg="black", fg="white", font=("Arial", 14))
        self.label_bienvenida.pack(pady=50)

        self.label_usuario = tk.Label(
            self, text="Usuario:", bg="black", fg="white", font=("Arial", 12))
        self.label_usuario.pack(pady=5)
        self.entry_usuario = tk.Entry(
            self, textvariable=self.usuario_actual, font=("Arial", 12))
        self.entry_usuario.pack()

        self.label_contraseña = tk.Label(
            self, text="Contraseña:", bg="black", fg="white", font=("Arial", 12))
        self.label_contraseña.pack(pady=5)
        self.entry_contraseña = tk.Entry(
            self, show="*", textvariable=self.contraseña_actual, font=("Arial", 12))
        self.entry_contraseña.pack()

        self.btn_mostrar_contraseña = tk.Button(
            self, text="Mostrar Contraseña", bg="#1E90FF", fg="white", command=self.mostrar_contraseña)
        self.btn_mostrar_contraseña.pack(pady=10)

        self.btn_login = tk.Button(
            self, text="Iniciar Sesión", bg="#1E90FF", fg="white", command=self.login)
        self.btn_login.pack(pady=10)

        self.btn_registro = tk.Button(self, text="Registrar Nuevo Usuario",
                                      bg="#1E90FF", fg="white", command=self.mostrar_ventana_registro)
        self.btn_registro.pack(pady=10)

    def login(self):
        usuario = self.usuario_actual.get()
        contraseña = self.contraseña_actual.get()

        if usuario in self.usuarios_registrados and self.usuarios_registrados[usuario] == contraseña:
            messagebox.showinfo("Inicio de Sesión Exitoso",
                                f"Bienvenido, {usuario}!")
            self.redirigir_a_calculadora()
        else:
            messagebox.showerror("Inicio de Sesión Fallido",
                                 "Usuario o contraseña incorrectos.")

    def mostrar_ventana_registro(self):
        ventana_registro = RegistroVentana(self)

    def redirigir_a_calculadora(self):
        ruta_calculadora = r"D:\python\PYTHON\calculadora_SF_p1\calculadora.py"
        subprocess.Popen(["python", ruta_calculadora])
        self.destroy()

    def mostrar_contraseña(self):
        if self.entry_contraseña.cget('show') == '':
            self.entry_contraseña.configure(show='*')
        else:
            self.entry_contraseña.configure(show='')

        for child in self.winfo_children():
            if isinstance(child, RegistroVentana):
                child.mostrar_contraseña()


if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()

