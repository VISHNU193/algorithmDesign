def bellman_ford(graph, vertices, start):
    distances = {v: float('inf') for v in vertices}
    distances[start] = 0

    for _ in range(len(vertices) - 1):
        for u, v, weight in graph:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    for u, v, weight in graph:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            print("Graph contains a negative weight cycle")
            return None

    return distances

def create_graph():
    vertices = input("Enter the vertices separated by space: ").split()
    graph = []
    
    num_edges = int(input("Enter the number of edges: "))
    
    for _ in range(num_edges):
        u, v, weight = input("Enter the edge (e.g., A B -1) with vertices and weight: ").split()
        weight = int(weight)
        graph.append((u, v, weight))
    
    return graph, vertices

if __name__ == "__main__":
    graph, vertices = create_graph()
    start_node = input("Enter the starting node for Bellman-Ford algorithm: ")
    distances = bellman_ford(graph, vertices, start_node)
    
    if distances:
        print(f"Shortest distances from {start_node}:")
        for vertex, distance in distances.items():
            print(f"Distance to {vertex}: {distance}")
