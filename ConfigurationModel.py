import math as m
import random as r

from FuncionesGrafos import *

# secuencia de grados (degree sequence)
Sd = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5
	, 5, 5, 5, 5, 5, 5, 5, 5]
# Sd = [9,9,9,8,8,8,8,8,7,7,7,7,6,6,5,5,5,4,3,3,3,3,3,2,2,2,2,2,1]
# Sd = [3,3,2,1,1,1,1]
N = []
E = []
St = []  # lista de stubs

if havel_hakimi(Sd):
	print("Secuencia de grados:", Sd)
	print("Secuencia de grados valida")
	for i in range(len(Sd)):
		N.append(i + 1)
		for j in range(Sd[i]):
			St.append(N[i])
	# print("Nodos:", N)
	print("Cantidad de nodos:", len(N))
	print("Stubs:", St)
	print("Cantidad de Stubs:", len(St))
	# emparejar parejas de stubs elegidos aleatoriamente
	while (len(St) > 0):
		a = St.pop(int(m.floor(r.random() * len(St))))
		b = St.pop(int(m.floor(r.random() * len(St))))
		E.append((a, b))
	print("Enlaces:", E)
	print("Cantidad de enlaces:", len(E))
	# mostrando con Networkx
	mostrar_networkx(N, E)
else:
	print("Secuencia de grados invalida")
