from flask import Flask, render_template, request, flash, redirect, url_for 

app = Flask(__name__)

app.config['SECRET_KEY']='una_clave_secreta_muy_larga_y_compleja_1234567890'

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
            flash("Todos los campos obligatorios deben completarse.", "danger")
            return redirect(url_for("registro"))
        if len(nombre) < 3:
            flash("El nombre debe tener al menos 3 caracteres.", "warning")
            return redirect(url_for("registro"))
        if "@" not in correo:
            flash("El correo ingresado no es válido.", "danger")
            return redirect(url_for("registro"))

        flash(f"¡Registro exitoso, {nombre}!", "success")
        return redirect(url_for("index"))

    return render_template('registro.html')

@app.route('/iniciodesesion')
def isesion():
    return render_template('isesion.html')

if __name__ == '__main__':
    app.run(debug=True)