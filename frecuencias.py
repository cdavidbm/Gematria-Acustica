# funciones relacionadas con la creación y conversión de frecuencias.

import string
from config import cargar_configuracion

# Crear un diccionario de frecuencias asignadas a cada letra
def crear_diccionario_frecuencias():
    config = cargar_configuracion()
    frecuencia_base = config["frecuencia_base"]
    incremento = config["incremento"]
    
    frecuencias = {}
    for i, letra in enumerate(string.ascii_lowercase):
        frecuencias[letra] = frecuencia_base + (i * incremento)
    return frecuencias

# Convertir una palabra a su frecuencia total
def palabra_a_frecuencia(palabra, frecuencias):
    palabra = palabra.lower()
    frecuencia_total = sum(frecuencias.get(letra, 0) for letra in palabra)
    return frecuencia_total

# Convertir cada palabra de una frase a frecuencias
def frase_a_frecuencias(frase, frecuencias):
    palabras = frase.lower().split()
    frecuencias_palabras = [
        palabra_a_frecuencia(palabra, frecuencias) for palabra in palabras
    ]
    return frecuencias_palabras
