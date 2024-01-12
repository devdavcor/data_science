from functions_covid_data_analysis import *

data = pd.read_csv('COVID19MEXICO.csv')
#headers = data.columns.to_numpy()
#headers = ['USMER', 'SECTOR', 'SEXO', 'TIPO_PACIENTE', 'SI_NO', 'NACIONALIDAD', 'RESULTADO_LAB', 'RESULTADO_ANTIGENO', 'CLASIFICACION_FINAL', 'ENTIDADES']

for head in range (40):
    try:
        if head + 1 != 1 and head + 1 != 2:
            array_column = extract_column_data('COVID19MEXICO.csv', head+1)
            print("\n\n")
            extract_column_information(array_column, head+1)
    except Exception as e:
        print(f"Error al procesar la columna {head}: {e}")
        continue  # Pasa a la siguiente iteración del bucle




