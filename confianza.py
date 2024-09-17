import laspy
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Cargar el archivo LAS
las_file_path = r"D:\TESIS\DATA DE CAMPO\2.1. PROCESAMIENTO\0. 19-12-2020\nube19-12-20.las"
las = laspy.read(las_file_path)

# Extraer las coordenadas y el campo "confidence"
x = las.x
y = las.y
z = las.z
confidence = las['confidence']

# Verificar si el archivo LAS tiene datos RGB
if 'red' in las.point_format.dimension_names and 'green' in las.point_format.dimension_names and 'blue' in las.point_format.dimension_names:
    r = las.red / 65535.0  # Normalizar los valores RGB
    g = las.green / 65535.0
    b = las.blue / 65535.0
    rgb_present = True
else:
    print("El archivo LAS no contiene información RGB.")
    rgb_present = False

# Analizar estadísticamente el campo "confidence"
mean_confidence = np.mean(confidence)
std_dev_confidence = np.std(confidence)

print(f"Media del nivel de confianza: {mean_confidence}")
print(f"Desviación estándar del nivel de confianza: {std_dev_confidence}")

# Crear la figura y los subplots
fig = plt.figure(figsize=(18, 8))

# Primer subplot: Distribución 3D de los puntos en función del nivel de confianza
ax1 = fig.add_subplot(121, projection='3d')
scatter_conf = ax1.scatter(x, y, z, c=confidence, cmap='plasma', s=1)
colorbar_conf = plt.colorbar(scatter_conf, ax=ax1, pad=0.1)
colorbar_conf.set_label('Nivel de Confianza')
ax1.set_title('Distribución 3D de los Puntos con Niveles de Confianza')
ax1.set_xlabel('Coordenada X')
ax1.set_ylabel('Coordenada Y')
ax1.set_zlabel('Coordenada Z')

# Segundo subplot: Visualización RGB de la nube de puntos
if rgb_present:
    ax2 = fig.add_subplot(122, projection='3d')
    scatter_rgb = ax2.scatter(x, y, z, c=np.stack((r, g, b), axis=-1), s=1)
    ax2.set_title('Visualización RGB de la Nube de Puntos')
    ax2.set_xlabel('Coordenada X')
    ax2.set_ylabel('Coordenada Y')
    ax2.set_zlabel('Coordenada Z')
else:
    print("No se pudo generar la visualización RGB porque el archivo LAS no contiene información de color.")

plt.show()

