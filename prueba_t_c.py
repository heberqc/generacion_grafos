# diferencia entre el coeficiente de agrupamiento y transitividad

import networkx as nx

G = nx.Graph()
G.add_nodes_from(["1", "2", "3", "4"])
G.add_edges_from([("1", "2"), ("1", "3"), ("1", "4"), ("2", "3"), ("3", "4")])
print("Transitivity:", nx.transitivity(G))
# print(nx.clustering(G))
# sum = 0
# for i in nx.clustering(G).values():
# 	sum = sum + i
# print("Average Cluestering:", sum/len(G.nodes()))
print("Average Clustering:", nx.average_clustering(G))
