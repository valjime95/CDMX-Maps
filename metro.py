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

#arcpy.Merge_management(["rutas-lineas-de-metro/lineas-de-metro.shp", "rutas-metro/estaciones-metro.shp"], "merge.shp")



# os.chdir('/Users/valeriajimeno/Downloads/Peiser_maps')

estaciones = nx.read_shp('rutas-metro/estaciones-metro.shp').to_undirected()
lineas = nx.read_shp('rutas-lineas-de-metro/lineas-de-metro.shp')

estaciones_list = list(estaciones)

g = nx.compose(estaciones, lineas)

for i in range(200):
	n1 = estaciones_list[ran.randint(0,194)]
	n2 = estaciones_list[ran.randint(0,194)]
	if n1 != n2:
		estaciones.add_edge(n1,n2)

new_estaciones = list(nx.connected_components(estaciones))[0]
new_estaciones_list = list(new_estaciones)

l = len(new_estaciones_list)

n1 = new_estaciones_list[ran.randint(0,l-1)]
n2 = new_estaciones_list[ran.randint(0,l-1)]

path = nx.shortest_path(estaciones,n1,n2)
djs_path = nx.dijkstra_path(estaciones,n1,n2)
print("from node " + str(n1))
print("to node " + str(n2))
print("the shortest path is: " + str(path))
print("and using Dijkstra : " + str(djs_path))


nx.draw(estaciones)
plt.savefig("graf")


