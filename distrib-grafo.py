# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 19:13:50 2017

@author: heber_000
"""

import FuncionesGrafos as fg
import pandas as pd
import matplotlib.pyplot as plt
import random as r
import numpy as np

#definir variables
N_NODOS = 1500

#leer la secuencia de grados del grafo
#1. leer los nodos
#2. leer los enlaces
#3. calcular los grados


#cargar los datos con pandas
grados = pd.read_csv('./TablaDistFrec.csv', sep=';')

# Crear N clases clases

#crear la función de distribución de frecuencias de grados original

# =============================================================================
# #graficar r [0, 1] vs X
# #https://pandas.pydata.org/pandas-docs/stable/visualization.html
# grados['Hi'].plot()
# =============================================================================
#generador de grados aleatorios según la función de la tabla de frecuencias
def buscarClase(valor):
#    print(valor)
#    grado = -1
	for pos in range(len(grados)-1, 0, -1):
#        print('posicion:', pos)
		if valor > grados['Hi'][pos]:
			return grados['i'][pos+1]

# =============================================================================
#Generación aleatoria de N_NODOS grados
nGrados = []
for m in range(N_NODOS):
	nGrados.append(buscarClase(r.random()))
# =============================================================================


# =============================================================================
nGrados = pd.DataFrame(nGrados)
nGrados.boxplot()
histograma = plt.hist(nGrados[0], N_NODOS, histtype='stepfilled')
# =============================================================================

#crear un grafo
N, E = fg.uda_model(nGrados[0], ["G_diagonal", "G_0"])
G = fg.n_networkx(N,E)
fg.mostrar_datos(G)

# =============================================================================
# Crear 500 grafos
# =============================================================================
import math as m

#grafo original
Sg = fg.extrae_secuencia_grados(
	'./input/facebook_nodos.csv', 
	'./input/facebook_aristas.csv'
)

#escalar los grados
densidad = 0.01082
cE = m.ceil(densidad * 1000 * 999 / 2)
#e_grados = np.ceil(grados['hi'] * cE)
eSg = []
for g in Sg:
	eSg.append(m.ceil(g * densidad))

#comprobar cantidad enlaces
sum = 0
for i in eSg:
	sum = sum + i

#---------------------------------
#Crear las columnas 'i', y 'fi' de la tabla de distribución de frecuencias
i, fi = [], []
for g  in Sg:
	if g in i:
		fi[i.index(g)] += 1
	else:
		i.append(g)
		fi.append(1)
#cálculo de columnas
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

#Armar la tabla de distribución de frecuencias
d = {
	'fi' : pd.Series(fi, index=i),
	'Fi' : pd.Series(Fi, index=i),
	'hi' : pd.Series(hi, index=i),
	'Hi' : pd.Series(Hi, index=i)
}
tabla = pd.DataFrame(d, columns=['fi', 'hi', 'Fi', 'Hi'])
tabla.index.name = 'i'
#---------------------------------

#Crear las 500 secuencias de grados
secuencias = []

#Generar los grafos según las secuencias de grados
grafos_creados = []
for n in range(500):
	N, E = fg.uda_model(eSg, ["G_diagonal", "G_0"])
	G = fg.n_networkx(N,E)
	grafos_creados.append(G)

