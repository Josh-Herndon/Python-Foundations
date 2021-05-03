graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def bfs(graph, start):
    visited = set()
    queue = [start]

    while queue:
        vertex = queue.pop(0)

        if vertex not in visited:
            visited.add(vertex)

            queue.extend(graph[vertex] - visited)

    return visited

print(bfs(graph, 'A'))

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]

    while queue:
        vertex, path = queue.pop(0)

        for nxt in graph[vertex] - set(path):
            if nxt == goal:
                yield path + [nxt]
            else:
                queue.append((nxt, path + [nxt]))

print(list(bfs_paths(graph, 'A', 'F')))

def shortest_path_bfs(graph, start, goal):

    try:
        return next(bfs_paths(graph, start, goal))

    except StopIteration:
        return None

print(shortest_path_bfs(graph, 'C', 'F'))
