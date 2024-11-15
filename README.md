# Generador de Frecuencias para Frases

Este proyecto es una aplicación web que convierte frases en frecuencias y colores, y busca combinaciones de letras que aproximen un número objetivo. La aplicación está construida con Flask y utiliza SuperCollider para la síntesis de sonido.

## Estructura del Proyecto

- `app.py`: Archivo principal de la aplicación Flask.
- `color.py`: Contiene la función para generar colores hexadecimales a partir de frases.
- `combinaciones.py`: Contiene la función para encontrar combinaciones de letras que aproximen un número objetivo.
- `config.py`: Maneja la configuración de la aplicación.
- `frequencias.py`: Contiene funciones relacionadas con la creación y conversión de frecuencias.
- `input_usuario.py`: Contiene la función para obtener el número objetivo del usuario.
- `main.py`: Archivo principal que organiza las funciones de los demás módulos.
- `FullSynth.scd`: Script de SuperCollider para la síntesis de sonido.
- `requirements.txt`: Lista de dependencias del proyecto.
- `static/styles.css`: Archivo de estilos CSS.
- `templates/base.html`: Plantilla base de HTML.
- `templates/index.html`: Plantilla principal de la aplicación.

## Instalación

1. Descarga los archivos o Clona el repositorio:
    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_REPOSITORIO>
    ```

2. Crea un entorno virtual y actívalo (Opcional pero recomendado):
    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

4. Inicia la aplicación Flask:
    ```sh
    python app.py
    ```

5. Abre tu navegador y ve a `http://127.0.0.1:5000`.

## Uso

### Convertir Frase a Frecuencias

1. Introduce una palabra o frase en el campo de texto.
2. Selecciona el modo de reproducción (simultáneo o individual).
3. Haz clic en "Convertir" para ver las frecuencias y colores generados.

### Buscar Combinaciones

1. Introduce un número objetivo entre 1 y 1000.
2. Haz clic en "Buscar" para encontrar combinaciones de letras que aproximen el número objetivo.

### Configuración

1. Ajusta los valores de frecuencia base, incremento, ataque y decaimiento.
2. Haz clic en "Guardar" para actualizar la configuración.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que te gustaría hacer.
