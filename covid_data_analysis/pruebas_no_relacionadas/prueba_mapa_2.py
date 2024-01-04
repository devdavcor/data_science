from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# Definir las coordenadas de México
min_lat, max_lat = 14.53, 32.71
min_lon, max_lon = -117.13, -86.74

# Crear un mapa centrado en México
mapa = Basemap(projection='mill', llcrnrlat=min_lat, llcrnrlon=min_lon, urcrnrlat=max_lat, urcrnrlon=max_lon, resolution='c')

# Descargar datos de límites necesarios
mapa.drawcoastlines()
mapa.drawcountries()

# Agregar una capa de relleno para México con un color diferente
mapa.drawmapboundary(fill_color='lightblue')  # Puedes cambiar el color según tus preferencias
mapa.fillcontinents(color='white', lake_color='lightblue', zorder=0)

# Datos de ejemplo: latitudes y longitudes de algunos estados
latitudes_estados = [19.4326, 21.1619, 23.6345, 25.4336]
longitudes_estados = [-99.1332, -86.8515, -102.5528, -100.9665]

# Colores diferentes para cada estado
colores_estados = ['red', 'blue', 'green', 'purple']

# Añadir puntos al mapa para representar los estados
for lat, lon, color in zip(latitudes_estados, longitudes_estados, colores_estados):
    x, y = mapa(lon, lat)
    mapa.scatter(x, y, marker='o', color=color, label='Estado')

# Mostrar leyenda y título
plt.legend()
plt.title('Visualización de estados en México con el país coloreado')

# Mostrar el mapa
plt.show()
