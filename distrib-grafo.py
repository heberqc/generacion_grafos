# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 19:13:50 2017

@author: heber_000
"""

import FuncionesGrafos as fg
import pandas as pd
import matplotlib.pyplot as plt
import random as r

#definir variables
n_nodos = 1500

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

def buscarClase(valor):
#    print(valor)
#    grado = -1
    for pos in range(len(grados)-1, 0, -1):
#        print('posicion:', pos)
        if valor > grados['Hi'][pos]:
            return grados['i'][pos+1]

# =============================================================================
nGrados = []
for m in range(n_nodos):
    nGrados.append(buscarClase(r.random()))
# =============================================================================


# =============================================================================
nGrados = pd.DataFrame(nGrados)
nGrados.boxplot()
histograma = plt.hist(nGrados[0], n_nodos, histtype='stepfilled')
# =============================================================================

#crear un grafo
N, E = fg.uda_model(nGrados[0], ["G_diagonal", "G_0"])
G = fg.n_networkx(N,E)
fg.mostrar_datos(G)
