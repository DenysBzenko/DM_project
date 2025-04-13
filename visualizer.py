import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(graph):
    G = nx.Graph()

    for i in range(graph.V):
        for j in range(i + 1, graph.V):
            if graph.adj_matrix[i][j] != 0:
                G.add_edge(i, j)

    pos = nx.spring_layout(G)
    plt.figure(figsize=(3, 3))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', 
            node_size=500)
    plt.title("Undirected Graph Visualization")
    plt.show()
