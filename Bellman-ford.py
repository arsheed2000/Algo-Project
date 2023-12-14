def bellman(graph, start_node):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_node] = 0

    for i in range(len(graph)):
        for u, neighbor in graph.items():
            for v,weight in neighbor.items():
                if distances[u] + weight < distances[v]:
                    distances [v] = distances[u] + weight

    return distances