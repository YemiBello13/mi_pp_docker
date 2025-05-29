from flask import Flask, jsonify, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html', message="¡Hola Mundo desde Docker y GitHub Actions!")

@app.route('/api/data')
def get_data():
    return jsonify({"id": 1, "name": "Dato de ejemplo", "status": "OK"})

def una_funcion_simple(a, b):
    """Una función simple para probar la cobertura."""
    if a > b:
        return a - b
    else:
        return a + b

# Este bloque se ejecuta solo si el script se corre directamente
if __name__ == '__main__':
    # Iniciamos el servidor de desarrollo de Flask
    app.run(host='0.0.0.0', port=5000, debug=True)