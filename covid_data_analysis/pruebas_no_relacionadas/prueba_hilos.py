import pandas as pd
from concurrent.futures import ThreadPoolExecutor

def imprimir_fila(indice, fila):
    print(f'Fila {indice + 1}:')
    print(fila)
    print('-' * 20)  # Separador entre filas

# Lee el archivo CSV
df = pd.read_csv('../COVID19MEXICO.csv')

# Número de hilos que deseas utilizar
num_hilos = 16  # Puedes ajustar este número según tu preferencia

# Utiliza ThreadPoolExecutor para imprimir las filas en paralelo
with ThreadPoolExecutor(max_workers=num_hilos) as executor:
    # Mapea la función imprimir_fila a cada fila del DataFrame
    resultados = list(executor.map(imprimir_fila, df.index, df.itertuples(index=False)))
