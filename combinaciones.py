# función para encontrar combinaciones de letras que aproximan un número objetivo

import random
import time
from functools import lru_cache

# Encontrar combinaciones optimizadas de letras para alcanzar una frecuencia objetivo
def encontrar_combinaciones_optimizada(
    frecuencias, objetivo, max_resultados=100, max_profundidad=10, tiempo_limite=5
):
    combinaciones = []
    letras = list(frecuencias.keys())
    random.shuffle(letras)
    mejor_diferencia = float("inf")
    mejor_combinaciones = []
    mensaje_aproximacion = False

    letras_filtradas = [letra for letra in letras if frecuencias[letra] <= objetivo]
    tiempo_inicio = time.time()

    @lru_cache(None)
    def backtrack(combinacion, suma, profundidad):
        nonlocal mejor_diferencia, mejor_combinaciones, mensaje_aproximacion
        if time.time() - tiempo_inicio > tiempo_limite:
            return
        if len(combinaciones) >= max_resultados or profundidad >= max_profundidad:
            return
        if suma == objetivo:
            combinaciones.append("".join(combinacion))
            return
        if suma > objetivo:
            diferencia = abs(suma - objetivo)
            if diferencia < mejor_diferencia:
                mejor_diferencia = diferencia
                mejor_combinaciones = ["".join(combinacion)]
                mensaje_aproximacion = True
            elif diferencia == mejor_diferencia:
                mejor_combinaciones.append("".join(combinacion))
            return

        for letra in letras_filtradas:
            if suma + frecuencias[letra] <= objetivo or mejor_diferencia > abs(
                suma + frecuencias[letra] - objetivo
            ):
                backtrack(
                    combinacion + (letra,), suma + frecuencias[letra], profundidad + 1
                )

    backtrack((), 0, 0)

    if (
        len(combinaciones) < max_resultados
        and time.time() - tiempo_inicio > tiempo_limite
    ):
        print(
            "El tiempo límite de búsqueda se alcanzó; los resultados pueden ser parciales."
        )

    if combinaciones:
        return combinaciones
    else:
        if mensaje_aproximacion:
            print(
                "No se encontró una combinación exacta para el número objetivo. Se muestra una aproximación."
            )
        return (
            mejor_combinaciones
            if mejor_combinaciones
            else ["Ninguna combinación encontrada"]
        )
