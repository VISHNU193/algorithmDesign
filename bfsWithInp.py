def bfs(graph, start):
    visited = set() 
    queue = [start]

    while queue:
        vertex = queue.pop(0) 
        if vertex not in visited:
            print(vertex, end=" ") 
            visited.add(vertex) 

            
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Function to create the graph from user input

graph = {}
num_vertices = int(input("Enter the number of vertices: "))

for _ in range(num_vertices):
    vertex = input("Enter the vertex: ")
    neighbors = input(f"Enter the neighbors of {vertex} separated by space: ").split()
    graph[vertex] = neighbors


start_node = input("Enter the starting node for BFS: ")
print("BFS traversal starting from node", start_node, ":")
bfs(graph, start_node)
