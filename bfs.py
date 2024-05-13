
graph_queston = {
    1 : [2 , 3],
    2 : [3,4,5],
    3: [2,6,7],
    4 : [2,5,8,9],
    5 : [2,4,9],
    6 : [3,7],
    7 : [3,6],
    8 : [4,9],
    9 : [4,5,8,10],
    10 : [9]
}
print(len(graph_queston))


def bfs(graph,s):
    visited = [False] * (len(graph)+1)
    queue = []
    if s in graph.keys():
        print(f"Visited {s}")
        queue.append(s)
        visited[s] = True
        while queue:
            current_node = queue.pop(0)
            for neighbour in graph[current_node]:
                if not visited[neighbour]:
                    print(f"Visited {neighbour}")
                    queue.append(neighbour)
                    visited[neighbour] = True
    else:
        print(f"Vertex {s} is not present in graph")

bfs(graph_queston,1)