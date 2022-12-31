graph = {
    'S': {'C': 4, 'B': 2, 'A': 5},
    'A': {'D': 9, 'E': 4},
    'B': {'G': 6},
    'C': {'F': 2},
    'D': {'H': 7},
    'E': {'G': 6},
    'F': {'G': 1}
}


def bfs(graph, start, end):
    stack = []
    stack.append([start])
    while stack:
        path = stack.pop()
        node = path[-1]
        if node == end:
            return path
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            stack.append(new_path)


path = bfs(graph, 'S', 'G')
cost = 0
for i in range(len(path)-1):
    cost += graph[path[i]][path[i+1]]

print("Path: ", path)
print("Cost: ", cost)
