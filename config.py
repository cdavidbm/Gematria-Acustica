# configurar el cliente OSC
from pythonosc import udp_client

# Configuración del cliente OSC
client = udp_client.SimpleUDPClient("127.0.0.1", 57120)



# configurar parametros iniciales

import json
import os

# Path del archivo de configuración
CONFIG_FILE_PATH = "config.json"

# Valores predeterminados para la configuración
default_config = {
    "frecuencia_base": 100,
    "incremento": 1
}

# Cargar la configuración desde el archivo o usar valores predeterminados
def cargar_configuracion():
    if os.path.exists(CONFIG_FILE_PATH):
        with open(CONFIG_FILE_PATH, "r") as file:
            return json.load(file)
    else:
        return default_config

# Guardar la configuración en el archivo
def guardar_configuracion(config):
    with open(CONFIG_FILE_PATH, "w") as file:
        json.dump(config, file, indent=4)
