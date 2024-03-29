from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        # Procesar datos del formulario de ejercicio 1
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])

        # Calcular el promedio y estado de aprobación
        promedio = (nota1 + nota2 + nota3) / 3.0
        estado = 'APROBADO' if promedio >= 50 and asistencia >= 75 else 'REPROBADO'

        return render_template('ejercicio1.html', promedio=promedio, estado=estado)

    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        # Procesar datos del formulario de ejercicio 2
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        # Encontrar el nombre con más caracteres
        nombres = [nombre1, nombre2, nombre3]
        nombre_largo = max(nombres, key=len)
        caracteres = len(nombre_largo)

        return render_template('ejercicio2.html', nombre_largo=nombre_largo, caracteres=caracteres)

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)
