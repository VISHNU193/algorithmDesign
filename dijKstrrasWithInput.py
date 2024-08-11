import heapq

def dijkstra(graph, start):
    priority_queue = []
    
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    heapq.heappush(priority_queue, (0, start))
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances


def create_graph():
    graph = {}
    num_vertices = int(input("Enter the number of vertices: "))

    for _ in range(num_vertices):
        vertex = input("Enter the vertex: ")
        graph[vertex] = []
        num_neighbors = int(input(f"Enter the number of neighbors for {vertex}: "))
        
        for _ in range(num_neighbors):
            neighbor, weight = input(f"Enter neighbor and weight (e.g., B 2) for {vertex}: ").split()
            weight = int(weight)
            graph[vertex].append((neighbor, weight))

    return graph

# Main function to run the program
if __name__ == "__main__":
    graph = create_graph()
    start_node = input("Enter the starting node for Dijkstra's algorithm: ")
    distances = dijkstra(graph, start_node)
    
    print(f"Shortest distances from {start_node}:")
    for vertex, distance in distances.items():
        print(f"Distance to {vertex}: {distance}")
