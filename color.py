# Generar un color hexadecimal único para cada palabra
def generar_color_hexadecimal(frase):
    palabras = frase.lower().split()
    colores = []
    for palabra in palabras:
        r = sum(ord(char) * (i + 1) for i, char in enumerate(palabra)) % 256
        g = sum(ord(char) * (i + 2) for i, char in enumerate(palabra)) % 256
        b = sum(ord(char) * (i + 3) for i, char in enumerate(palabra)) % 256
        color_hex = "#{:02x}{:02x}{:02x}".format(r, g, b)
        colores.append(color_hex)
    return colores
