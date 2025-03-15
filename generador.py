import pandas as pd
import os

df = pd.read_csv('data/Compuestos.csv')

def generar_pagina(formula):
    resultados = df[df['Formula'] == formula]
    if not resultados.empty:
        html_resultados = resultados.to_html()
        with open(f'{formula}.html', 'w') as f:
            f.write(f"""
<!DOCTYPE html>
<html>
<head>
    <title>Resultados para {formula}</title>
</head>
<body>
    <h1>Resultados para {formula}</h1>
    {html_resultados}
</body>
</html>
            """)

# Generar páginas para todas las fórmulas únicas (opcional)
for formula in df['Formula'].unique():
    generar_pagina(formula)

print('Páginas generadas.')
