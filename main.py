import numpy as np
import pandas as pd
import os
import time
from db_data import *


def data_generator(data, diretory_name):
	start = time.time()
	if not os.path.exists(diretory_name):
		os.makedirs(diretory_name)
		print(f"Carpeta '{diretory_name}' creada exitosamente en '{diretory_name}'.")
	else:
		print(f"La carpeta '{diretory_name}' ya existe en '{diretory_name}'.")
		print("Para evitar sobre escrituras, inicia de nuevo")
		return
	
	for head in headers:
		try:
			array_aux = extract_column_data(data, head)
			db_head = diretory_name + '\\' + head
			save_column_data(array_aux, db_head)
		except KeyError as e:
			print(f"Error: La columna '{head}' no se encuentra en el DataFrame.")
	end = time.time()
	print(f"Tiempo de ejecución: {end - start}")
	return


def extract_column_data(csv_data, column_name):
	csv_column = csv_data[column_name]
	array_column = csv_column.to_numpy()
	return array_column


def save_column_data(array_column, column_name):
	array_name = column_name + '.npy'
	np.save(array_name, array_column)
	return


data_generator(data, 'prueba_5')
