# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 16:57:32 2017

@author: heber
"""

import networkx as nx
import FuncionesGrafos as fg
import numpy as np
import pandas as pd

nodos, aristas = [], []

G = nx.Graph()

# =============================================================================
# Leer el grafo desde archivo txt
# =============================================================================

with open('CA-HepTh.txt', 'r') as f:
#	contador = 0
#	f.readline()
	line = f.readline()
#	while line != "" and contador <= 100:
	while line != "":
#		print(line)
		if line[0] != '#':
			campos = line.split('\t')
#			print(campos[0], campos[1])
			aristas.append((int(campos[0]), int(campos[1])))
#			contador = contador + 1
		line = f.readline()

G.add_edges_from(aristas)

fg.mostrar_datos(G)

# =============================================================================
# Secuencia de grados del grafo
# =============================================================================

#sg = fg.secuencia_grados(G.nodes, G.edges)
sg = []

for d in G.degree:
	sg.append(d[1])

sg.sort()

# =============================================================================
# Datos estadísticos de la secuencia de grados
# =============================================================================

media = np.mean(sg)
mediana = np.median(sg)
varianza = np.var(sg)

# =============================================================================
# Tabla de frecuencias
# =============================================================================

i, fi = [], []
for g  in sg:
	if g in i:
		fi[i.index(g)] += 1
	else:
		i.append(g)
		fi.append(1)

Fi = []
Fi.append(fi[0])
for u in np.arange(1, len(fi)):
	Fi.append(fi[u] + Fi[u - 1])
hi = []
for u in fi:
	hi.append(u / Fi[-1])
Hi = []
Hi.append(hi[0])
for u in np.arange(1, len(hi)):
	Hi.append(hi[u] + Hi[u - 1])

# =============================================================================
# Dataframe de la tabla de frecuencias
# =============================================================================

d = {
	'fi' : pd.Series(fi, index=i),
	'Fi' : pd.Series(Fi, index=i),
	'hi' : pd.Series(hi, index=i),
	'Hi' : pd.Series(Hi, index=i)
}
tabla = pd.DataFrame(d, columns=['fi', 'hi', 'Fi', 'Hi'])
tabla.index.name = 'i'

tabla.hist(column='fi', bins=100)

# =============================================================================
# Generar grafo aleatorio
# =============================================================================

N, E = fg.uda_model(sg, ["G_equis", "G_0"])

fg.imprimir_gephi(N, E)

