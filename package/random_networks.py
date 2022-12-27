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