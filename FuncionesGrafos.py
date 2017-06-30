import networkx as nx
import matplotlib.pyplot as plt
import math as m
import random as r

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

def mostrar_datos(G):
	print("Cantidad de nodos:", nx.number_of_nodes(G))
	print("Cantidad de enlaces:", nx.number_of_edges(G))
	print("Coef. agrupamiento global - Transitividad:", nx.transitivity(G))
	print("Coef. agrupamiento promedio:", round(nx.average_clustering(G), 4))
	nTriangles = 0
	for valor in nx.triangles(G).values():
		nTriangles = nTriangles + valor
	nTriangles = int(nTriangles / 3)
	print("Cantidad de triangulos:", nTriangles)