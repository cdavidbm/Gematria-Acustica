# archivo principal que importa y organiza las funciones de los demás módulos

from config import *
from frequencias import *
from color import generar_color_hexadecimal
from combinaciones import encontrar_combinaciones_optimizada
from input_usuario import obtener_numero_objetivo


# Función para enviar frecuencias a SuperCollider
def enviar_frecuencias(frecuencias, modo='simultaneo', efectos=None):
    config = cargar_configuracion()
    print(f"\n-> Enviando frecuencias: {frecuencias} Hz a SuperCollider")
    print(f"   Modo: {modo}")
    print(f"   Ataque: {config['ataque']}s, Decaimiento: {config['decaimiento']}s\n")
    
    if efectos is None:
        efectos = {
            "delay": {"active": False, "amount": 0},
            "distortion": {"active": False, "amount": 0},
            "noise": {"active": False, "amount": 0}
        }
    
    # Extraer valores de efectos
    delay_amount = efectos["delay"]["amount"] if efectos["delay"]["active"] else 0
    dist_amount = efectos["distortion"]["amount"] if efectos["distortion"]["active"] else 0
    noise_amount = efectos["noise"]["amount"] if efectos["noise"]["active"] else 0

    # Asegurar que las frecuencias sean una lista
    if not isinstance(frecuencias, list):
        frecuencias = [frecuencias]

    client.send_message("/frecuencia_palabra", 
                       [modo, *frecuencias, config['ataque'], config['decaimiento'],
                        delay_amount, dist_amount, noise_amount])

# Función para actualizar configuración
def actualizar_configuracion():
    config = cargar_configuracion()
    print("\n=== Configuración Actual ===")
    print(f"1) Frecuencia base: {config['frecuencia_base']}")
    print(f"2) Incremento: {config['incremento']}")
    print(f"3) Ataque (segundos): {config['ataque']}")
    print(f"4) Decaimiento (segundos): {config['decaimiento']}")
    print("\nIntroduce el número de la opción que deseas modificar o '0' para regresar.")

    opcion = input("Opción: ")
    if opcion == "1":
        try:
            config["frecuencia_base"] = int(input("Introduce el nuevo valor para frecuencia base: "))
        except ValueError:
            print("Entrada inválida. Se requiere un número entero.")
    elif opcion == "2":
        try:
            config["incremento"] = int(input("Introduce el nuevo valor para incremento: "))
        except ValueError:
            print("Entrada inválida. Se requiere un número entero.")
    elif opcion == "3":
        try:
            ataque = float(input("Introduce el nuevo valor para ataque (segundos): "))
            if ataque >= 0:
                config["ataque"] = ataque
            else:
                print("El ataque debe ser un número positivo.")
        except ValueError:
            print("Entrada inválida. Se requiere un número decimal.")
    elif opcion == "4":
        try:
            decaimiento = float(input("Introduce el nuevo valor para decaimiento (segundos): "))
            if decaimiento >= 0:
                config["decaimiento"] = decaimiento
            else:
                print("El decaimiento debe ser un número positivo.")
        except ValueError:
            print("Entrada inválida. Se requiere un número decimal.")
    elif opcion == "0":
        return

    guardar_configuracion(config)
    print("Configuración actualizada con éxito.\n")

# Función para regenerar el diccionario de frecuencias después de la actualización
def actualizar_frecuencias():
    return crear_diccionario_frecuencias()

# Crear el diccionario de frecuencias para el programa
frecuencias = crear_diccionario_frecuencias()


'''
# Interfaz del programa para el usuario
print("=== Generador de Frecuencias para Frases ===")
print("Escribe '0' y presiona 'Enter' en cualquier momento para detener el sonido.\n")

while True:
    print("---------------------------------------------------")
    print("Selecciona una opción:")
    print(" 1) Convertir una palabra o frase a frecuencia ('acorde de palabras')")
    print(" 3) Encontrar combinaciones de letras para un número objetivo")
    print(" 4) Configuración")
    print("---------------------------------------------------")
    opcion = input("Introduce una opción (o '0' seguido de 'Enter' para detener): ")

    elif opcion == "1":
        texto = input("\nIntroduce una palabra o frase: ")
        frecuencias_palabras = frase_a_frecuencias(texto, frecuencias)
        colores = generar_color_hexadecimal(texto)
        print(f"\nFrecuencias para:'{texto}'\n{frecuencias_palabras}")
        print(f"\nColor hexadecimal para cada palabra:\n{colores}\n")
        enviar_frecuencias(frecuencias_palabras)


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
    
    elif opcion == "4":
        actualizar_configuracion()
        frecuencias = actualizar_frecuencias()

    else:
        print("Opción no válida, por favor elige una opción del menú.\n")
'''