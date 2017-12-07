# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 17:36:55 2017

@author: heber

https://networkx.github.io/documentation/stable/reference/algorithms/centrality.html

"""

import networkx as nx
import FuncionesGrafos as fg

Sg = [8] * 20

N, E = fg.configuration_model(Sg)

G = nx.Graph()

G.add_nodes_from(N)
G.add_edges_from(E)

# =============================================================================
# Centralidad
# =============================================================================

nx.degree_centrality(G)

#Eigenvector centrality
nx.eigenvector_centrality(G, max_iter=100, tol=1e-06, nstart=None, weight=None)

#Katz centrality
nx.katz_centrality(G, alpha=0.1, beta=1.0, max_iter=1000, tol=1e-06, 
	nstart=None, normalized=True, weight=None)

#Closeness
nx.closeness_centrality(G, u=None, distance=None, wf_improved=True, 
	reverse=False)

#Current Flow Closeness
nx.current_flow_closeness_centrality(G, weight=None, dtype='float', 
	solver='lu')



