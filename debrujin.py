import networkx, matplotlib.pyplot as plot


def kmers(read, k):
    mers = []
    for mer in range(len(read) - k + 1):
        # print(read[mer:mer+k])
        mers.append(read[mer:mer + k])
    return mers


def DeBruijn(reads, k):
    nodes = []
    edges = []
    for read in reads:
        km = kmers(read, k)
        # print(km)
        for mer in range(len(km)):
            m = km[mer]
            # print(m)
            # print(m[:-1], m[1:])
            nodes.append(m[:-1])
            nodes.append(m[1:])
            edges.append([m[:-1], m[1:]])
    nodes = tuple(set(nodes))
    edges = tuple(edges)
    return nodes, edges


def visualizeDBGraph(nodes, edges):
    dbGraph = networkx.DiGraph()
    dbGraph.add_nodes_from(nodes)
    dbGraph.add_edges_from(edges)
    networkx.draw(dbGraph, with_labels=True, node_size=1000)
    plot.show()


read = ['TTACGTT', 'CCGTTA', 'GTTAC', 'GTTCGA', 'CGTTC']
# print(kmers(read[0], 5))
nodes, edges = DeBruijn(read, 5)
# print(nodes, edges)
visualizeDBGraph(nodes, edges)
