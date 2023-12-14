import heapq

def dijkstra(graph, start_node):
    queue = []
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
