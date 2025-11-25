<div align="center">

# Gestor de Contraseñas - Proyecto Final

### Proyecto Final Programación I

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-green?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Activo-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-Escolar-orange?style=for-the-badge)

</div>

---

## Descripción

Sistema completo de **gestión y seguridad de contraseñas** con interfaz gráfica estilo terminal retro. Este proyecto combina funcionalidad profesional con una estética console que incluye animaciones ASCII, consola integrada y un diseño visual tipo Matrix.

> **Proyecto escolar desarrollado para la clase de Programación I en CUCGDL**

### Características Principales

- **Interfaz estilo terminal** con tema verde neón sobre fondo negro
- **Animaciones ASCII** que cambian según el contexto
- **Hash de contraseñas** usando SHA-256
- **Generador de contraseñas** aleatorias y seguras
- **Verificación de seguridad** de contraseñas
- **Sistema de almacenamiento dual** basado en JSON (contraseñas y hashes separados)
- **Consola integrada** con registro detallado de operaciones
- **Cronómetro de tiempo** para cada operación en segundos
- **Rutas absolutas** basadas en la ubicación del script
- **Barra de progreso** para operaciones largas
- **Easter Egg:** Función "Hackear SIIAU" (totalmente inofensiva)

---

## Equipo de Desarrollo

<table align="center">
  <tr>
    <td><b>David Padilla Ruiz</b></td>
  </tr>
  <tr>
    <td><b>Juan Pablo Conde Espinosa</b></td>
  </tr>
  <tr>
    <td><b>Rogelio Abdiel Vazquez Pintor</b></td>
  </tr>
  <tr>
    <td><b>Edson Ivan Rubio Gonzalez</b></td>
  </tr>
</table>

---

## Instalación y Uso

### Prerrequisitos

```bash
Python 3.14 o superior
Tkinter (incluido en la mayoría de instalaciones de Python)
```

### Instalación

1. **Clona el repositorio:**

```bash
git clone https://github.com/DinoDavidRaptor/ProyectoFinalUDG.git
cd ProyectoFinalUDG
```

2. **Ejecuta el programa:**

```bash
python hashes.py
```

---

## Funcionalidades

<table>
  <tr>
    <th>Opción</th>
    <th>Descripción</th>
  </tr>
  <tr>
    <td><b>Verificar Archivo JSON</b></td>
    <td>Valida y muestra el contenido del archivo de contraseñas</td>
  </tr>
  <tr>
    <td><b>Buscar Contraseña</b></td>
    <td>Busca contraseñas por su hash SHA-256</td>
  </tr>
  <tr>
    <td><b>Hashear Todo</b></td>
    <td>Genera hashes de todas las contraseñas almacenadas</td>
  </tr>
  <tr>
    <td><b>Generar Contraseñas</b></td>
    <td>Crea contraseñas aleatorias seguras</td>
  </tr>
  <tr>
    <td><b>Verificar Seguridad</b></td>
    <td>Analiza la fortaleza de las contraseñas almacenadas</td>
  </tr>
  <tr>
    <td><b>Eliminar Inseguras</b></td>
    <td>Remueve contraseñas que no cumplan estándares de seguridad</td>
  </tr>
  <tr>
    <td><b>Hackear SIIAU</b></td>
    <td>Easter egg con animación especial (100% inofensivo)</td>
  </tr>
</table>

---

