from flask import Flask, render_template


app = Flask(__name__)


#request -> petición
#response -> respuesta
#client -> cliente 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Hola Mucho gusto, Bienvenido a la casa de los sustos :3')
def hola():
    return render_template('hola.html')

if __name__ == '__main__':
    app.run()