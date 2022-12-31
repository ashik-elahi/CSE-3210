graph = {
    'S': ['A', 'B', 'C'],
    'A': ['D', 'E'],
    'B': ['G'],
    'C': ['F'],
    'D': ['H'],
    'E': ['G'],
    'F': ['G']
}

visited = []
queue = []


def bfs(sn):
    visited.append(sn)
    queue.append(sn)
    while queue:
        m = queue.pop(0)
        print(m, end=" ")
        for neighbour in graph.get(m, []):
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


bfs('S')
print()
