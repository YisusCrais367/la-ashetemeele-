from flask import Flask, render_template, request

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

@app.route('/calculadora')
def calculadora():
    return render_template('calculadora.html')

@app.route('/calCULOS', methods=['POST'])
def calCULOS():
    try:
        num1 = float(request.form.get('value1'))
        num2 = float(request.form.get('value2'))
        resultado = num1 + num2
        
        return render_template('calculadora.html', resultado = resultado)    
    except(ValueError):
        return render_template('calculadora.html', resultado = None)
    
    

if __name__ == '__main__':
    app.run(debug=True)