# configurar el cliente OSC y almacenar configuraciones generales.
from pythonosc import udp_client

# Configuración del cliente OSC
client = udp_client.SimpleUDPClient("127.0.0.1", 57120)
