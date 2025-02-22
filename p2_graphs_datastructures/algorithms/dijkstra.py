from p2_graphs_datastructures.data_structures import heap


def dijkstra(filename, source_node):
    "Implementation of Dijksta's Shortest Path algorithm using a minheap"
    # graph rep: {source: [(dest, weight)]})
    graph = load_graph_adjacency_list(filename)

    distances = {}  # enter shortest path distances as nodes are processed
    minheap = []  # initialize empty minheap
    heap.minheap_push(minheap, (0, source_node))

    while minheap:
        distance, node = heap.extract_min(minheap)

        if node in distances:
            continue  # Already processed this node, move on

        distances[node] = distance  # Process new node

        for edge in graph[node]:  # Update all adjacent nodes
            adjacent_node = edge[0]
            potential_path_dist = edge[1] + distance
            # add to heap (nodes can be added multiple times, will only be processed once)
            heap.minheap_push(minheap, (potential_path_dist, adjacent_node))

    return distances


def load_graph_adjacency_list(filename):
    "Parses, and returns, a graph adjacency list represented as a dictionary, {source: [(dest, weight)]}"

    graph = {}

    with open(filename, 'r') as f:

        for line in f:

            data = line.replace('\n', '').replace('\t', ' ').rstrip()
            data = data.split(' ')

            source = data[0]
            edges = []
            graph[source] = [(edge.split(',')[0], int(edge.split(',')[1]))
                             for edge in data[1:]]  # convert edge weight to int

    return graph


if __name__ == '__main__':
    pass
