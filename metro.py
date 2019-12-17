import zipfile
import numpy as np
import pandas as pd
import requests
import seaborn as sns
import io
import ogr
import gdal
import networkx as nx
import os
import matplotlib.pyplot as plt
import geopandas as gpd
import zipfile
import random as ran
import ast 
import json
import lineas
import folium


#arcpy.Merge_management(["rutas-lineas-de-metro/lineas-de-metro.shp", "rutas-metro/estaciones-metro.shp"], "merge.shp")



# os.chdir('/Users/valeriajimeno/Downloads/Peiser_maps')

# estaciones = nx.read_shp('rutas-metro/estaciones-metro.shp').to_undirected() # convertimos a grafica no dirigida
# lineas = nx.read_shp('rutas-lineas-de-metro/lineas-de-metro.shp')
# con = ast.literal_eval('lineas-de-metro.json')
# estaciones_list = list(estaciones) # como es un conjunto de nodos lo convertimos a listas

estaciones=nx.Graph()                      # Creamos una gráfica 
aristas = json.loads(lineas.jason)         
'''
for key in aristas:
	i = 0
	ar = aristas[key]['coordinates']
print(ar[1][0])
'''

#Conectamos las aristas con los nodos.

for key in aristas:
	i = 0
	ar = aristas[key]['coordinates']
	while i < len(ar)-1:
		x = (ar[i][0],ar[i][1])
		y = (ar[i+1][0],ar[i+1][1])
		estaciones.add_edge(x,y)
		i+=1

estaciones_list= list(estaciones)

print(len(estaciones_list)) #hay 164 estaciones DISTINTAS


n1 = estaciones_list[ran.randint(0,163)]   #origen    nodos aleatorios
n2 = estaciones_list[ran.randint(0,163)]   #destino

# n1 = (-99.142524, 19.3441988) #universidad
# n2 = (-99.1878051, 19.3761645) #mixcoac

path = nx.shortest_path(estaciones,n1,n2)
djs_path = nx.dijkstra_path(estaciones,n1,n2)
#print("from node " + str(n1))
#print("to node " + str(n2))
print("the shortest path is: " + str(path))
#print("and using Dijkstra : " + str(djs_path))
#print(path == djs_path)


# DIBUJAR EN EL MAPA

mapa = folium.Map(location=[19.4284700,-99.1276600])  # inicilizamos con las coordenadas de la ciudad de mexico
for i in range(len(path)):
    folium.CircleMarker([path[i][1], path[i][0]], icon=folium.Icon(color='red')).add_to(mapa)

mapa.save(('plot_data.html'))

#nx.draw(estaciones) # se dibuja la gráfica sin formato
#plt.savefig("graf")



