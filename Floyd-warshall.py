def floyd_warshall(graph):          #The Graph MUST be an adjacency matrix with weight.
    vertices = len(graph)           #The function has not been tsted with dictionaries but it has been coded with Adjacency Matrix in mind
    distance = list(map(lambda i: list(map(lambda j: j, i)), graph))
    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    return distance