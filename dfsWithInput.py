def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    print(start, end=" ")
    visited.add(start) 
    
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


graph = {}
num_vertices = int(input("Enter the number of vertices: "))

for _ in range(num_vertices):
    vertex = input("Enter the vertex: ")
    neighbors = input(f"Enter the neighbors of {vertex} separated by space: ").split()
    graph[vertex] = neighbors


start_node = input("Enter the starting node for DFS: ")
print("DFS traversal starting from node", start_node, ":")
dfs(graph, start_node)
