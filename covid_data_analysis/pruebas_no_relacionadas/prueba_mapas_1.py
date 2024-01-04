import folium

# Definir las coordenadas de ubicación
latitud = 40.7128  # Reemplaza con la latitud de tu ubicación
longitud = -74.0060  # Reemplaza con la longitud de tu ubicación

# Crear un mapa centrado en la ubicación especificada
mapa = folium.Map(location=[latitud, longitud], zoom_start=12)

# Añadir un marcador al mapa
folium.Marker([latitud, longitud], popup='Datos aquí').add_to(mapa)

# Guardar el mapa como un archivo HTML
mapa.save('mapa.html')

