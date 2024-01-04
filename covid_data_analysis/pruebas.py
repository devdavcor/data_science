import pandas as pd
import numpy as np


data = pd.read_csv('COVID19MEXICO.csv')
columna = data['ORIGEN']
arreglo = columna.to_numpy()
elementos_unicos, frecuencias = np.unique(arreglo, return_counts=True)

# Ahora 'elementos_unicos' contiene los elementos únicos y 'frecuencias' contiene sus frecuencias
for elemento, frecuencia in zip(elementos_unicos, frecuencias):
    print(f"Elemento: {elemento}, Frecuencia: {frecuencia}")


