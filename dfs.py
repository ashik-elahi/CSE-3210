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
stack = []


def bfs(sn):
    visited.append(sn)
    stack.append(sn)
    while stack:
        m = stack.pop()
        print(m, end=" ")
        for neighbour in graph.get(m, []):
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)

bfs('S')
print()