import networkx as nx
import numpy as np
import scipy as sp


def distribution_of_degree(G):   #
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

def NDNW_average_degree(G):
    number_of_edges = G.number_of_edges()
    number_of_nodes = G.number_of_nodes()
    average_degree = (2*number_of_edges)/number_of_nodes
    return average_degree
def DNW_average_degree(G):
    number_of_edges = G.number_of_edges()
    number_of_nodes = G.number_of_nodes()
    average_degree = (number_of_edges)/number_of_nodes
    return average_degree

def catagory_of_network(G):
    av = NDNW_average_degree(G)
    number_of_nodes = G.number_of_nodes()
    if av<1:
        print("该网络为亚临界状态网络")
    elif av==1:
        print("该网络为临界状态网络")
    elif av>1 and av<np.log(number_of_nodes):
        print("该网络为超临界状态网络")
    elif av>=np.log(number_of_nodes):
        print("该网络为连通状态网络")
    else:
        print("ERROR,PLEASE CHECK YOUR GRAPH!")

def NDNW_network_diameter(G):
    dmax = np.log(G.number_of_nodes())/np.log(NDNW_average_degree(G))
    return dmax

def DNW_network_diameter(G):
    dmax = np.log(G.number_of_nodes())/np.log(DNW_average_degree(G))
    return dmax

def natural_cutoff(G,func,kmin):
    number_of_nodes = G.number_of_nodes()
    result = sp.integrate.quad(func,kmin,np.pi)
    return result
