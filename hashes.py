import os
import hashlib
import time
import json
import random
import string
import threading
import tkinter as tk
from tkinter import ttk, scrolledtext, simpledialog, messagebox

# Variables Globales
Contrasenias = {}
Caracteres = r".,!@#$%^&*()_+{}[]|\:;/?<>-_"
Letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

class ProyectoFinal:
    def __init__(self, root):
        self.root = root
        self.root.title("El Software mas cabron que has visto en tu vida")
        self.root.geometry("1600x900")
        self.root.configure(bg="black")

        # Estilo
        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure("TButton", 
                             background="black", 
                             foreground="#00FF00", 
                             font=("Courier", 12, "bold"),
                             borderwidth=1,
                             focuscolor="none")
        self.style.map("TButton", 
                       background=[('active', '#003300')], 
                       foreground=[('active', '#00FF00')])
        
        self.style.configure("TLabel", 
                             background="black", 
                             foreground="#00FF00", 
                             font=("Courier", 14, "bold"))
        
        self.style.configure("Horizontal.TProgressbar",
                             troughcolor="black",
                             background="#00FF00",
                             thickness=20)

        # Layout Principal (Dos columnas)
        self.main_frame = tk.Frame(root, bg="black")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Columna Izquierda (Funcionalidad)
        self.left_frame = tk.Frame(self.main_frame, bg="black")
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        # Columna Derecha (Arte ASCII)
        self.right_frame = tk.Frame(self.main_frame, bg="black", width=900)
        self.right_frame.pack_propagate(False)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(10, 0))

        # --- Contenido Izquierda ---
        
        # Título
        self.label_titulo = ttk.Label(self.left_frame, text="--- Proyecto Final ---", anchor="center")
        self.label_titulo.pack(pady=20)

        # Frame de Botones
        self.frame_botones = tk.Frame(self.left_frame, bg="black")
        self.frame_botones.pack(pady=10)

        botones = [
            ("1. Verificar Archivo JSON", self.opcion_1),
            ("2. Buscar Contraseña (Hash)", self.opcion_2),
            ("3. Hashear Todo", self.opcion_3),
            ("4. Generar Contraseñas", self.opcion_4),
            ("5. Verificar Seguridad", self.opcion_5),
            ("6. Eliminar Inseguras", self.opcion_6),
            ("7. Hackear SIIAU", self.hackear_siiau),
            ("8. Salir", self.salir)
        ]

        for texto, comando in botones:
            btn = ttk.Button(self.frame_botones, text=texto, command=comando, width=40)
            btn.pack(pady=5)

        # Consola
        self.consola = scrolledtext.ScrolledText(self.left_frame, bg="black", fg="#00FF00", font=("Courier", 9), height=20, wrap=tk.WORD)
        self.consola.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        self.consola.insert(tk.END, "="*70 + "\n")
        self.consola.insert(tk.END, "  SISTEMA INICIADO - MODO VERBOSE ACTIVADO\n")
        self.consola.insert(tk.END, "  Ready for commands...\n")
        self.consola.insert(tk.END, "="*70 + "\n")
        self.consola.config(state=tk.DISABLED)

        # Barra de Progreso
        self.progress = ttk.Progressbar(self.left_frame, orient="horizontal", length=500, mode="determinate", style="Horizontal.TProgressbar")
        self.progress.pack(pady=10, fill=tk.X, padx=20)

        # --- Contenido Derecha (Arte ASCII) ---
        self.ascii_label = tk.Label(self.right_frame, text="", bg="black", fg="#00FF00", font=("Courier", 10), justify=tk.LEFT, anchor="n")
        self.ascii_label.pack(fill=tk.BOTH, expand=True)

        # Datos de Arte ASCII
        self.ascii_inicio = [
           r"""⠀⠀⠀⠀⠀
               ⣾⣿⣿⣿⣿⣷⢸⣿⣿⡜⢯⣷⡌⡻⣿⣿⣿⣆⢈⠻⠿⢿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡁⢳⣿⣿⣿⣿⣿⣿⡜⣿⣿⣧⢀⢻⣷⠰⠈⢿⣿⣿⣧⢣⠉⠑⠪⢙⠿⠿⠿⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣱⡇⡞⣿⣿⣿⣿⣿⣿⡇⣿⣿⡏⡄⣧⠹⡇⠧⠈⢻⣿⣿⡇⢧⢢⠀⠀⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣇⢃⢿⣿⣿⣿⣿⣿⣷⣿⣿⠇⢃⣡⣤⡹⠐⣿⣀⢻⣿⣿⢸⡎⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣾⣿⣿⠘⡸⣿⣿⣿⣿⣿⣿⣿⡿⣰⣿⣿⢟⡷⠈⠋⠃⠎⢿⣿⡏⣿⠀⠘⢆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⢹⣿⣿⡐⢡⢹⣿⣿⣿⣿⡏⣿⢣⣿⣿⡑⠁⠔⠀⠉⠉⠢⡘⣿⡇⣿⡇⠀⡀⠡⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠘⣿⣿⣇⠇⢣⢻⣿⣿⣿⡇⢇⣾⣿⣿⡆⢸⣤⡀⠚⢂⠀⢡⢿⡇⣿⡇⠀⢿⠀⠀⠄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠠⠹⣿⣿⡘⣆⢣⠻⣿⣿⢈⣾⣿⣿⣿⣶⣸⣏⢀⣬⣋⡼⣠⢸⢹⣿⡇⢠⣼⠙⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠁⠹⣿⣇⠹⡃⠃⠙⡇⠘⢿⣿⣿⣿⣿⣿⣏⣓⣉⣭⣴⣿⠘⢸⣿⠁⠘⠋⠀⠹⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⠀⠀⠈⢿⣇⠂⣷⠄⠐⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢠⢸⡏⠀⢀⣠⣴⣾⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⠀⠀⠀⠙⠆⠈⠢⠲⠥⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡞⣸⠁⠀⢸⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠄⠃⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⡏⠹⣿⣿⡿⠫⠊⠀⠀⠀⣶⠀⢻⣿⣿⣿⣿⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠻⠿⠿⠿⢋⠀⠀⠀⠀⢀⣼⣿⡆⠈⣿⣿⣿⡟⣱⡷⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⣁⡀⠨⣛⠿⠶⠄⢀⣠⣾⣿⣿⣷⠀⢹⣿⡟⣴⠈⢃⣶⠔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⡄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠈⣿⣿⡿⠀⡀⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⠻⣿⣿⢀⠙⠻⠿⣿⣿⣿⣿⣿⣿⡇⠁⣿⠟⡀⠈⣧⢰⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⠴⠮⣥⠻⢧⣤⣄⣀⡉⢩⣭⣍⣃⣀⣩⠎⢀⣼⠉⣼⡯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠁⣛⠓⢒⣒⣢⡭⢁⡈⠿⠿⠟⠹⠛⠁⠀⠀⠀⠰⠃⠂⠀⠀⠀"""]

        self.ascii_error = [
    r"""⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣷⣜⢿⣧⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠻⣿⣿⣿⣿⣦⠄⠄
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣮⡻⣷⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣆⠙⣿⣿⣿⣿⣧⠄
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⣿⣿⣿⣿⣿⣿⣧⢸⣿⣿⣿⡘⢿⣮⡛⣷⡙⢿⣿⡏⢻⣿⣿⣿⣧⠙⢿⣿⣿⣷⠘⢿⣿⣆⢿⣿⣿⣿⣿⣆
⣿⣿⣿⣿⣿⣿⣿⣿⡿⠐⣿⣿⣿⣿⣿⣿⠃⠄⢣⠻⣿⣧⠄⠙⢷⡀⠙⢦⡙⢿⡄⠹⣿⣿⣿⣇⠄⠻⣿⣿⣇⠈⢻⣿⡎⢿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⠋⠄⣼⣆⢧⠹⣿⣆⠄⠈⠛⣄⠄⢬⣒⠙⠂⠈⢿⣿⣿⡄⠄⠈⢿⣿⡀⠄⠙⣿⠘⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡇⠄⣿⣿⣿⣿⠏⢀⣼⣿⣿⣎⠁⠐⢿⠆⠄⠄⠈⠢⠄⠙⢷⣤⡀⠄⠙⠿⠷⠄⠄⠄⠹⠇⠄⠄⠘⠄⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⢻⣿⣿⠏⢀⣾⣿⣿⣿⣿⡦⠄⠄⡘⢆⠄⠄⠄⠄⠄⠄⠙⠻⡄⠄⠄⠉⡆⠄⠄⠄⠑⠄⢠⡀⠄⠄⣿⡿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⢸⣿⠋⣰⣿⣿⡿⢟⣫⣵⣾⣷⡄⢻⣄⠁⠄⠄⠠⣄⠄⠄⠄⠈⠂⠄⠄⠈⠄⠱⠄⠄⠄⠄⢷⢀⣠⣽⡇⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡄⠄⠄⢁⣚⣫⣭⣶⣾⣿⣿⣿⣿⣿⣿⣦⣽⣷⣄⠄⠄⠘⢷⣄⠄⠄⠄⠄⣠⠄⠄⠄⠄⠈⠉⠈⠻⢸⣿⣿⡇⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡇⠄⢠⣾⣿⣿⣿⣿⣿⡿⠿⠿⠟⠛⠿⣿⣿⣿⣿⣷⣤⣤⣤⣿⣷⣶⡶⠋⢀⡠⡐⢒⢶⣝⢿⡟⣿⢸⣿⣿⡃⣿
⣿⣿⣿⢹⣿⢿⣿⣿⣷⢠⣿⣿⣿⣿⣯⠷⠐⠋⠋⠛⠉⠁⠛⠛⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⡏⠊⡼⢷⢱⣿⡾⡷⣿⢸⡏⣿⢰⣿
⣿⣿⣿⢸⣿⡘⡿⣿⣿⠎⣿⠟⠋⢁⡀⡠⣒⡤⠬⢭⣖⢝⢷⣶⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢃⢔⠭⢵⣣⣿⠓⢵⣿⢸⢃⡇⢸⣿
⣿⣿⣿⡄⣿⡇⠄⡘⣿⣷⡸⣴⣾⣿⢸⢱⢫⡞⣭⢻⡼⡏⣧⢿⣿⣿⣿⣿⣿⣿⣿⡿⣿⢿⡿⣿⣧⣕⣋⣉⣫⣵⣾⣿⡏⢸⠸⠁⢸⡏
⣿⣿⣿⡇⠸⣷⠄⠈⠘⢿⣧⠹⣹⣿⣸⡼⣜⢷⣕⣪⡼⣣⡟⣾⣿⣿⢯⡻⣟⢯⡻⣿⣮⣷⣝⢮⣻⣿⢿⣿⣝⣿⣿⢿⣿⢀⠁⠄⢸⠄
⣿⣿⡿⣇⠄⠹⡆⠄⠄⠈⠻⣧⠩⣊⣷⠝⠮⠕⠚⠓⠚⣩⣤⣝⢿⣿⣯⡿⣮⣷⣿⣾⣿⢻⣿⣿⣿⣾⣷⣽⣿⣿⣿⣿⡟⠄⠄⠄⠄⢸
⠹⣿⡇⢹⠄⠄⠐⠄⠄⠄⠄⠈⠣⠉⡻⣟⢿⣝⢿⣝⠿⡿⣷⣝⣷⣝⣿⣿⣿⣿⣿⣿⣿⣧⢹⣿⣿⣿⣿⣿⣿⣿⣿⡟⣠⠄⠄⠄⠄⠈
⠄⠘⠇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠠⣌⠈⢳⢝⣮⣻⣿⣿⣮⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⢀
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢻⣷⣤⣝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠄⠄⠄⠄⣼
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⠏⠄⠄⠄⠄⣰⢩
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢻⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠋⠉⠉⠉⠄⠄⠄⠄⣸⣿⣿⣿⣿⡿⠃⠄⠄⠄⠄⣰⣿⣧
⣷⡀⠄⠈⢦⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢻⣯⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣤⣤⣶⣶⣶⣶⣾⣿⣿⣿⣿⡿⠋⠄⠄⠄⠄⠄⣰⣿⣿⣿
⣿⣿⣦⡱⣌⢻⣦⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠄⠄⠄⠄⠄⠄⢰⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣷⣿⣿⣦⣐⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣫⡔⢀⣴⠄⠄⠄⡼⣠⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠉⠉⠙⠛⢛⣛⣛⣭⣾⣿⣴⣿⢇⣤⣦⣾⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    """
        ]

        self.ascii_ok = [
            r"""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠶⠚⠉⢉⣩⠽⠟⠛⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠉⠀⢀⣠⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠁⠀⠀⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⡤⠤⠄⢤⣄⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠒⠋⠉⠀⠀⠀⣀⣤⠴⠒⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⡄⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⢳⡄⢀⡴⠚⠉⠀⠀⠀⠀⠀⣠⠴⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⠹⡏⠀⠀⠀⠀⠀⣀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⢬⣳⣄⣠⠤⠤⠶⠶⠒⠋⠀⠀⠀⠀⠹⡀⠀⠀⠀⠀⠈⠉⠛⠲⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⠖⠋⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠉⢳⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⠋⠀⠀⠀⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⢃⠈⠙⠲⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⠞⠁⠀⠀⠀⢀⢾⠃⠀⠀⠀⠀⠀⠀⠀⠀⢢⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⠮⣄⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣰⠋⠀⠀⢀⡤⡴⠃⠈⠦⣀⠀⠀⠀⠀⠀⠀⢀⣷⢸⠀⠀⠀⠀⢀⣀⠘⡄⠤⠤⢤⠔⠒⠂⠉⠁⠀⠀⠀⠑⢄⡀⠀⠀⠙⢦⡀⠀⠀⠀
⠀⠀⠀⠀⣼⠃⠀⠀⢠⣞⠟⠀⠀⠀⡄⠀⠉⠒⠢⣤⣤⠄⣼⢻⠸⠀⠀⠀⠀⠉⢤⠀⢿⡖⠒⠊⢦⠤⠤⣀⣀⡀⠀⠀⠀⠈⠻⡝⠲⢤⣀⠙⢦⠀⠀
⠀⠀⠀⢰⠃⠀⠀⣴⣿⠎⠀⠀⢀⣜⠤⠄⢲⠎⠉⠀⠀⡼⠸⠘⡄⡇⠀⠀⠀⠀⢸⠀⢸⠘⢆⠀⠘⡄⠀⠀⠀⢢⠉⠉⠀⠒⠒⠽⡄⠀⠈⠙⠮⣷⡀
⠀⠀⠀⡟⠀⠀⣼⢻⠧⠐⠂⠉⡜⠀⠀⡰⡟⠀⠀⠀⡰⠁⡇⠀⡇⡇⠀⠀⠀⠀⢺⠇⠀⣆⡨⢆⠀⢽⠀⠀⠀⠈⡷⡄⠀⠀⠀⠀⠹⡄⠀⠀⠀⠈⠁
⠀⠀⢸⠃⠀⠀⢃⠎⠀⠀⠀⣴⠃⠀⡜⠹⠁⠀⠀⡰⠁⢠⠁⠀⢸⢸⠀⠀⠀⢠⡸⢣⠔⡏⠀⠈⢆⠀⣗⠒⠀⠀⢸⠘⢆⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀
⠀⠀⢸⠀⠀⠀⡜⠀⠀⢀⡜⡞⠀⡜⠈⠏⠀⠈⡹⠑⠒⠼⡀⠀⠀⢿⠀⠀⠀⢀⡇⠀⢇⢁⠀⠀⠈⢆⢰⠀⠀⠀⠈⡄⠈⢢⠀⠀⠀⠈⣇⠀⠀⠀⠀
⠀⠀⢸⡀⠀⢰⠁⠀⢀⢮⠀⠇⡜⠀⠘⠀⠀⢰⠃⠀⠀⡇⠈⠁⠀⢘⡄⠀⠀⢸⠀⠀⣘⣼⠤⠤⠤⣈⡞⡀⠀⠀⠀⡇⠰⡄⢣⡀⠀⠀⢻⠀⠀⠀⠀
⠀⠀⠈⡇⠀⡜⠀⢀⠎⢸⢸⢰⠁⠀⠄⠀⢠⠃⠀⠀⢸⠀⠀⠀⠀⠀⡇⠀⠀⡆⠀⠀⣶⣿⡿⠿⡛⢻⡟⡇⠀⠀⠀⡇⠀⣿⣆⢡⠀⠀⢸⡇⠀⠀⠀
⠀⠀⢠⡏⠀⠉⢢⡎⠀⡇⣿⠊⠀⠀⠀⢠⡏⠀⠀⠀⠎⠀⠀⠀⠀⠀⡇⠀⡸⠀⠀⠀⡇⠀⢰⡆⡇⢸⢠⢹⠀⠀⠀⡇⠀⢹⠈⢧⣣⠀⠘⡇⠀⠀⠀
⠀⠀⢸⡇⠀⠀⠀⡇⠀⡇⢹⠀⠀⠀⢀⡾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢠⠃⠀⠀⠠⠟⡯⣻⣇⢃⠇⢠⠏⡇⠀⢸⡆⠀⢸⠀⠈⢳⡀⠀⡇⠀⠀⠀
⠀⠀⠀⣇⠀⡔⠋⡇⠀⢱⢼⠀⠀⡂⣼⡇⢹⣶⣶⣶⣤⣤⣀⠀⠀⠀⣇⠇⠀⠀⠀⠀⣶⡭⢃⣏⡘⠀⡎⠀⠇⠀⡾⣷⠀⣼⠀⠀⠀⢻⡄⡇⠀⠀⠀
⠀⠀⠀⣹⠜⠋⠉⠓⢄⡏⢸⠀⠀⢳⡏⢸⠹⢀⣉⢭⣻⡽⠿⠛⠓⠀⠋⠀⠀⠀⠀⠀⠘⠛⠛⠓⠀⡄⡇⠀⢸⢰⡇⢸⡄⡟⠀⠀⠀⠀⢳⡇⠀⠀⠀
⠀⣠⠞⠁⠀⠀⠀⠀⠀⢙⠌⡇⠀⣿⠁⠀⡇⡗⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠀⠀⠀⠀⠀⠀⠁⠁⠀⢸⣼⠀⠈⣇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⠁⠀⠀⢀⡠⠔⠚⠉⠉⢱⣇⢸⢧⠀⠀⠸⣱⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡤⠦⡔⠀⠀⠀⠀⠀⢀⡼⠀⠀⣼⡏⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⠀⠀⠀⠋⠀⠀⠀⢀⡠⠤⣿⣾⣇⣧⠀⠀⢫⡆⠀⠀⠀⠀⠀⠀⠀⢨⠀⠀⣠⠇⠀⠀⢀⡠⣶⠋⠀⠀⡸⣾⠁⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⡄⠀⠀⠀⠀⠠⠊⠁⠀⠀⢸⢃⠘⡜⡵⡀⠈⢿⡱⢲⡤⠤⢀⣀⣀⡀⠉⠉⣀⡠⡴⠚⠉⣸⢸⠀⠀⢠⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢧⠀⠀⠀⠀⠀⠀⠀⣀⠤⠚⠚⣤⣵⡰⡑⡄⠀⢣⡈⠳⡀⠀⠀⠀⢨⡋⠙⣆⢸⠀⠀⣰⢻⡎⠀⠀⡎⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⢷⡀⠀⠀⠀⠀⠀⠁⠀⠀⠀⡸⢌⣳⣵⡈⢦⡀⠳⡀⠈⢦⡀⠀⠘⠏⠲⣌⠙⢒⠴⡧⣸⡇⠀⡸⢸⠇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣿⠢⡀⠀⠀⠀⠠⠄⡖⠋⠀⠀⠙⢿⣳⡀⠑⢄⠹⣄⡀⠙⢄⡠⠤⠒⠚⡖⡇⠀⠘⣽⡇⢠⠃⢸⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣾⠃⠀⠀⠀⠀⠀⢀⡼⣄⠀⠀⠀⠀⠀⠑⣽⣆⠀⠑⢝⡍⠒⠬⢧⣀⡠⠊⠀⠸⡀⠀⢹⡇⡎⠀⡿⢸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡼⠁⠀⠀⠀⠀⠀⠀⢀⠻⣺⣧⠀⠀⠀⠰⢢⠈⢪⡷⡀⠀⠙⡄⠀⠀⠱⡄⠀⠀⠀⢧⠀⢸⡻⠀⢠⡇⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢰⠇⠀⠀⠀⠀⠀⠀⠀⢸⠀⡏⣿⠀⠀⠀⠀⢣⢇⠀⠑⣄⠀⠀⠸⡄⠀⠀⠘⡄⠀⠀⠸⡀⢸⠁⠀⡾⢰⡏⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
        ]

        self.ascii_adios = [
            r"""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⠶⢶⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠏⠀⠀⠀⢹⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣏⡗⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠁⣿⠀⠀⠀⣀⣼⣧⣤⣤⣀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⢀⣶⠋⠉⠀⠀⠈⠉⢳⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣸⣿⣤⣄⠀⢹⡏⠀⠀⠀⠀⠀⠀⠈⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠛⠀⠀⣻⡷⣿⣇⠀⠀⠀⠀⢀⣄⠀⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣀⡤⠤⠤⠤⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⣀⠀⠀⠀⣈⡧⠈⠛⡦⠤⠴⡟⠛⠁⠀⠻⣦⡀⠀⠀
⠀⠀⠀⠀⠀⠀⣴⠿⠉⠁⠀⠀⠀⠀⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠏⠉⠷⢶⣿⣯⣤⣤⣤⣤⣤⣤⣤⡀⠀⠀⠀⠸⣧⡄⠀
⠀⠀⠀⠀⢠⡟⠃⠀⢀⡀⠀⣶⣘⣷⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⣰⣿⠛⠃⠀⠀⠀⠀⠀⠀⠀⠛⢻⣆⠀⠀⢸⡇⠀
⠀⠀⠀⢰⡎⠁⠀⠀⠈⢳⡆⢸⣿⡿⠿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢧⡄⣼⠿⠀⠀⣶⣶⠀⠀⠀⠀⢰⣶⡆⠀⠸⣦⠀⣼⡇⠀
⠀⠀⠀⣸⡇⠀⠀⢰⣦⣼⣷⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⣿⠀⠀⢀⣛⡋⠀⠀⠀⠀⢘⣛⣁⠀⠀⣿⣾⣏⣀⣀
⠀⠀⢀⣿⠀⠀⠀⢰⡎⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⠉⣷⣄⡀⠀⢈⡆⠒⠒⢰⡁⠀⡈⣶⡾⠛⠁⠈⠉⠻
⠀⠀⣽⠁⠀⠀⠀⠘⢳⡆⠀⠀⠀⠀⠀⠀⠀⠀⢠⣀⡴⠶⠶⠶⠶⣴⠶⠞⠛⠛⠙⠛⡷⢿⣶⡶⠶⠶⠾⣶⠿⣋⣀⠀⠀⠀⠀⠀
⠀⢸⡏⠀⠀⠀⠀⠀⠸⢧⡄⡀⣠⣤⣤⣤⣄⢰⣿⠉⠁⠀⠀⠀⠀⠉⠀⣠⡄⠀⢠⣤⡟⠛⠛⣧⣤⠀⠀⠛⠛⠉⠉⠀⠀⠀⠀⠀
⢀⡸⠇⠀⠀⠀⠀⠀⠀⣼⡷⠛⠃⠀⠀⠀⠛⠛⢀⣀⠀⠀⠀⠀⠀⠀⠘⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠶⣆⣐⡾⠃⠀⠀⠀⠀⠀
⢸⡇⠀⠀⠀⠀⠀⠀⠀⢨⡄⠀⠀⠀⠀⠀⠀⠀⠘⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⡀⠀⠀⠀⠀⠀⠀
⢸⡇⠀⠀⠀⠀⠀⠀⠀⠼⠇⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⣤⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠿⠻⣤⣤⠀⠀⢀
⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣦⢀⣀⣀⣀⡀⣤⣾⣛⠀⠀⠀⠀⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣟⣀⣀⣀⣸⠛⠛⠻
⠈⢱⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠁⠀⠈⠉⣰⡶⠶⠶⠶⣯⣽⠶⣦⣤⣤⣤⣤⣤⣤⣄⣤⣶⠞⠉⠉⠉⠉⠿⠉⠀⠀⠀
⠀⠘⣿⣟⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣼⡏⠁⠀⠀⠀⠉⠙⢳⡏⠀⠀⠀⠀⠈⠉⣿⠉⠉⠀⠀⠀⠀⠀⠀⣤⠀⠀⠀
⠀⠀⠀⠛⠶⣦⣤⣤⣤⣤⣤⣤⣤⣤⣤⡴⠶⠾⠋⠘⠳⣆⡀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠻⣄⣀⠀⠀⠀⠀⢀⣾⠛⠶⠶⠶
⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠉⠻⠤⣄⣀⠀⠈⣿⠀⠀⠀⠀⠀⠀⣿⠉⠙⠛⠛⠁⠀⠘⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠿⠿⠏⢿⣤⠀⠀⠀⠀⠻⣤⠀⠀⠀⠀⠀⠀⠀⠀⣸⣧⣴
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⡋⠀⠀⠀⠀⠘⣛⠀⠀⠀⠀⠀⠀⢘⡃⠀⠈
    """
        ]

        self.ascii_hackear_siiau = [
            r"""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣷⢀⠀⠀⠀⠀⠀⡀⣀⡄⣒⠖⣒⠒⠒⠂⠀⠄⠄⡀⠀⠀⠀⠀⣠⣿⣿⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢿⡏⠓⠐⣤⣰⠲⣍⢣⠱⡘⢄⠊⠄⠁⠂⡔⠀⠀⠀⠀⠈⠒⢠⠞⠡⢹⠻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡿⣳⡵⣾⢣⡭⢓⠴⡈⠔⡈⠂⣁⠂⡌⡐⢀⠁⠀⠀⠀⠀⠀⠀⠑⠆⠡⣽⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢏⡷⣙⢦⠓⡌⢃⠆⠱⡈⠔⡀⠠⠐⢠⢁⠂⡀⠀⢀⠀⠀⠀⠀⠀⠘⠀⠘⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣚⢮⡵⣍⢎⡱⢈⢆⠨⣐⣐⢢⣌⡱⢌⠶⣌⡖⣤⣓⣂⡎⠴⣀⠀⠀⢀⠠⠀⠈⠳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡱⣏⡞⡶⣩⢖⡡⢚⡾⢟⣯⣿⣤⠈⠙⢪⠟⣿⠋⠉⣭⣿⣿⡛⠶⣧⠌⠠⠀⠐⠈⠄⠘⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⣶⣹⢾⡹⢷⣉⢶⢁⢿⣀⢸⣿⣿⣿⡇⠀⢸⡈⢷⡆⢸⢿⣿⣿⡇⠀⢰⠏⠀⠁⠆⠀⡈⢀⠈⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣞⣳⢧⣟⢮⣝⡳⡜⢦⣋⠼⣟⢬⣚⠟⠛⢀⣤⣞⠰⡈⡾⣢⣙⠟⠛⠁⢀⠜⠀⠀⠁⠀⠀⠰⡈⠄⠈⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢪⣞⣧⡟⣾⠳⣎⠵⣉⠖⣌⠲⠉⡝⣲⣲⣾⣿⣿⣾⢷⡷⣜⣷⣋⠖⠒⠈⠀⠀⠀⠀⠀⠠⠁⠠⢀⠡⠘⡄⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣽⡻⢾⣼⡹⣎⠷⣩⠖⡡⠎⡄⢣⢁⠂⣷⣿⣿⣿⣿⣿⣿⣿⣿⣯⣟⡧⡄⠀⠀⠀⠀⠀⠀⠁⡀⠀⠄⢂⠡⠈⠄⡈⢦⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣲⣟⡾⣽⣻⣜⡳⣝⠾⣡⠎⣅⠳⢌⠂⡌⢲⣹⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠡⠐⠈⠄⣂⠢⢁⠜⡠⠐⢕⠄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⢶⣛⢶⣯⣟⡷⡽⣎⡷⣹⢮⡱⢋⡔⠣⢌⠒⡠⠡⠄⡀⠂⠐⠚⠛⠛⠋⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢁⠒⢠⢂⠔⡨⢐⠡⢂⠳⣰⡀⠀⠀⠀
⠀⠀⠀⠀⣜⡾⣽⢯⣞⡾⣽⣻⡵⣏⠷⣎⡵⢋⡔⠣⢌⠂⡅⢊⡐⠠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠠⢈⡐⢌⠰⣁⢃⠞⢤⣛⢧⣇⠀⠀⠀
⠀⠀⠀⢠⣽⣿⣯⡿⣾⡽⣯⢷⣻⣽⢻⡜⣜⡣⡜⡱⢂⡱⢈⠄⠠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⡐⢀⠂⠤⠑⡠⠒⢨⠑⣌⠲⡘⢦⡟⢦⢿⠀⠀⠀
⠀⠀⠀⢸⣼⣿⣯⣟⣷⣻⣽⣟⡷⣯⢷⡻⣬⢳⡱⢥⡃⢦⢁⠎⡄⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠌⢠⠐⣀⠢⠌⡐⢡⢂⡍⢦⠱⣌⢣⡝⣺⡝⡎⡞⡄⠀⠀
⠀⠀⠀⣼⣾⣿⣷⣻⢾⣟⣷⣿⣻⣽⢯⣟⣵⣫⢞⣥⢛⡤⣋⠴⡐⡠⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠄⡁⢢⠐⡄⢓⠜⣂⠧⣘⢆⡻⣬⢷⣹⢷⣻⠴⣙⣇⠀⠀
⠀⠀⠀⣿⣿⣿⣿⡽⣿⣿⣿⣻⣿⣽⣿⣞⡷⣯⣞⣮⣟⣼⣛⡞⡳⢛⡙⢛⠛⠞⠷⠾⠖⠶⠶⠦⠦⢔⡠⢂⠥⣚⠜⣬⢚⡴⢫⣜⢮⣷⣻⣞⣯⣿⣯⡗⣥⣻⠀⠀
⠀⠀⣰⣿⣿⣿⡃⢙⣿⣿⣿⣿⣿⣿⣯⣿⣿⣯⣿⣞⣾⣳⣽⢾⣵⣫⣜⣦⢭⣎⣴⣢⣜⡴⣢⣜⡴⣎⡶⣯⣞⡵⣛⣦⣟⣼⣻⣞⡿⣾⣷⣿⣿⡝⣿⣽⢆⢯⡆⠀
⠀⠀⣟⣿⣿⣷⠀⠀⠽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣾⣿⣾⣯⣷⣿⣽⣷⣿⣿⣿⢿⣷⣿⣻⣽⣾⣽⣾⣷⣿⣿⣿⣿⣿⠋⠀⢸⣿⣯⠾⣑⠀
⠀⢀⣿⣿⣿⡿⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⠏⠀⠀⠀⣿⣿⣷⢹⠀
⠀⢸⣿⣿⣿⢂⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠃⠀⠀⠀⠀⢈⡏⠄⢊⡇
⠀⢼⣿⣿⣿⡂⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⢈⠖⡀⢌⡇
⠀⢼⣿⣿⣟⡇⠀⠀⠀⠀⠀⠀⠀⢈⣿⡿⣯⣿⣿⣿⣿⣿⣿⢿⣿⡿⣿⣿⢿⣟⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠘⣣⠀⢎⡆
⠀⣹⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠸⢿⡽⣿⣿⡷⡟⢟⢾⡿⣿⣟⣿⣿⣻⣿⣿⣻⣿⢿⣿⣷⡿⣯⣿⣿⣻⡟⣿⣿⣿⣟⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⡧⠐⢬⡇
⠀⢽⣿⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠸⣸⣟⣿⣿⣟⠀⠀⠀⠈⠈⠉⠛⠊⠙⠳⠿⠽⠯⠛⠺⠯⠛⠋⠑⠉⠀⢀⣿⣿⣛⢮⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡇⠐⣸⠃
⠀⣿⣿⣟⡇⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⢾⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢺⣷⢫⡞⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⢼⠀
⢠⣿⣻⢯⢃⡀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣻⣯⠷⣯⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡃⠀⢞⡇
⣰⣿⢯⣟⣷⡱⡄⠀⠀⠀⠀⠀⠀⣘⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣟⡿⣱⠀⠀⠀⠀⠀⠀⠀⠀⢀⣰⠓⠀⠀⢎⡃
⣽⣿⡿⣽⣞⣳⠹⡀⠀⠀⠀⠀⠀⢻⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡯⠀⠀⠀⠀⠀⠀⠀⢀⡞⠂⠀⠀⢈⡳⣼
⣿⣿⣟⡳⣿⣷⣗⣣⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣻⣿⣿⠁⠀⠀⠀⠀⠀⠀⢀⡜⢠⣞⣔⠠⣙⢞⡧
⣿⣿⣿⣵⣾⣛⣿⣾⣃⠀⠀⠀⠀⣺⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣻⡇⠀⠀⠀⠀⠀⠀⣼⣠⡿⢻⡉⢠⡝⣾⣟
⠈⢻⣿⣿⡷⣧⠿⣿⣿⠀⠀⠀⠀⣾⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣟⣿⡆⠀⠀⠀⠀⠀⠰⣿⣼⠃⣸⢏⣿⣿⣾⡿
⠀⠀⣿⣿⣿⡸⣿⣷⠇⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣾⣿⡆⠀⠀⠀⠀⠀⢸⣿⠁⣰⢿⢾⡷⣿⣹⠇
⠀⠀⠀⠙⢻⡿⣿⡦⠇⠀⠀⠀⠀⣻⣿⣷⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡿⣯⣟⠃⠀⠀⠀⠀⠀⠀⣺⡛⣲⣿⣿⣿⠿⠋⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⢿⡟⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠟⣻⢿⢄⠀⠀⠀⠀⠀⠑⠟⠛⠋⠛⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡻⣼⡷⣻⢄⠻⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢼⣯⣟⣬⠻⣼⣤⣆⡠⠤⠀⢀⡀⡀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣖⣺⣷⣳⣼⣀⢫⣷⣧⡎⣁⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢮⣷⢾⣽⣞⡿⣰⢆⣐⡙⣿⣿⢧⡝⡗⢷⣰⡐⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⣏⣹⣷⣿⣿⣿⠁⣿⣿⣿⣿⣧⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⢿⢿⣿⣿⡾⣝⣧⠘⣿⣿⣽⣿⣄⢹⣿⠮⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⠿⠿⠟⠻⢿⣷⡿⠛⠿⣿⣿⣾⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠿⠿⠟⠛⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀
    """
        ]
        self.current_ascii_list = self.ascii_inicio
        self.ascii_index = 0
        self.animate_ascii()

        # Cargar datos iniciales
        self.cargar_datos()

    def set_ascii_main(self):
        self.current_ascii_list = self.ascii_inicio
        self.ascii_index = 0

    def set_ascii_error(self):
        self.current_ascii_list = self.ascii_error
        self.ascii_index = 0

    def set_ascii_ok(self):
        self.current_ascii_list = self.ascii_ok
        self.ascii_index = 0

    def set_ascii_exit(self):
        self.current_ascii_list = self.ascii_adios
        self.ascii_index = 0

    def set_ascii_hackear_siiau(self):
        self.current_ascii_list = self.ascii_hackear_siiau
        self.ascii_index = 0

    def animate_ascii(self):
        if not self.current_ascii_list: return
        
        art = self.current_ascii_list[self.ascii_index]
        self.ascii_label.config(text=art)
        
        self.ascii_index = (self.ascii_index + 1) % len(self.current_ascii_list)
        self.root.after(1500, self.animate_ascii)

    def log(self, mensaje):
        self.consola.config(state=tk.NORMAL)
        self.consola.insert(tk.END, f"> {mensaje}\n")
        self.consola.see(tk.END)
        self.consola.config(state=tk.DISABLED)
        self.root.update_idletasks()

    def cargar_datos(self):
        global Contrasenias
        if os.path.exists("contrasenias.json"):
            try:
                with open("contrasenias.json", "r") as archivo:
                    Contrasenias = json.load(archivo)
                self.log("Base de datos cargada correctamente.")
            except json.JSONDecodeError:
                Contrasenias = {}
                self.log("Error al leer base de datos. Iniciando vacía.")
        else:
            Contrasenias = {}
            self.log("No se encontró base de datos. Se creará una nueva al guardar.")

    def guardar_datos(self):
        """Guarda los datos en el archivo JSON"""
        global Contrasenias
        self.log("="*60)
        self.log("INICIANDO SECUENCIA DE GUARDADO DE DATOS")
        self.log("="*60)
        self.log("ACCEDIENDO AL SISTEMA DE ARCHIVOS...")
        self.log(f"RUTA DE ARCHIVO: contrasenias.json")
        self.log(f"TOTAL DE CONTRASEÑAS A GUARDAR: {len(Contrasenias)}")
        try:
            self.log("ABRIENDO FLUJO DE ESCRITURA...")
            with open("contrasenias.json", "w") as f:
                self.log("SERIALIZANDO DATOS A FORMATO JSON...")
                self.log("APLICANDO FORMATO DE INDENTACIÓN (4 ESPACIOS)...")
                json.dump(Contrasenias, f, indent=4)
                self.log(f"BYTES ESCRITOS: {len(json.dumps(Contrasenias, indent=4))}")
            self.log("ESCRITURA EN DISCO COMPLETADA EXITOSAMENTE.")
            self.log("CERRANDO FLUJO DE ARCHIVO...")
            self.log("VERIFICANDO INTEGRIDAD DE DATOS...")
            self.log("✓ DATOS GUARDADOS CORRECTAMENTE")
            self.log("="*60)
            self.set_ascii_ok()
        except Exception as e:
            self.set_ascii_error()
            self.log("="*60)
            self.log(f"¡¡¡ERROR CRÍTICO DE E/S!!!")
            self.log(f"TIPO DE ERROR: {type(e).__name__}")
            self.log(f"MENSAJE: {str(e)}")
            self.log("="*60)

    def guardar_contrasenas(self):
        """Método alternativo para compatibilidad"""
        self.guardar_datos()

    def hackear_siiau(self):
        self.set_ascii_hackear_siiau()
        self.log("="*60)
        self.log("INICIANDO ATAQUE AL SISTEMA SIIAU...")
        self.log("="*60)
        self.log("ESCANEANDO PUERTOS...")
        self.log("  • Puerto 80: ABIERTO")
        self.log("  • Puerto 443: ABIERTO")
        self.log("  • Puerto 8080: ABIERTO")
        self.log("\nINTENTANDO BYPASS DE AUTENTICACIÓN...")
        self.log("  • Método 1: SQL Injection... FALLÓ")
        self.log("  • Método 2: XSS Attack... FALLÓ")
        self.log("  • Método 3: Buffer Overflow... FALLÓ")
        self.log("\nEJECUTANDO EXPLOIT SQL INJECTION...")
        self.log("  • SELECT * FROM usuarios WHERE...")
        self.log("  • ' OR '1'='1' --")
        self.log("\nACCEDIENDO A BASE DE DATOS...")
        self.log("="*60)
        self.log("███╗   ██╗ ██████╗ ")
        self.log("████╗  ██║██╔═══██╗")
        self.log("██╔██╗ ██║██║   ██║")
        self.log("██║╚██╗██║██║   ██║")
        self.log("██║ ╚████║╚██████╔╝")
        self.log("╚═╝  ╚═══╝ ╚═════╝ ")
        self.log("="*60)
        self.log("ACCESO DENEGADO. FIREWALL ACTIVADO.")
        self.log("")
        self.log("Seguro? depositame 5000 pesos y te paso el programa")
        self.log("="*60)
        messagebox.showwarning("SIIAU Hacker Pro", "Seguro? depositame 5000 pesos y te paso el programa")
        # Volver al arte principal después de 5 segundos
        self.root.after(10000, self.set_ascii_main)

    def salir(self):
        self.set_ascii_exit()
        self.log("="*60)
        self.log("FINALIZANDO SESIÓN...")
        self.log("="*60)
        self.log("LIMPIANDO MEMORIA...")
        self.log("  • Borrando variables temporales...")
        self.log("  • Liberando recursos...")
        self.log("\nCERRANDO PUERTOS...")
        self.log("  • Puerto 8080: CERRADO")
        self.log("  • Puerto 443: CERRADO")
        self.log("  • Puerto 80: CERRADO")
        self.log("\nDESCONECTANDO DEL SISTEMA...")
        self.log("\nTe portas bien")
        self.log("="*60)
        self.root.update() # Forzar actualización de UI
        self.root.after(3000, self.root.destroy)

    def generar_contrasenia_segura(self):
        longitud = 9
        while True:
            todo_junto = Letras + Caracteres + string.digits
            password = ''.join(random.choices(todo_junto, k=longitud))
            
            if (any(c.islower() for c in password) and
                any(c.isupper() for c in password) and
                any(c in Caracteres for c in password) and
                any(c.isdigit() for c in password)):
                return password

    # --- Opciones ---

    def opcion_1(self):
        self.log("="*60)
        self.log("VERIFICACIÓN DE ARCHIVO DE BASE DE DATOS")
        self.log("="*60)
        self.log("ARCHIVO A VERIFICAR: contrasenias.json")
        self.log("RUTA ACTUAL: " + os.getcwd())
        self.log("\nINICIANDO ESCANEO DEL SISTEMA DE ARCHIVOS...")
        
        if os.path.exists("contrasenias.json"):
            file_size = os.path.getsize("contrasenias.json")
            self.log("✓ ARCHIVO ENCONTRADO: contrasenias.json")
            self.log(f"  • Tamaño: {file_size} bytes ({file_size/1024:.2f} KB)")
            self.log(f"  • Ruta completa: {os.path.abspath('contrasenias.json')}")
            
            try:
                with open("contrasenias.json", "r") as f:
                    data = json.load(f)
                    self.log(f"  • Registros en DB: {len(data)}")
                    self.log(f"  • Formato: JSON válido ✓")
                    
                    hasheadas = sum(1 for v in data.values() if len(v) == 64)
                    texto_plano = len(data) - hasheadas
                    
                    self.log(f"  • Contraseñas hasheadas: {hasheadas}")
                    self.log(f"  • Contraseñas en texto plano: {texto_plano}")
            except Exception as e:
                self.log(f"  ⚠ ERROR AL LEER CONTENIDO: {str(e)}")
            
            self.log("\n" + "="*60)
            self.log("VEREDICTO: BASE DE DATOS OPERATIVA ✓")
            self.log("="*60)
            self.set_ascii_ok()
        else:
            self.log("✗ ARCHIVO NO ENCONTRADO")
            self.log("  • Estado: No existe base de datos")
            self.log("  • Acción requerida: Se creará al guardar contraseñas")
            self.log("\n" + "="*60)
            self.log("VEREDICTO: BASE DE DATOS NO INICIALIZADA")
            self.log("="*60)
            self.set_ascii_error()

    def opcion_2(self):
        contra = simpledialog.askstring("Buscar", "Ingrese la contraseña a buscar:")
        if not contra: 
            return
        
        global Contrasenias
        self.log("="*60)
        self.log("INICIANDO BÚSQUEDA DE CONTRASEÑA EN BASE DE DATOS")
        self.log("="*60)
        self.log(f"CONTRASEÑA A BUSCAR: {contra}")
        self.log(f"LONGITUD: {len(contra)} caracteres")
        self.log("GENERANDO HASH SHA-256 PARA COMPARACIÓN...")
        
        hash_obj = hashlib.sha256(contra.encode())
        hash_hex = hash_obj.hexdigest()
        
        self.log(f"HASH GENERADO: {hash_hex}")
        self.log(f"\nBUSCANDO EN {len(Contrasenias)} REGISTROS...")
        
        encontrada = False
        key_encontrada = None
        
        for key, value in Contrasenias.items():
            if value == hash_hex:
                encontrada = True
                key_encontrada = key
                break
        
        self.log("="*60)
        if encontrada:
            self.log("✓✓✓ RESULTADO: CONTRASEÑA ENCONTRADA ✓✓✓")
            self.log(f"KEY: {key_encontrada}")
            self.log(f"HASH: {hash_hex}")
            self.log("ESTADO: La contraseña existe en la base de datos (Hasheada)")
            self.set_ascii_ok()
        else:
            self.log("✗✗✗ RESULTADO: CONTRASEÑA NO ENCONTRADA ✗✗✗")
            self.log("ESTADO: La contraseña NO existe en la base de datos")
            self.log(f"HASH BUSCADO: {hash_hex}")
            self.log("SUGERENCIA: La contraseña puede ser nueva o nunca fue agregada")
            self.set_ascii_error()
        self.log("="*60)

    def opcion_3(self):
        threading.Thread(target=self._opcion_3_thread).start()

    def _opcion_3_thread(self):
        global Contrasenias
        self.log("="*60)
        self.log("INICIANDO PROCESO DE HASHEO MASIVO CON SHA-256")
        self.log("="*60)
        self.log(f"TOTAL DE CONTRASEÑAS EN DB: {len(Contrasenias)}")
        self.log("ALGORITMO: SHA-256 (Secure Hash Algorithm 256-bit)")
        self.log("ENCODING: UTF-8")
        self.log("OUTPUT: Hexadecimal (64 caracteres)")
        self.log("="*60)
        
        cambios = False
        total = len(Contrasenias)
        self.progress["maximum"] = total
        self.progress["value"] = 0
        
        count = 0
        hasheadas = 0
        ya_hasheadas = 0
        
        for key in list(Contrasenias.keys()):
            valor = Contrasenias[key]
            self.log(f"\n>>> PROCESANDO: {key}")
            self.log(f"    Valor actual: {valor[:20]}{'...' if len(valor) > 20 else ''}")
            self.log(f"    Longitud: {len(valor)} caracteres")
            
            if len(valor) != 64:  # Longitud de SHA256 hex
                self.log("    STATUS: Contraseña en texto plano detectada")
                self.log("    ACCIÓN: Aplicando hash SHA-256...")
                self.log(f"    ORIGINAL: {valor}")
                
                hash_obj = hashlib.sha256(valor.encode())
                hash_hex = hash_obj.hexdigest()
                Contrasenias[key] = hash_hex
                
                self.log(f"    HASH: {hash_hex}")
                self.log("    ✓ HASHEADO EXITOSAMENTE")
                cambios = True
                hasheadas += 1
            else:
                self.log("    STATUS: Ya está hasheada (64 chars detectados)")
                self.log("    ACCIÓN: Omitiendo...")
                ya_hasheadas += 1
            
            count += 1
            self.progress["value"] = count
            time.sleep(0.03)
        
        self.log("\n" + "="*60)
        self.log("RESUMEN DEL PROCESO DE HASHEO")
        self.log("="*60)
        self.log(f"TOTAL PROCESADAS: {count}")
        self.log(f"NUEVAS HASHEADAS: {hasheadas}")
        self.log(f"YA ESTABAN HASHEADAS: {ya_hasheadas}")
        
        if cambios:
            self.log("\nCAMBIOS DETECTADOS - GUARDANDO EN BASE DE DATOS...")
            self.guardar_datos()
            self.log("✓ PROCESO COMPLETADO: Todas las contraseñas han sido hasheadas.")
            self.set_ascii_ok()
        else:
            self.log("✓ ESTADO: Todas las contraseñas ya estaban hasheadas.")
        
        self.log("="*60)
        self.progress["value"] = 0

    def opcion_4(self):
        cantidad_str = simpledialog.askstring("Generar", "Cantidad de contraseñas a generar:")
        if not cantidad_str: return
        
        try:
            cantidad = int(cantidad_str)
            threading.Thread(target=self._opcion_4_thread, args=(cantidad,)).start()
        except ValueError:
            self.log("ERROR: Por favor ingrese un número válido.")

    def generar_contrasenas(self):
        try:
            cantidad = int(self.entry_cantidad.get())
            longitud = int(self.entry_longitud.get())
            
            if cantidad <= 0 or longitud <= 0:
                self.set_ascii_error()
                messagebox.showerror("Error", "Cantidad y longitud deben ser mayores a 0")
                return

            self.log("INICIANDO PROTOCOLO DE GENERACIÓN DE CREDENCIALES...")
            self.log(f"PARÁMETROS: CANTIDAD={cantidad}, LONGITUD={longitud}")
            
            nuevas_contrasenas = []
            for i in range(cantidad):
                pwd = ''.join(random.choice(Caracteres) for _ in range(longitud))
                nuevas_contrasenas.append({"password": pwd, "hash": ""}) # Hash vacío por ahora
                self.log(f"GENERANDO CREDENCIAL #{i+1}...")
                self.log(f"COMPLEJIDAD COMPUTACIONAL: ALTA")
                self.log(f"ENTROPÍA: {longitud * 6.5:.2f} BITS")
                self.log(f"CREDENTIAL GENERATED: {pwd}")
                self.log("VERIFICANDO INTEGRIDAD... OK")
                self.log("----------------------------------------")

            self.contrasenas.extend(nuevas_contrasenas)
            self.log("TODAS LAS CREDENCIALES GENERADAS EXITOSAMENTE.")
            self.log("INICIANDO SECUENCIA DE ALMACENAMIENTO...")
            self.guardar_contrasenas()
            self.actualizar_lista()
            self.set_ascii_ok()
            self.log("PROCESO COMPLETADO. SISTEMA SEGURO.")
            messagebox.showinfo("Éxito", f"Se generaron {cantidad} contraseñas.")
            
            # Volver al arte principal después de 5 segundos
            self.root.after(5000, self.set_ascii_main)

        except ValueError:
            self.set_ascii_error()
            self.log("ERROR CRÍTICO: ENTRADA DE DATOS INVÁLIDA.")
            messagebox.showerror("Error", "Por favor ingrese números válidos")

    def _opcion_4_thread(self, cantidad):
        global Contrasenias
        self.log("="*60)
        self.log("INICIANDO GENERADOR DE CONTRASEÑAS SEGURAS")
        self.log("="*60)
        self.log(f"CANTIDAD SOLICITADA: {cantidad} contraseñas")
        self.log(f"NIVEL DE SEGURIDAD: MÁXIMO")
        self.log(f"LONGITUD MÍNIMA: 9 caracteres")
        self.log(f"REQUISITOS: Mayúsculas, Minúsculas, Números, Símbolos")
        self.log("="*60)
        
        self.progress["maximum"] = cantidad
        self.progress["value"] = 0
        
        nuevas_keys = []
        for i in range(cantidad):
            self.log(f"\n>>> GENERANDO CONTRASEÑA #{i+1} de {cantidad}")
            self.log("INICIALIZANDO GENERADOR ALEATORIO...")
            self.log("MEZCLANDO CARACTERES: A-Z, a-z, 0-9, símbolos...")
            
            nueva = self.generar_contrasenia_segura()
            key = f"pass_{int(time.time())}_{i}"
            
            self.log(f"✓ CONTRASEÑA GENERADA: {nueva}")
            self.log(f"  • Longitud: {len(nueva)} caracteres")
            self.log(f"  • Mayúsculas: {sum(1 for c in nueva if c.isupper())}")
            self.log(f"  • Minúsculas: {sum(1 for c in nueva if c.islower())}")
            self.log(f"  • Números: {sum(1 for c in nueva if c.isdigit())}")
            self.log(f"  • Símbolos: {sum(1 for c in nueva if c in Caracteres)}")
            self.log(f"  • KEY ID: {key}")
            self.log("  • ESTADO: ✓ VÁLIDA Y SEGURA")
            
            Contrasenias[key] = nueva
            nuevas_keys.append(key)
            
            self.progress["value"] = i + 1
            time.sleep(0.02)
        
        self.log("\n" + "="*60)
        self.log("PROCESO DE GENERACIÓN COMPLETADO")
        self.log("="*60)
        self.guardar_datos()
        self.log(f"✓ {cantidad} CONTRASEÑAS GENERADAS Y ALMACENADAS")
        self.progress["value"] = 0
        
        # Preguntar si hashear (usando messagebox en el hilo principal)
        self.root.after(0, lambda: self._preguntar_hashear(nuevas_keys))

    def _preguntar_hashear(self, keys):
        global Contrasenias
        respuesta = messagebox.askyesno("Hashear", "¿Desea hashear las nuevas contraseñas inmediatamente?")
        if respuesta:
            self.log("\n" + "="*60)
            self.log("INICIANDO HASHEO DE CONTRASEÑAS NUEVAS")
            self.log("="*60)
            self.log(f"CANTIDAD A HASHEAR: {len(keys)} contraseñas")
            
            for i, key in enumerate(keys, 1):
                valor = Contrasenias[key]
                self.log(f"\n>>> HASHEANDO {i}/{len(keys)}: {key}")
                self.log(f"    CONTRASEÑA ORIGINAL: {valor}")
                self.log(f"    APLICANDO SHA-256...")
                
                hash_obj = hashlib.sha256(valor.encode())
                hash_hex = hash_obj.hexdigest()
                Contrasenias[key] = hash_hex
                
                self.log(f"    HASH GENERADO: {hash_hex}")
                self.log(f"    ✓ COMPLETADO")
            
            self.log("\n>>> GUARDANDO HASHES EN BASE DE DATOS...")
            self.guardar_datos()
            self.log("✓ TODAS LAS CONTRASEÑAS NUEVAS HAN SIDO HASHEADAS")
            self.log("="*60)

    def opcion_5(self):
        contra = simpledialog.askstring("Verificar", "Ingrese contraseña a analizar:")
        if not contra: 
            return
        
        self.log("="*60)
        self.log("ANÁLISIS DE SEGURIDAD DE CONTRASEÑA")
        self.log("="*60)
        self.log(f"CONTRASEÑA INGRESADA: {contra}")
        self.log(f"LONGITUD: {len(contra)} caracteres")
        
        tiene_minus = any(c.islower() for c in contra)
        tiene_mayus = any(c.isupper() for c in contra)
        tiene_raro = any(c in Caracteres for c in contra)
        tiene_num = any(c.isdigit() for c in contra)
        
        self.log("\nCRITERIOS DE SEGURIDAD:")
        self.log(f"  ✓ Longitud >= 9: {'SÍ ✓' if len(contra) >= 9 else 'NO ✗'} (actual: {len(contra)})")
        self.log(f"  ✓ Minúsculas: {'SÍ ✓' if tiene_minus else 'NO ✗'} ({sum(1 for c in contra if c.islower())} encontradas)")
        self.log(f"  ✓ Mayúsculas: {'SÍ ✓' if tiene_mayus else 'NO ✗'} ({sum(1 for c in contra if c.isupper())} encontradas)")
        self.log(f"  ✓ Números: {'SÍ ✓' if tiene_num else 'NO ✗'} ({sum(1 for c in contra if c.isdigit())} encontrados)")
        self.log(f"  ✓ Símbolos: {'SÍ ✓' if tiene_raro else 'NO ✗'} ({sum(1 for c in contra if c in Caracteres)} encontrados)")
        
        if len(contra) >= 9 and tiene_minus and tiene_mayus and tiene_raro and tiene_num:
            self.log("\n" + "="*60)
            self.log("VEREDICTO: ✓✓✓ CONTRASEÑA SEGURA ✓✓✓")
            self.log("="*60)
            self.set_ascii_ok()
        else:
            self.log("\n" + "="*60)
            self.log("VEREDICTO: ✗✗✗ CONTRASEÑA INSEGURA (DÉBIL) ✗✗✗")
            self.log("="*60)
            self.log("RECOMENDACIONES:")
            if len(contra) < 9:
                self.log("  • Aumentar longitud a mínimo 9 caracteres")
            if not tiene_minus:
                self.log("  • Agregar letras minúsculas (a-z)")
            if not tiene_mayus:
                self.log("  • Agregar letras mayúsculas (A-Z)")
            if not tiene_num:
                self.log("  • Agregar números (0-9)")
            if not tiene_raro:
                self.log("  • Agregar símbolos especiales (!@#$%^&*...)")
            self.set_ascii_error()

    def opcion_6(self):
        threading.Thread(target=self._opcion_6_thread).start()

    def _opcion_6_thread(self):
        global Contrasenias
        self.log("="*60)
        self.log("INICIANDO ANÁLISIS DE SEGURIDAD Y LIMPIEZA")
        self.log("="*60)
        self.log(f"TOTAL DE CONTRASEÑAS A ANALIZAR: {len(Contrasenias)}")
        self.log("CRITERIOS DE SEGURIDAD:")
        self.log("  • Longitud mínima: 9 caracteres")
        self.log("  • Debe contener: Mayúsculas, Minúsculas, Números, Símbolos")
        self.log("="*60)
        
        llaves_a_borrar = []
        total = len(Contrasenias)
        self.progress["maximum"] = total
        self.progress["value"] = 0
        
        count = 0
        for key, contra in Contrasenias.items():
            self.log(f"\n>>> ANALIZANDO: {key}")
            self.log(f"    Longitud: {len(contra)} caracteres")
            
            # Solo analizamos las que no parecen hashes
            if len(contra) != 64:
                self.log("    Tipo: TEXTO PLANO")
                self.log(f"    Valor: {contra}")
                
                tiene_minus = any(c.islower() for c in contra)
                tiene_mayus = any(c.isupper() for c in contra)
                tiene_raro = any(c in Caracteres for c in contra)
                tiene_num = any(c.isdigit() for c in contra)
                
                self.log(f"    ✓ Minúsculas: {'SÍ' if tiene_minus else 'NO'}")
                self.log(f"    ✓ Mayúsculas: {'SÍ' if tiene_mayus else 'NO'}")
                self.log(f"    ✓ Números: {'SÍ' if tiene_num else 'NO'}")
                self.log(f"    ✓ Símbolos: {'SÍ' if tiene_raro else 'NO'}")
                
                es_segura = len(contra) >= 9 and tiene_minus and tiene_mayus and tiene_raro and tiene_num
                
                if not es_segura:
                    llaves_a_borrar.append(key)
                    self.log(f"    ⚠ VEREDICTO: INSEGURA - MARCADA PARA ELIMINACIÓN")
                else:
                    self.log(f"    ✓ VEREDICTO: SEGURA")
            else:
                self.log("    Tipo: HASH (64 caracteres)")
                self.log("    ✓ VEREDICTO: HASH VÁLIDO - NO SE PUEDE ANALIZAR")
            
            count += 1
            self.progress["value"] = count
            time.sleep(0.02)
        
        self.log("\n" + "="*60)
        self.log("RESUMEN DEL ANÁLISIS DE SEGURIDAD")
        self.log("="*60)
        self.log(f"TOTAL ANALIZADAS: {count}")
        self.log(f"CONTRASEÑAS INSEGURAS ENCONTRADAS: {len(llaves_a_borrar)}")
        
        if llaves_a_borrar:
            self.log("\n>>> INICIANDO PROCESO DE ELIMINACIÓN...")
            for key in llaves_a_borrar:
                self.log(f"    ✗ ELIMINANDO: {key}")
                del Contrasenias[key]
            self.log("\n>>> GUARDANDO CAMBIOS EN BASE DE DATOS...")
            self.guardar_datos()
            self.log(f"✓ LIMPIEZA COMPLETADA: {len(llaves_a_borrar)} contraseñas inseguras eliminadas.")
            self.set_ascii_ok()
        else:
            self.log("✓ LIMPIEZA: No se encontraron contraseñas inseguras.")
            self.log("    Todas las contraseñas cumplen con los estándares de seguridad")
            self.log("    o están hasheadas.")
        
        self.log("="*60)
        self.progress["value"] = 0

    def opcion_7(self):
        """Redirige al método salir para mantener compatibilidad"""
        self.salir()

if __name__ == "__main__":
    root = tk.Tk()
    app = ProyectoFinal(root)
    root.mainloop()