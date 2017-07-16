from FuncionesGrafos import *

N, E = uda_model([6] * 50, ["G_equis"])
imprimir_gephi(N, E)
G = n_networkx(N, E)
mostrar_datos(G)
show_networkx(G)
print(list(nx.degree(G).values()))
