from flask import Flask, render_template, request

app = Flask(__name__)

app.debug = True

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        notaUno = float(request.form['nota1'])
        notaDos = float(request.form['nota2'])
        notaTres = float(request.form['nota3'])
        asistenciaPCT = float(request.form['asistencia'])

        promedioNotas = round((notaUno + notaDos + notaTres) / 3)

        if (promedioNotas > 40 and asistenciaPCT >= 75):
            situacion = "APROBADO"
            return render_template('ejercicio1.html', promedioNotas= promedioNotas, situacion= situacion)
        else:
            situacion = "REPROBADO"
            return render_template('ejercicio1.html', promedioNotas= promedioNotas, situacion= situacion)

    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == "POST":
        nombreUno = request.form["nombre1"]
        nombreDos = request.form['nombre2']
        nombreTres = request.form['nombre3']

        nombre1Largo = len(nombreUno)
        nombre2Largo = len(nombreDos)
        nombre3Largo = len(nombreTres)

        if (nombre1Largo > nombre2Largo and nombre1Largo > nombre3Largo):
            return render_template('ejercicio2.html', nombreMayor= nombreUno, nombreLargo= nombre1Largo)
        elif (nombre2Largo > nombre1Largo and nombre2Largo > nombre3Largo):
            return render_template('ejercicio2.html', nombreMayor= nombreDos, nombreLargo= nombre2Largo)
        elif (nombre3Largo > nombre1Largo and nombre3Largo > nombre2Largo):
            return render_template('ejercicio2.html', nombreMayor= nombreTres, nombreLargo= nombre3Largo)

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run()