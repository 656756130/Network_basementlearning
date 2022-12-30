import networkx as nx
import matplotlib.pyplot as plt

def draw_random_layout_networks(G,figsize1,figsize2,with_labels=False,font_size=1,node_size = 200,line_width=0.3,color="red"):
    pos = nx.random_layout(G)
    plt.figure(figsize=(figsize1,figsize2))
    options = {
        "with_labels": with_labels,
        "font_size": font_size,
        "font_weight": "bold",
        "font_color": "white",
        "node_size": node_size,
        "width": line_width,
        "node_color":color
    }
    nx.draw_networkx(G, pos, **options)
    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("off")
    plt.show()

def draw_DD(k,p_k,bar_width=0.5,color="red",xlabel="$k$",ylabel="$p_k$",xlim1=0,xlim2=10):
    plt.bar(k, p_k, width=bar_width, color=color)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xlim([xlim1,xlim2])