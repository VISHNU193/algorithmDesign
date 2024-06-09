from collections import deque
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

def is_bipartite(graph:dict,start):

    n = len(graph)
    color = [-1] * (n+1)
    queue = deque([start])
    color[start] = 0 
    
    while queue:
        u = queue.popleft()
        
        for v in graph[u]:
            if color[v] == -1:
                color[v] = 1 - color[u] 
                queue.append(v)
            elif color[v] == color[u]:
                return False
    
    return True

print(is_bipartite(graph_queston,1))
print(is_bipartite(g2,1))



