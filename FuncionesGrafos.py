import networkx as nx
import matplotlib.pyplot as plt
import math as m
import random as r
import subprocess
from datetime import datetime

def havel_hakimi(secuencia):
	# sacar copia de la secuencia de grados
	DS = secuencia[:]
	# comprobar si la secuencia solo contiene ceros
	if DS.count(0) == len(DS):
		return True
	# ordenar de forma descendente
	DS.sort(reverse=True)
	# comprobar que no hayan negativos
	if DS[len(DS)-1] < 0: return False
	# comprobar que la suma de grados es par
	if sum(DS) %2 != 0: return False
	# comprobar que el primer grado se pueda reducir
	if DS[0] >= len(DS): return False
	# reducir el primer grado y continuar con el algoritmo
	count = DS.pop(0)
	for i in range(count):
		DS[i] = DS[i] - 1
	return havel_hakimi(DS)

def mostrar_networkx(N, E):
	G = nx.Graph()
	G.add_nodes_from(N)
	G.add_edges_from(E)
	nx.draw_networkx(G)
	# nx.draw_circular(G)
	plt.show()
	# print("Clustering:", nx.clustering(G))
	print("Coef. agrupamiento promedio:", round(nx.average_clustering(G), 4))
	# print("Triangles:", nx.triangles(G))
	nTriangles = 0
	for valor in nx.triangles(G).values():
		nTriangles = nTriangles + valor
	nTriangles = int(nTriangles / 3)
	print("Cantidad de triangulos:", nTriangles)

def configuration_model(Sg):
	N, E, Stubs = [], [], []
	for i in range(len(Sg)):
		N.append(i + 1)
		for j in range(Sg[i]):
			Stubs.append(N[i])
	while len(Stubs) > 0:
		a = Stubs.pop(int(m.floor(r.random() * len(Stubs))))
		while True:
			aux = int(m.floor(r.random() * len(Stubs)))
			if a != Stubs[aux]:
				break
		b = Stubs.pop(aux)
		E.append((a, b))
	return N, E

def edgetriangle_model(Ss, St):
	N, E, s_stubs, t_stubs = [], [], [], []
	for i in range(len(Ss)):
		N.append(i + 1)
		for j in range(Ss[i]):
			s_stubs.append(N[i])
		for j in range(St[i]):
			t_stubs.append(N[i])
	while len(s_stubs) > 0:
		a = s_stubs.pop(int(m.floor(r.random() * len(s_stubs))))
		b = s_stubs.pop(int(m.floor(r.random() * len(s_stubs))))
		E.append((a, b))
	while len(t_stubs) > 0:
		a = t_stubs.pop(int(m.floor(r.random() * len(t_stubs))))
		b = t_stubs.pop(int(m.floor(r.random() * len(t_stubs))))
		c = t_stubs.pop(int(m.floor(r.random() * len(t_stubs))))
		E.append((a, b))
		E.append((a, c))
		E.append((b, c))
	return N, E

def uda_model(Sg, subgrafos):
	# catalogo de subgrafos
	cat_subgrafos = {
		"G_0": [1],
		"G_triangulo": [2],
		"G_cuadrado": [2],
		"G_diagonal": [2, 3],
		"G_equis": [3],
		"G_pentagono": [1],
		"G_hexagono": [1]
	}
	N, E = [], []
	# conjunto de grados del grafo
	l_k = set([])
	for i in Sg:
		l_k.add(i)
	# conjunto de grados de los subgrafos
	H = set([])
	for s in subgrafos:
		for i in cat_subgrafos[s]:
			H.add(i)
	string_H = ""
	for n in H:
		string_H = string_H + " " + str(n)
	# espacio de soluciones
	sol_esp = []
	# soluciones
	for k in l_k:
		subprocess.call("./solver.exe " + str(k) + string_H)
		sol_k = []
		c_max = len(H) - 1
		with open('soluciones.txt', 'r') as f:
			f.readline()
			cont = 0
			solution = []
			line = f.readline()
			while line != "":
				solution.append(int(line))
				if cont == c_max:
					sol_k.append(solution[:])
					cont = 0
					solution = []
				else:
					cont = cont + 1
				line = f.readline()
		sol_esp.append([k, sol_k])
	print(sol_esp)
	# linea 21
	return N, E

def mostrar_datos(G):
	print("Cantidad de nodos:", nx.number_of_nodes(G))
	print("Cantidad de enlaces:", nx.number_of_edges(G))
	print("Coef. Transitividad:", round(nx.transitivity(G), 4))
	print("Coef. agrupamiento promedio:", round(nx.average_clustering(G), 4))
	nTriangles = 0
	for valor in nx.triangles(G).values():
		nTriangles = nTriangles + valor
	nTriangles = int(nTriangles / 3)
	print("Cantidad de triangulos:", nTriangles)

def imprimir_gephi(G):
	fecha = datetime.now().strftime('%Y%m%d-%H%M%S')
	nodos = open(fecha + '_n.csv', 'w')
	nodos.write("ID,Label")
	for i in G.nodes():
		nodos.write("\n" + str(i) + "," + str(i))
	nodos.close()
	enlaces = open(fecha + '_e.csv', 'w')
	enlaces.write("Source,Target,Weight,Label,Type")
	for j in G.edges():
		enlaces.write("\n" + str(j[0]) + "," + str(j[1]) + ",1,,Undirected")
	enlaces.close()
