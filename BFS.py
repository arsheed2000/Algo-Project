def breadth_first_search(graph, start_node):
    visited = []
    queue = []
    visited.append(start_node)
    queue.append(start_node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbor in graph[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
