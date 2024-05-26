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

visited= [False]*(len(graph_queston)+1)
def dfs(graph, s):
    print(f"Visited {s}")
    visited[s] = True
    
    for neighbour in graph[s]:
        if not visited[neighbour]:
            print(f"Visited {neighbour}")
            visited[neighbour] = True
            dfs(graph, neighbour)
dfs(graph_queston,1)