from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/animales_exoticos')
def aniexo():
    return render_template('aniexo.html')

@app.route('/autos_antiguos')
def autos_antiguos():
    return render_template('autos_antiguos.html')

if __name__ == '__main__':
    app.run(debug=True)