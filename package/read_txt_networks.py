import pandas as pd
import networkx as nx

def read_txt_networks(file_name):
    data = open(file_name).readlines()
    set = []
    for line in data:
        a,b = line.split('\t')
        a = int(a)
        b = int(b.strip('\n'))
        #print(a,b)
        set.append((a,b))
    print(set[1])
    print("max index: "+str(max(set[len(set)-1])))
    print("Warning: This is only a reference value for the number of nodes, and if there is no largest isolated node, the value plus 1 is the total number of nodes")
    return set

def build_txt_network(set,max_node):
    G = nx.Graph()
    Node = nx.path_graph(max_node)
    G.add_nodes_from(Node)
    G.add_edges_from(set)
    return G