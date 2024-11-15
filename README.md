# Generador de Frecuencias para Frases

Este proyecto convierte palabras y frases en frecuencias sonoras. El programa envía las frecuencias generadas a SuperCollider usando el protocolo OSC (Open Sound Control). También sugiere colores únicos para representar cada palabra y permite buscar combinaciones de letras que se aproximen a una frecuencia objetivo.

## Requisitos

- Python 3.x
- Biblioteca [python-osc](https://pypi.org/project/python-osc/)
- SuperCollider (para recibir los mensajes OSC)
- Flask (para la interfaz web)

## Instalación

1. Descarga los archivos o clona este repositorio así:
    ```bash
    git clone https://github.com/usuario/generador-frecuencias.git
    cd generador-frecuencias
    ```

2. Instala las bibliotecas necesarias:
    ```bash
    pip install -r requirements.txt
    ```

3. Asegúrate de tener SuperCollider configurado para recibir mensajes OSC en el puerto `57120`.

## Estructura del Proyecto

El proyecto está dividido en varios módulos para facilitar su mantenimiento:

- **app.py**: Configuración de la aplicación Flask y rutas para procesar las solicitudes.
- **color.py**: Generación de colores hexadecimales únicos para cada palabra.
- **combinaciones.py**: Búsqueda de combinaciones de letras que se aproximen a una frecuencia objetivo.
- **config.py**: Configuración del cliente OSC para enviar mensajes a SuperCollider.
- **frequencias.py**: Generación de frecuencias a partir de letras y palabras.
- **input_usuario.py**: Procesamiento del input del usuario para la búsqueda de combinaciones.
- **main.py**: Interfaz de usuario y lógica principal del programa.
- **FullSynth.scd**: Sintetizador de SuperCollider.
- **templates/**: Plantillas HTML para la interfaz web.
- **static/**: Archivos estáticos como CSS.

## Uso

1. Inicia SuperCollider y configura el receptor OSC en el puerto `57120`.
2. Ejecuta el programa en Python:
    ```bash
    python main.py
    ```

## Ejemplo de Uso

Al ejecutar el programa, verás el siguiente menú:
```
=== Generador de Frecuencias para Frases ===
Escribe '0' en cualquier momento para detener el sonido y salir del programa.
---------------------------------------------------
Selecciona una opción:
 1) Convertir una palabra o frase a frecuencia ('acorde de palabras')
 3) Encontrar combinaciones de letras para un número objetivo
 4) Configuración
---------------------------------------------------
Introduce una opción (o '0' para terminar): 
```
- **Opción 1**: Convierte una palabra o frase en frecuencias y muestra un color hexadecimal único para cada palabra.
- **Opción 3**: Busca combinaciones de letras que se aproximen a un número objetivo, con un límite de resultados para optimizar el rendimiento.
- **Opción 4**: Permite modificar la configuración del programa, como la frecuencia base y el incremento.

## Notas

- **Optimización**: El número máximo de combinaciones se limita a 100 para evitar sobrecargar el sistema.
- **Tiempo límite**: La búsqueda de combinaciones tiene un límite de tiempo de 5 segundos para mejorar la eficiencia.
