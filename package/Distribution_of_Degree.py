import networkx as nx
import numpy as np

def DD(G):
    d = nx.degree(G)
    print(d)
    d = dict(nx.degree(G))
    degree_list = np.array(d.values())
    Distribution = nx.degree_histogram(G)
    Distribution = np.array(Distribution)
    p_k = Distribution/len(G.nodes)
    #print(p_k)
    k = np.array(range(0,len(Distribution)))
    #print(k)
    return p_k,k