## Tecnologías Utilizadas

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-FF6B6B?style=for-the-badge)
![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white)
![Hashlib](https://img.shields.io/badge/Hashlib-4B8BBE?style=for-the-badge)
![Threading](https://img.shields.io/badge/Threading-306998?style=for-the-badge)

</div>

### Bibliotecas Principales

- **tkinter** - Interfaz gráfica
- **hashlib** - Funciones de hash criptográfico
- **json** - Manejo de datos
- **threading** - Operaciones asíncronas
- **random** & **string** - Generación de contraseñas

---

## Algoritmos de Hash Soportados


| Algoritmo | Bits | Uso                 |
| --------- | ---- | ------------------- |
| SHA-256   | 256  | Seguridad estándar |

---

## Criterios de Seguridad

El sistema evalúa contraseñas basándose en:

- Longitud mínima de 8 caracteres
- Presencia de letras mayúsculas y minúsculas
- Inclusión de números
- Caracteres especiales
- Variedad de tipos de caracteres

---

## Estructura del Proyecto

```
ProyectoFinalUDG/
│
├── hashes.py              # Archivo principal del programa
├── contrasenias.json      # Base de datos de contraseñas (texto plano)
├── hashes.json            # Base de datos de hashes SHA-256
└── README.md              # Este archivo
```

### Sistema de Archivos Dual

El proyecto utiliza dos archivos JSON separados:

- **contrasenias.json**: Almacena las contraseñas en texto plano para facilitar su gestión
- **hashes.json**: Almacena los hashes SHA-256 de las contraseñas para mayor seguridad

Las rutas de los archivos son absolutas y se basan en la ubicación del script, no en el directorio de ejecución.

---

## Características Técnicas

### Cronometraje de Operaciones

Cada función del sistema mide y reporta el tiempo de ejecución en segundos:

- **Verificación de archivos**: Tiempo de lectura y validación
- **Búsqueda de contraseñas**: Tiempo de búsqueda en ambas bases de datos
- **Hasheo masivo**: Tiempo total de procesamiento de todas las contraseñas
- **Generación de contraseñas**: Tiempo de creación y almacenamiento
- **Análisis de seguridad**: Tiempo de evaluación de criterios
- **Limpieza de contraseñas inseguras**: Tiempo de análisis y eliminación

Los cronómetros **NO** incluyen el tiempo de espera de inputs del usuario, solo miden el tiempo de procesamiento real.

### Gestión de Rutas

El sistema utiliza rutas absolutas calculadas desde la ubicación del script:

```python
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONTRASENIAS_FILE = os.path.join(SCRIPT_DIR, "contrasenias.json")
HASHES_FILE = os.path.join(SCRIPT_DIR, "hashes.json")
```

Esto garantiza que los archivos JSON siempre se crean en el mismo directorio que el script, independientemente desde dónde se ejecute el programa.

---

## Estructura UI

### Panel Principal

El sistema presenta una interfaz dividida en dos columnas:

- **Izquierda:** Botones de funcionalidad y consola de comandos
- **Derecha:** Arte ASCII animado que responde al contexto

### Consola Integrada

Cada operación se registra en tiempo real con:

- Mensajes de éxito en verde (Demasiados, le da un toque de consola)
- Errores claramente identificados
- Timestamps y progreso de operaciones

---

## Disclaimer

> **Nota Importante:** Este es un proyecto con fines educativos desarrollado para la clase de Programación I en CUCGDL. No debe utilizarse para almacenar contraseñas reales en entornos de producción. La función "Hackear SIIAU" es completamente ficticia y no realiza ninguna acción maliciosa.

---

## Institución

**Centro Universitario de Guadalajara - Universidad de Guadalajara**
Curso: Programación I
Semestre: 2025 - B

---

## Licencia

Este proyecto es de uso educativo. Desarrollado como proyecto final de la materia de Programación I.

---

<div align="center">

### Si te gustó el proyecto, no dudes en depositarme $5,000 pesos para mis vicios

**Hecho por:**

- David Padilla Ruiz
- Juan Pablo Conde Espinosa
- Rogelio Abdiel Vazquez Pintor
- Edson Ivan Rubio Gonzalez

```
╔═══════════════════════════════════════════════════════╗
║              "Vibecodeando el semestre"               ║
║                                            - Dino     ║
╚═══════════════════════════════════════════════════════╝
```

---

[![GitHub](https://img.shields.io/badge/GitHub-DinoDavidRaptor-181717?style=for-the-badge&logo=github)](https://github.com/DinoDavidRaptor)

[![GitHub](https://img.shields.io/badge/GitHub-Drg025-181717?style=for-the-badge&logo=github)](https://github.com/Drg025)

[![GitHub](https://img.shields.io/badge/https%3A%2F%2Fgithub.com%2FShogun-S4ma?style=social)](https://github.com/Shogun-S4ma)

[![UDG](https://img.shields.io/badge/UDG-CUCGDL-004B87?style=for-the-badge)](http://www.cucgdl.udg.mx/)

</div>
