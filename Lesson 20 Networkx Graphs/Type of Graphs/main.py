if __name__ == "__main__":
    import networkx as nx
    import matplotlib.pyplot as plt
    import matplotlib as mlib
    mlib.use('TkAgg')

    # graph examples
    G = nx.Graph()
    G.add_nodes_from([
    (1, {"color": "red"}),
    (2, {"color": "green"}),
    (3, {"color": "blue"}),
    ])

    G.add_edges_from([(1, 2), (1, 3)])
    nx.draw(G,with_labels=True)
    plt.show()

    # digraph exmple
    G = nx.DiGraph()
    G.add_nodes_from([
    (1, {"color": "red"}),
    (2, {"color": "green"}),
    (3, {"color": "blue"}),
    ])

    G.add_edges_from([(1, 2), (1, 3)])
    nx.draw(G,with_labels=True)
    plt.show()

    MG = nx.MultiGraph()
    MG.add_weighted_edges_from([(1, 2, 0.5), (1, 2, 0.75), (2, 3, 0.5)])
    nx.draw(MG,with_labels=True)
    plt.show()

    MDG = nx.MultiDiGraph()
    MDG.add_weighted_edges_from([(1, 2, 0.5), (1, 2, 0.75), (2, 3, 0.5)])
    nx.draw(MDG,with_labels=True)
    plt.show()



