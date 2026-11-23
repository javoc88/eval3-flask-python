from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    promedio = None
    estado = None
    asistencia = None
    error = None

    if request.method == 'POST':
        try:
            nota1 = float(request.form.get('nota1', 0))
            nota2 = float(request.form.get('nota2', 0))
            nota3 = float(request.form.get('nota3', 0))
            asistencia = float(request.form.get('asistencia', 0))
            promedio = round((nota1 + nota2 + nota3) / 3, 1)

            if promedio >= 40 and asistencia >= 75:
                estado = "APROBADO"
            else:
                estado = "REPROBADO"

        except ValueError:
            error = "Por favor, ingresa números válidos en todos los campos."

    return render_template(
        'ejercicio1.html',
        promedio=promedio,
        estado=estado,
        asistencia=asistencia,
        error=error,
    )

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombre_mayor = None
    longitud_mayor = None
    error = None

    if request.method == 'POST':
        nombre1 = request.form.get('nombre1', '').strip()
        nombre2 = request.form.get('nombre2', '').strip()
        nombre3 = request.form.get('nombre3', '').strip()

        if nombre1 and nombre2 and nombre3:
            nombres = [nombre1, nombre2, nombre3]
            nombre_mayor = max(nombres, key=len)
            longitud_mayor = len(nombre_mayor)
        else:
            error = "Por favor, ingresa los 3 nombres antes de enviar."

    return render_template(
        'ejercicio2.html',
        nombre_mayor=nombre_mayor,
        longitud_mayor=longitud_mayor,
        error=error,
    )

if __name__ == '__main__':
    app.run(debug=True)