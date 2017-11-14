#! python

import time
import networkx as nx
import matplotlib.pyplot as plt

def main():
    with open('path_sum_matrix.txt') as f:
        matrix = [[int(x) for x in line.split(',')] for line in f]
    mat_size = len(matrix)

    graph = nx.DiGraph()

    # create in and out nodes
    for i in range(0, mat_size):
        for j in range(0, mat_size):
            graph.add_edge(str((i, j)) + 'In', str((i, j)) + 'Out', weight=matrix[i][j])

    for i in range(0, mat_size):
        for j in range(0, mat_size - 1):
            graph.add_edge(str((i, j)) + 'Out', str((i, j + 1)) + 'In', weight=0) # add right edges
            graph.add_edge(str((j, i)) + 'Out', str((j + 1, i)) + 'In', weight=0) # add down edges

    for i in range(1, mat_size):
        for j in range(0, mat_size):
            graph.add_edge(str((i, j)) + 'Out', str((i - 1, j)) + 'In', weight=0) # add up edges
            graph.add_edge(str((j, i)) + 'Out', str((j, i - 1)) + 'In', weight=0)  # add left edges

    # add a source node and a sink node
    graph.add_edge('source', str((0, 0)) + 'In', weight=0)
    graph.add_edge(str((mat_size - 1, mat_size - 1)) + 'Out', 'sink', weight=0)

    # create a grid layout for viz
    pos = {'source' : (-4, mat_size - 1), 'sink':(4 * mat_size, 0)}
    for i in range(0, mat_size):
        for j in range(0, mat_size):
            pos[str((i, j)) + 'Out'] = (4 * j, mat_size - 1 - i)
            pos[str((i, j)) + 'In'] = (4 * j - 2, mat_size - 1 - i)

    #nx.draw_networkx(graph, pos=pos, with_labels=True, font_weight='bold')
    #plt.show()

    #print(nx.dijkstra_path(graph, source='source', target='sink'))
    print(nx.dijkstra_path_length(graph, source='source', target='sink'))

if __name__ == "__main__":
    start = time.time()
    main()
    print('RUNTIME: ', time.time() - start, 's')