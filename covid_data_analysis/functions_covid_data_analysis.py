import numpy as np
import pandas as pd

def extract_column_data(path_db, column_name):
    csv_data = pd.read_csv(path_db)
    csv_column = csv_data[column_name]
    array_column = csv_column.to_numpy()
    return array_column

def extract_column_information (array_column, column_name):
    array_unique_data, frecuencies = np.unique(array_column, return_counts=True)
    total = 0
    print(f"----------Información de la columna {column_name}----------")
    for element, frecuency in zip(array_unique_data, frecuencies):
        print(f"{dictionary[column_name][int(element)]} tiene {'{:,}'.format(frecuency)} casos")
        total += frecuency
    formatted_total = '{:,}'.format(total)
    print(f"El total de casos para {column_name} es de {formatted_total}")

dictionary = {
	'USMER': {
		1 : 'USMER',
		2 : 'Fuera de USMER'
	},
	'SECTOR': {
		1 : 'CRUZ ROJA',
		2 : 'DIF',
		3 : 'ESTATAL',
		4 : 'IMSS',
		5 : 'IMSS-BIENESTAR',
		6 : 'ISSSTE',
		7 : 'MUNICIPAL',
		8 : 'PEMEX',
		9 : 'PRIVADA',
		10 : 'SEDENA',
		11 : 'SEMAR',
		12 : 'SSA',
		13 : 'UNIVERSITARIO',
		99 : 'NO ESPECIFICADO'
	},
	'SEXO':{
		1 : 'MUJER',
		2 : 'HOMBRE',
		99 : 'NO ESPECIFICADO'
	},
	'TIPO_PACIENTE':{
		1 : 'AMBULATORIO',
		2 : 'HOSPITALIZADO',
		99 : 'NO ESPECIFICADO'
	},
	'SI_NO': {
		1 : 'SI ',
		2 : 'NO ',
		97 : 'NO APLICA',
		98 : 'SE IGNORA',
		99 : 'NO ESPECIFICADO'
	},
	'NACIONALIDAD': {
		1 : 'MEXICANA',
		2 : 'EXTRANJERA',
		99 : 'NO ESPECIFICADO'
	},
	'RESULTADO_LAB': {
		1 : 'POSITIVO A SARS-COV-2',
		2 : 'NO POSITIVO A SARS-COV-2',
		3 : 'RESULTADO PENDIENTE',
		4 : 'RESULTADO NO ADECUADO ',
		97 : 'NO APLICA (CASO SIN MUESTRA)'
	},
	'RESULTADO_ANTIGENO': {
		1 : 'POSITIVO A SARS-COV-2',
		2 : 'NEGATIVO A SARS-COV-2',
		97 : 'NO APLICA (CASO SIN MUESTRA)'
	},
	'CLASIFICACION_FINAL': {
		1 : 'CASO DE COVID-19 CONFIRMADO POR ASOCIACIÓN CLÍNICA EPIDEMIOLÓGICA',
		2 : 'CASO DE COVID-19 CONFIRMADO POR COMITÉ DE  DICTAMINACIÓN',
		3 : 'CASO DE SARS-COV-2  CONFIRMADO',
		4 : 'INVÁLIDO POR LABORATORIO',
		5 : 'NO REALIZADO POR LABORATORIO',
		6 : 'CASO SOSPECHOSO',
		7 : 'NEGATIVO A SARS-COV-2'
	},
	'ENTIDADES': {
		1 : 'AGUASCALIENTES',
		2 : 'BAJA CALIFORNIA',
		3 : 'BAJA CALIFORNIA SUR',
		4 : 'CAMPECHE',
		5 : 'COAHUILA DE ZARAGOZA',
		6 : 'COLIMA',
		7 : 'CHIAPAS',
		8 : 'CHIHUAHUA',
		9 : 'CIUDAD DE MÉXICO',
		10 : 'DURANGO',
		11 : 'GUANAJUATO',
		12 : 'GUERRERO',
		13 : 'HIDALGO',
		14 : 'JALISCO',
		15 : 'MÉXICO',
		16 : 'MICHOACÁN DE OCAMPO',
		17 : 'MORELOS',
		18 : 'NAYARIT',
		19 : 'NUEVO LEÓN',
		20 : 'OAXACA',
		21 : 'PUEBLA',
		22 : 'QUERÉTARO',
		23 : 'QUINTANA ROO',
		24 : 'SAN LUIS POTOSÍ',
		25 : 'SINALOA',
		26 : 'SONORA',
		27 : 'TABASCO',
		28 : 'TAMAULIPAS',
		29 : 'TLAXCALA',
		30 : 'VERACRUZ DE IGNACIO DE LA LLAVE',
		31 : 'YUCATÁN',
		32 : 'ZACATECAS',
		33 : 'ESTADOS UNIDOS MEXICANOS',
		34 : 'NO APLICA',
		35 : 'SE IGNORA',
		36 : 'NO ESPECIFICADO'
	}
}