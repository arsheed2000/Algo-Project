import heapq

graph = {"a": {"c"},
          "b": {"c", "e"},
          "c": {"a", "b", "d", "e"},
          "d": {"c"},
          "e": {"c", "b"},
          "f": {}
        }

weighted_graph = {"a": {"c": 4, "b": 4},
                  "b": {"a": 4, "c": 2, "d": 3, "e": 7, "f": 6},
                  "c": {"a": 4, "b": 2},
                  "d": {"b": 3, "f": 2},
                  "e": {"b": 7, "f": 3},
                  "f": {"d": 2, "e": 3}
                 }

weighted_graph_negative = {"a": {"c": 10, "b": 20},
                           "b": {"d": 33, "e": 20},
                           "c": {"d": 10, "e": 50},
                           "d": { "f": 1},
                           "e": {"d": -20, "f": -2},
                           "f": {}
                        }

weighted_graph_mat = {"a": {"b": 3, "d": 5},
                  "b": {"a": 2, "d": 4},
                  "c": {"b": 1},
                  "d": {"c": 2},
                 }


class matrix:
    def __init__(self, num_of_vertices):
        self.num_of_vertices = num_of_vertices
        self.matrix = [[float('inf')] * num_of_vertices for _ in range(num_of_vertices)]

    def add_edge(self, from_vertex, to_vertices, weight):
        if from_vertex == to_vertices:
            self.matrix[from_vertex][to_vertices] = 0
        else:
            self.matrix[from_vertex][to_vertices] = weight

    def print_matrix(self):
        for row in self.matrix:
            print(row)


    def get_weight(self,from_vertex,to_vertex):
        print(self.matrix[from_vertex][to_vertex])

    def convert_from_dict(self,graph):
        vertices = set()
        for i, j in graph.items():
            vertices.add(i)
            vertices.update(j)

        vertex_to_index = {vertex: index for index, vertex in enumerate(vertices)}

        self.num_of_vertices = len(graph)
        self.matrix = [[float('inf')] * self.num_of_vertices for _ in range(self.num_of_vertices)]
        for key, subkeys in graph.items():
            key_index = vertex_to_index[key]
            for subkey, weight in subkeys.items():
                subkey_index = vertex_to_index[subkey]
                self.add_edge(key_index, subkey_index, weight)


"""
print(weighted_graph_mat.items())
test_matrix = matrix(len(weighted_graph))
test_matrix.print_matrix()
print(" ")
print(" ")

test_matrix.convert_from_dict(weighted_graph_mat)
test_matrix.print_matrix()
print(test_matrix.get_weight(1,0))
"""

visited = []
queue = []


def breadth_first_search(graph, start_node):
    visited.append(start_node)
    queue.append(start_node)

    while queue:
        m= queue.pop(0)
        print(m, end= " ")

        for neighbor in graph[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)





def dijkstra(graph, start_node):
    queue.append((0, start_node))
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_node] = 0


    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor,weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


def bellman(graph, start_node):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_node] = 0

    for i in range(len(graph)):
        for u, neighbor in graph.items():
            for v,weight in neighbor.items():
                if distances[u] + weight < distances[v]:
                    distances [v] = distances[u] + weight

    return distances


def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append({node, neighbour})

    return edges


def find_isolated_nodes(graph):
    """ returns a set of isolated nodes. """
    isolated = set()
    for node in graph:
        if not graph[node]:
            isolated.add(node)
    return isolated





