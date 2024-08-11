def dfs(graph, node, visited, parent):
    visited[node] = True
    
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if dfs(graph, neighbor, visited, node):
                return True
        elif parent != neighbor:
            return True
    
    return False

def has_cycle(graph, edge):
    u, v = edge
    visited = {vertex: False for vertex in graph}
    
    graph[u].append(v)
    graph[v].append(u)
    
    if dfs(graph, u, visited, None):
        graph[u].remove(v)
        graph[v].remove(u)
        return True
    
    return False

def kruskal(vertices, edges):
    mst = []
    graph = {v: [] for v in vertices}
    total_cost = 0  # Variable to accumulate total cost
    
    # Sort edges by weight
    edges = sorted(edges, key=lambda edge: edge[2])
    
    for edge in edges:
        if not has_cycle(graph, edge[:2]):
            mst.append(edge)
            total_cost += edge[2]  # Add the edge's weight to the total cost
    
    return mst, total_cost

# Function to create the graph from user input
def create_graph():
    vertices = input("Enter the vertices separated by space: ").split()
    edges = []
    
    num_edges = int(input("Enter the number of edges: "))
    
    for _ in range(num_edges):
        u, v, weight = input("Enter the edge (e.g., A B 2) with vertices and weight: ").split()
        weight = int(weight)
        edges.append((u, v, weight))
    
    return vertices, edges

# Main function to run the program
if __name__ == "__main__":
    vertices, edges = create_graph()
    mst, total_cost = kruskal(vertices, edges)
    
    print("Minimum Spanning Tree (MST) edges and weights:")
    for u, v, weight in mst:
        print(f"{u} - {v} : {weight}")
    
    print(f"Total minimum cost: {total_cost}")