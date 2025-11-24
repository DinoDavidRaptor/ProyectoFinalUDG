<h1>Proyecto Final de Gestión y Seguridad de Contraseñas</h1>

Este programa es una aplicación de escritorio creada con Python y Tkinter que funciona como un sistema completo para gestionar, generar, verificar y almacenar contraseñas. Incluye una consola visual interna, múltiples herramientas de seguridad, animaciones en ASCII y un diseño tipo terminal con estilo retro.

La aplicación organiza su interfaz en dos columnas, de modo que la parte izquierda contiene toda la funcionalidad principal y la derecha muestra arte ASCII animado que cambia según la acción realizada.

*Características principales
*Interfaz gráfica estilo terminal.
*Animación de arte ASCII en tiempo real.
*Múltiples herramientas de gestión de contraseñas.
*Sistema de almacenamiento basado en JSON.
*Consola integrada que registra cada acción.
*Barra de progreso para tareas largas.
*Función humorística llamada “Hackear SIIAU”.
*Mecanismo de cierre animado.

<h2>Flujo general del programa</h2>

1. Inicio
Al ejecutarse el archivo, se crea la ventana principal y se configuran todos los estilos.
Se cargan o inicializan los datos almacenados en contrasenias.json.

2. Animación inicial
El programa muestra una animación ASCII cíclica usando un sistema de actualización programada mediante la función after de Tkinter.

3. Menú de funciones
Se muestran botones numerados que representan las acciones del sistema.
El usuario interactúa con ellos y cada uno ejecuta una tarea distinta.

4. Registro en consola
Cada proceso escribe mensajes en la consola interna para dar retroalimentación detallada.

5. Guardado de datos
El sistema guarda cualquier cambio realizado en un archivo JSON.
Antes y después del guardado, se registran múltiples pasos para monitorear el proceso.

6. Cierre del sistema
La aplicación muestra arte ASCII de despedida, simula limpieza de recursos y cierra la ventana después de unos segundos.

<h2>Funciones incluidas en el código</h2>
Manejo visual y estético

animate_ascii
Controla el cambio automático del arte ASCII.

set_ascii_main, set_ascii_ok, set_ascii_error, set_ascii_exit, set_ascii_hackear_siiau
Cambian el tipo de animación según el evento.

log(mensaje)
Escribe texto en la consola integrada.

Manejo de almacenamiento

cargar_datos
Carga las contraseñas desde el archivo JSON, valida errores y asigna valores por defecto cuando es necesario.

guardar_datos
Guarda la base de contraseñas con formato legible.
Documenta cada etapa en la consola.

guardar_contrasenas
Alias directo a la función anterior.

Funciones del menú principal

<h2>El proyecto tiene botones que llaman a las siguientes funciones:</h2>

<h3>opcion_1</h3>
Verifica el archivo JSON.

<h3>opcion_2</h3>
Busca una contraseña usando su hash.

<h3>opcion_3</h3>
Hashea todas las contraseñas almacenadas.

<h3>opcion_4</h3>
Genera contraseñas nuevas con parámetros específicos.

<h3>opcion_5</h3>
Verifica si una contraseña es segura.

<h3>opcion_6</h3>
Elimina contraseñas considerados inseguras.

<h3>hackear_siiau</h3>
Simulación humorística de ataque con mensajes y ASCII.

<h3>salir</h3>
Limpia recursos y cierra la aplicación.

<h2>Requisitos</h2>
-Python 3.8 o superior
-Biblioteca estándar de Python
(se usa Tkinter, json, os, hashlib, random, threading, etc.)
