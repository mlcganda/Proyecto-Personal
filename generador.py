import pandas as pd
import os

df = pd.read_csv('data/Compuestos.csv')

def buscar_formula(formula,dfdatos):
  """
  Busca una fórmula específica en la columna 'Fórmula' del DataFrame df.

  Args:
    formula: La fórmula a buscar.

  Returns:
    Un DataFrame con las filas que contienen la fórmula especificada, o None si no se encuentra.
  """
  resultados = dfdatos[dfdatos['Formula'] == formula]
  if not resultados.empty:
      return resultados
  else:
      return None
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
