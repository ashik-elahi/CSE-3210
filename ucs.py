graph = {
    'S': {'A': 5, 'B': 2, 'C': 4},
    'A': {'D': 9, 'E': 4},
    'B': {'G': 6},
    'C': {'F': 2},
    'D': {'H': 7},
    'E': {'G': 6},
    'F': {'G': 1},
    'G': {},
    'H': {}
}


def dijkstra(src):
    queue = [src]
    minDistances = {v: float("inf") for v in graph}
    minDistances[src] = 0
    predecessor = {}

    while queue:
        currentNode = queue.pop(0)
        for neighbor in graph[currentNode]:
            newDist = minDistances[currentNode] + graph[currentNode][neighbor]

            if newDist < minDistances[neighbor]:
                minDistances[neighbor] = min(newDist, minDistances[neighbor])
                queue.append(neighbor)
                predecessor[neighbor] = currentNode

    return minDistances, predecessor


def ucs(graph, src, dest):
    minDistances, predecessor = dijkstra(src)

    path = []
    currentNode = dest
    while currentNode != src:
        if currentNode not in predecessor:
            print("Path not reachable")
            break
        else:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
    path.insert(0, src)

    # if dest in minDistances and minDistances[dest] != float("inf"):
    print('Path: ' + str(path))
    print('Cost: ' + str(minDistances[dest]))


ucs(graph, 'S', 'G')
