from flask import Flask, render_template, request, flash, redirect, url_for 

app = Flask(__name__)

app.secret_key = "una_clave_super_segura"

@app.route('/')
def index():
    return render_template('inicio.html')

@app.route('/animales')
def animales():
    return render_template('animales.html')

@app.route('/autos_antiguos')
def autos_antiguos():
    return render_template('autos_antiguos.html')

@app.route('/maravillas')
def maravillas():
    return render_template('maravillas.html')

@app.route('/acercade')
def acerca():
    return render_template('acerca.html')

@app.route('/registro', methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/iniciodesesion')
def isesion():
    return render_template('isesion.html')

if __name__ == '__main__':
    app.run(debug=True)