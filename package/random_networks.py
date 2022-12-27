import networkx as nx
import random


def empty_network(nodes_number):
    G = nx.Graph()
    Node = nx.path_graph(nodes_number)
    G.add_nodes_from(Node)
    return G


def rand_edge(G, vi, vj, p=0.8):  # 默认概率p=0.1
    probability = random.random()  # 生成随机小数
    if probability > p:  # 如果大于p
        print(probability)
        G.add_edge(vi, vj)
    return G

def create_random_networks(G,nodes_number,p=0.8):
    i = 0
    while i<nodes_number:
        j = 0
        while j<nodes_number:
            if j<i:
                j+=1
            else:
                rand_edge(G=G,vi=i,vj=j,p=p)
                j+=1
        i+=1
    return G