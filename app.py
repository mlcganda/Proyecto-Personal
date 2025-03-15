import pandas as pd
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Cargar el DataFrame desde una ruta relativa
df = pd.read_csv('Compuestos.csv')

def buscar_formula(formula, dfdatos):
    resultados = dfdatos[dfdatos['Formula'] == formula]
    if not resultados.empty:
        return resultados.to_dict(orient='records')
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        formula = request.form['formula']
        nomenclatura = request.form['nomenclatura']
        resultados = buscar_formula(formula, df)

        if resultados:
            if nomenclatura == 'Todas':
                resultado_filtrado = [{k: row[k] for k in ['Tradicional', 'Sistematica', 'Stock']} for row in resultados]
            elif nomenclatura in ['Tradicional', 'Sistematica', 'Stock']:
                resultado_filtrado = [row[nomenclatura] for row in resultados]
            else:
                resultado_filtrado = ["Nomenclatura no válida."]
        else:
            resultado_filtrado = [f"No se encontró la fórmula: {formula}"]

        return jsonify(resultado_filtrado)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
