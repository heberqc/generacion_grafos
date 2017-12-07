# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 17:36:55 2017

@author: heber

https://networkx.github.io/documentation/stable/reference/algorithms/centrality.html

"""

import networkx as nx
import FuncionesGrafos as fg
from networkx.algorithms import approximation

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

#(Shortest Path) Betweenness
nx.betweenness_centrality(G)
nx.edge_betweenness_centrality(G)
nx.betweenness_centrality_subset(G)
nx.edge_betweenness_centrality_subset(G)

#Current Flow Betweenness
nx.current_flow_betweenness_centrality(G)
nx.edge_current_flow_betweenness_centrality(G)
nx.approximate_current_flow_betweenness_centrality(G)
nx.current_flow_betweenness_centrality_subset(G)
nx.edge_current_flow_betweenness_centrality_subset(G)

#Communicability Betweenness
nx.communicability_betweenness_centrality(G)

#Load
nx.load_centrality(G)
nx.edge_load_centrality(G)

#Subgraph
nx.subgraph_centrality(G) #Return subgraph centrality for each node in G.
nx.subgraph_centrality_exp(G) #Return the subgraph centrality for each node of G.
nx.estrada_index(G) #Return the Estrada index of a the graph G.

#Harmonic Centrality
nx.harmonic_centrality(G) #Compute harmonic centrality for nodes.

# =============================================================================
# Approximation
# =============================================================================


