# archivo principal que importa y organiza las funciones de los demás módulos

from config import client
from frequencias import crear_diccionario_frecuencias, frase_a_frecuencias
from color import generar_color_hexadecimal
from combinaciones import encontrar_combinaciones_optimizada
from input_usuario import obtener_numero_objetivo

# Enviar las frecuencias a SuperCollider
def enviar_frecuencias(frecuencias):
    print(f"\n-> Enviando frecuencias: {frecuencias} Hz a SuperCollider\n")
    client.send_message("/frecuencia_palabra", frecuencias)

# Crear el diccionario de frecuencias para el programa
frecuencias = crear_diccionario_frecuencias()

# Interfaz del programa para el usuario
print("=== Generador de Frecuencias para Frases ===")
print("Escribe '0' en cualquier momento para detener el sonido y salir del programa.\n")

while True:
    print("---------------------------------------------------")
    print("Selecciona una opción:")
    print(" 1) Convertir una palabra o frase a frecuencia ('acorde de palabras')")
    print(" 2) Enviar frecuencia exacta numérica")
    print(" 3) Encontrar combinaciones de letras para un número objetivo")
    print("---------------------------------------------------")
    opcion = input("Introduce una opción (o '0' para terminar): ")

    if opcion == "0":
        enviar_frecuencias([0])
        print("==== [El sonido ha sido detenido] ====\n")
        break

    elif opcion == "1":
        texto = input("\nIntroduce una palabra o frase: ")
        frecuencias_palabras = frase_a_frecuencias(texto, frecuencias)
        colores = generar_color_hexadecimal(texto)
        print(f"\nFrecuencias para:'{texto}'\n{frecuencias_palabras}")
        print(f"\nColor hexadecimal para cada palabra:\n{colores}\n")
        enviar_frecuencias(frecuencias_palabras)

    elif opcion == "2":
        try:
            frecuencia = float(input("\nIntroduce una frecuencia exacta en Hz: "))
            enviar_frecuencias([frecuencia])
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número válido.")

    elif opcion == "3":
        print("\nPor favor, selecciona un número entre 1 y 1000.")
        print(
            "El número de resultados se limita a 100 combinaciones para optimizar el rendimiento del programa.\n"
        )

        objetivo = obtener_numero_objetivo()
        combinaciones = encontrar_combinaciones_optimizada(frecuencias, objetivo)
        print(
            f"\nCombinaciones de letras para el objetivo {objetivo}: {combinaciones if combinaciones else 'Ninguna combinación encontrada'}\n"
        )

    else:
        print("Opción no válida, por favor elige una opción del menú.\n")
