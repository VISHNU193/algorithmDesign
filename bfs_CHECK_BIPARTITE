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

def is_bipartite(graph:dict):
    # Number of vertices
    n = len(graph)
    
    # -1 indicates uncolored, 0 and 1 are the two colors
    color = [-1] * (n+1)
    
    # Process all components
    for start in graph.keys():
        if color[start] == -1:  # If not yet colored
            queue = deque([start])
            color[start] = 0  # Start coloring with color 0
            
            while queue:
                u = queue.popleft()
                
                for v in graph[u]:
                    if color[v] == -1:  # If the vertex v is uncolored
                        color[v] = 1 - color[u]  # Color it with the opposite color
                        queue.append(v)
                    elif color[v] == color[u]:
                        print(color)  # If the adjacent vertex has the same color
                        return False
    print(color)
    return True

print(is_bipartite(graph_queston))
print(is_bipartite(g2))



