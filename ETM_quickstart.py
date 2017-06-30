'''
Edge-Triangle Model Quickstart
'''
import networkx as nx
import matplotlib.pyplot as plt

from FuncionesGrafos import havel_hakimi
from FuncionesGrafos import edgetriangle_model
from FuncionesGrafos import mostrar_datos

# Enlaces
# E1 = [(13, 31), (1, 15), (15, 25), (20, 18), (14, 7), (13, 4), (8, 20)
# 	, (4, 31), (30, 5), (32, 9), (9, 12), (17, 28), (26, 12), (16, 7)
# 	, (22, 21), (15, 14), (14, 21), (13, 8), (30, 27), (29, 17), (18, 16)
# 	, (23, 3), (2, 31), (16, 28), (10, 19), (19, 30), (1, 8), (11, 26)
# 	, (16, 6), (14, 23), (20, 22), (19, 24), (25, 15), (18, 13), (15, 1)
# 	, (14, 11), (2, 21), (5, 24), (6, 25), (28, 19), (23, 7), (32, 4), (6, 10)
# 	, (5, 29), (23, 2), (10, 27), (23, 24), (27, 22), (7, 12), (17, 12)
# 	, (21, 22), (30, 25), (11, 10), (24, 29), (12, 21), (10, 13), (31, 18)
# 	, (5, 27), (18, 32), (2, 9), (28, 26), (6, 2), (4, 3), (6, 11), (3, 11)
# 	, (24, 8), (26, 1), (26, 3), (30, 22), (7, 4), (28, 9), (27, 19), (9, 17)
# 	, (20, 3), (32, 1), (16, 31), (29, 17), (29, 5), (25, 8), (20, 32)]
# G1 = nx.Graph()
# G1.add_edges_from(E1)
Sg1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5
	, 5, 5, 5, 5, 5, 5, 5, 5]
St1 = [0, 0, 1, 1, 2, 1, 1, 0, 2, 2, 2, 1, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 1, 1
	, 0, 1, 4, 1, 1, 3, 3, 1]
Ss1 = []
cantT = 0
for i in St1:
	cantT = cantT + i
print("cantidad de triangulos =", cantT/3)
for i in range(len(Sg1)):
	v = Sg1[i] - 2 * St1[i]
	if v > 0:
		Ss1.append(v)
	else:
		Ss1.append(0)
print("Sg:", Sg1)
print("St:", St1)
print("Ss:", Ss1)
N2, E2 = edgetriangle_model(Ss1, St1)
G2 = nx.Graph()
G2.add_edges_from(E2)
G2.add_nodes_from(N2)
nx.draw_networkx(G2)
mostrar_datos(G2)
plt.show()