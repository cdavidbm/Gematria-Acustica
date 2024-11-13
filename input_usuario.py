# función para obtener el número objetivo del usuario.

# Solicitar al usuario el número objetivo, con validación de entrada
def obtener_numero_objetivo():
    while True:
        try:
            objetivo = int(input("Introduce el número objetivo (entre 1 y 1000): "))
            return objetivo
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número entero válido.")
