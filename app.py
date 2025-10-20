from flask import Flask, render_template, request, flash, redirect, url_for, session

app = Flask(__name__)

app.config['SECRET_KEY']='una_clave_secreta_muy_larga_y_compleja_1234567890'

@app.route('/')
def index():
    if "usuario" not in session:
        return redirect(url_for("registro"))
    return render_template('inicio.html')

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
        if correo in usuarios:
            flash("El correo ya está registrado. Intenta con otro o inicia sesión.", "warning")
            return redirect(url_for("registro"))

    return render_template('registro.html')

@app.route('/iniciodesesion', methods=["GET", "POST"])
def isesion():
    if request.method == "POST":
        correo = request.form.get("correo")
        contraseña = request.form.get("contraseña")
    if correo in usuarios and usuarios[correo]["contraseña"] == contraseña:
            session["usuario"] = usuarios[correo]["nombre"]
            flash(f"Bienvenido de nuevo, {usuarios[correo]['nombre']}!", "success")
            return redirect(url_for("index"))
    
    if correo in usuarios and usuarios[correo]["contraseña"] == contraseña:
            session["usuario"] = usuarios[correo]["nombre"]
            flash(f"Bienvenido de nuevo, {usuarios[correo]['nombre']}!", "success")
            return redirect(url_for("index"))
    else:
            flash("Correo o contraseña incorrectos.", "danger")
            return redirect(url_for("isesion"))
        

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



if __name__ == '__main__':
    app.run(debug=True)