
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

g2 ={
    1 : [2,3],
    2 : [1,4],
    3 : [1,4],
    4 : [2,3]
}

color = {
    1: "",
    2: "",
    3: "",
    4: "",
    5: "",
    6: "",
    7: "",
    8: "",
    9: "",
    10: "",
}

def color_vertex(vertex):
    if vertex%2 == 0:
        color[vertex] = "blue"
    else:
        color[vertex] = "red"

def bfs(graph,s):
    visited = [False] * (len(graph)+1)
    queue = []
    if s in graph.keys():
        print(f"Visited {s}")
        queue.append(s)
        visited[s] = True
        color_vertex(s)
        while queue:
            current_node = queue.pop(0)
            for neighbour in graph[current_node]:
                if not visited[neighbour]:
                    color_vertex(neighbour)
                    print(f"Visited {neighbour}")
                    queue.append(neighbour)
                    visited[neighbour] = True
    else:
        print(f"Vertex {s} is not present in graph")

def check_bipartite(g):
    for node in g.keys():
        print(node)
        for neighbour in g[node]:
            print(neighbour)
            if color[node] == color[neighbour]:
                return False
    return True

bfs(g2, 1)
print(color)
print(check_bipartite(g2))
