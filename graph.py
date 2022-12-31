graph = {
    'S': {'A': 5, 'B': 2, 'C': 4},
    'A': {'D': 9, 'E': 4},
    'B': {'G': 6},
    'C': {'F': 2},
    'D': {'H': 7},
    'E': {'G': 6},
    'F': {'G': 1}
}

li = ['S', 'B', 'G']
for i in range(2):
    print(graph[li[i]][li[i+1]])
