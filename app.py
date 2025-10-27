from flask import Flask, render_template, request, flash, redirect, url_for, session

app = Flask(__name__)

app.config['SECRET_KEY']='una_clave_secreta_muy_larga_y_compleja_1234567890'

USUARIOS_REGISTRADOS = {
    'admin@correo.com': {
        'nombre': 'Admin',
        'contraseña': 'admin123'
    }
}

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
        nombre = request.form.get("nombre")
        apellidos = request.form.get("apellidos")
        dia = request.form.get("dia")
        mes = request.form.get("mes")
        año = request.form.get("año")
        genero = request.form.get("genero")
        correo = request.form.get("correo")
        contraseña = request.form.get("contraseña")
        if not nombre or not apellidos or not correo or not contraseña:
            flash("Todos los campos son obligatorios.", "danger")
            return redirect(url_for("registro"))
        if correo in USUARIOS_REGISTRADOS:
            flash("El correo ya está registrado. Intenta con otro o inicia sesión.", "warning")
            return redirect(url_for("registro"))
        USUARIOS_REGISTRADOS[correo] = {
            "nombre": nombre,
            "apellidos": apellidos,
            "fecha_nacimiento": f"{dia}/{mes}/{año}",
            "genero": genero,
            "contraseña": contraseña
        }
        session["usuario"] = nombre
        flash(f"¡Registro exitoso, {nombre}!", "success")
        return redirect(url_for("index"))

    return render_template('registro.html')

@app.route('/iniciodesesion', methods=["GET", "POST"])
def isesion():
    if request.method == "POST":
        correo = request.form.get("correo")
        contraseña = request.form.get("contraseña")
    if not correo or not contraseña:
            flash("Debes ingresar tu correo y contraseña.", "danger")
            return redirect(url_for("isesion"))
    return render_template('isesion.html')

if __name__ == '__main__':
    app.run(debug=True)