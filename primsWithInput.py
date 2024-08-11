import heapq

def prim(graph, start):
    mst = []
    visited = set([start])
    edges = [(cost, start, to) for to, cost in graph[start]]
    heapq.heapify(edges)
    total_cost = 0
    
    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, cost))
            total_cost += cost
            
            for next_to, next_cost in graph[to]:
                if next_to not in visited:
                    heapq.heappush(edges, (next_cost, to, next_to))
    
    return mst, total_cost

# Function to create the graph from user input
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
    print(graph)
    start_node = input("Enter the starting node for Prim's algorithm: ")
    mst, total_cost = prim(graph, start_node)
    
    print("Minimum Spanning Tree (MST) edges and weights:")
    for frm, to, weight in mst:
        print(f"{frm} - {to} : {weight}")
    
    print(f"Total minimum cost: {total_cost}")