# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 08:21:04 2017

@author: heber
"""

import Funcionsgrafos as fg
import pandas as pd
import networkx as nx
import numpy as np

# =============================================================================
# Propiedades del grafo
# =============================================================================

nodos = pd.read_csv('./input/facebook_nodos.csv')
enlaces = pd.read_csv('./input/facebook_aristas.csv')

N = []
E = []

for nodo in nodos['Id']:
	N.append(nodo)

for enlace in range(len(enlaces)):
	E.append((enlaces['Source'][enlace], enlaces['Target'][enlace]))

G = nx.Graph()
G.add_nodes_from(N)
G.add_edges_from(E)

fg.mostrar_datos(G)
#Diámetro (longest shortest path) = 8

# =============================================================================
# Secuencia de grados
# =============================================================================

sg = []

for grado in G.degree:
	sg.append(grado[1])

sg.sort()

#Crear las columnas 'i', y 'fi' de la tabla de distribución de frecuencias
i, fi = [], []
for g  in sg:
	if g in i:
		fi[i.index(g)] += 1
	else:
		i.append(g)
		fi.append(1)
#cálculo de columnas
Fi = []
Fi.append(fi[0])
for u in range(1, len(fi)):
	Fi.append(fi[u] + Fi[u - 1])
hi = []
for u in fi:
	hi.append(u / Fi[-1])
Hi = []
Hi.append(hi[0])
for u in range(1, len(hi)):
	Hi.append(hi[u] + Hi[u - 1])

#Armar la tabla de distribución de frecuencias
d = {
	 'i' : pd.Series(i),
	'fi' : pd.Series(fi),
	'Fi' : pd.Series(Fi),
	'hi' : pd.Series(hi),
	'Hi' : pd.Series(Hi)
}
tabla = pd.DataFrame(d, columns=['i', 'fi', 'hi', 'Fi', 'Hi'])

# =============================================================================
# Generar secuencia de grados nuevas
# =============================================================================

#Cantidad de nodos de grafos nuevos
cn = 1000
#Densidad 0.010819963503439287
#Cantidad de enlaces para conservar la densidad de los grafos
ce = int(0.010819963503439287 * cn * (cn - 1) / 2) + 1

#cantidad de iteraciones promedio para obtener la cantidad de enlaces
iter_prom = int(ce / np.mean(sg)) + 1

#función para ubicar la cantidad de grados según la probabilidad
def buscarClase(valor):
	for pos in range(len(tabla)):
		if valor < tabla['Hi'][pos]:
			return tabla['i'][pos]

#nuevas secuencia de grados
nsg = []

#Generar 500 secuencias de grados
for sec in range(500):
	sgg = [] #secuencia de grados generada
	for n in range(iter_prom):
		grado = buscarClase(np.random.random())
		if (grado > tabla['i'][len(tabla)-1]):
			sgg.append(cn)
		else:
			sgg.append(grado)
	nsg.append(sgg)

# =============================================================================
# Generación aleatoria de grafos
# =============================================================================

#arreglo de nuevos grafos generados
ngg = []


