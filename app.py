from flask import Flask, render_template, request, jsonify
from config import *
from frequencias import *
from color import generar_color_hexadecimal
from combinaciones import encontrar_combinaciones_optimizada
from main import enviar_frecuencias


app = Flask(__name__)
frecuencias = crear_diccionario_frecuencias()

@app.route('/')
def index():
    config = cargar_configuracion()
    return render_template('index.html', config=config)

@app.route('/procesar_frase', methods=['POST'])
def procesar_frase():
    texto = request.form['texto']
    frecuencias_palabras = frase_a_frecuencias(texto, frecuencias)
    colores = generar_color_hexadecimal(texto)
    enviar_frecuencias(frecuencias_palabras)
    return jsonify({
        'frecuencias': frecuencias_palabras,
        'colores': colores
    })

@app.route('/enviar_frecuencia', methods=['POST'])
def enviar_frecuencia():
    frecuencia = float(request.form['frecuencia'])
    enviar_frecuencias([frecuencia])
    return jsonify({'status': 'success'})

@app.route('/buscar_combinaciones', methods=['POST'])
def buscar_combinaciones():
    objetivo = int(request.form['objetivo'])
    combinaciones = encontrar_combinaciones_optimizada(frecuencias, objetivo)
    return jsonify({'combinaciones': combinaciones})

@app.route('/actualizar_config', methods=['POST'])
def actualizar_config():
    config = cargar_configuracion()
    config['frecuencia_base'] = float(request.form['frecuencia_base'])
    config['incremento'] = float(request.form['incremento'])
    config['ataque'] = float(request.form['ataque'])
    config['decaimiento'] = float(request.form['decaimiento'])
    guardar_configuracion(config)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)