import pandas as pd

# Lee el archivo CSV
df = pd.read_csv('../COVID19MEXICO.csv')

# Obtiene el número de filas con datos
numero_filas = len(df)

# Imprime el resultado
print(f'El número de filas con datos en el archivo CSV es: {numero_filas}')

# Itera sobre cada fila e imprímela
for indice, fila in df.iterrows():
    print(f'Fila {indice + 1}:')
    print(fila)
    print('-' * 20)  # Separador entre filas