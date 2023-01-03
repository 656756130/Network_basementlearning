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

def log_graph_with_zero(x,y,x_label='num',y_label='prob',color='r'):
    plt.plot(x, y, 'o-', color=color)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid()
    plt.show()

def log_graph_without_zero(x,y,x_label='num',y_label='prob',color='r'):
    new_x = []
    new_y = []
    # 删除0值
    for i in range(len(x)):
        if y[i] != 0:
            new_x.append(x)
            new_y.append(y)
    log_graph_with_zero(new_x,new_y,x_label=x_label,y_label=y_label,color='g')
