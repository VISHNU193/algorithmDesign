def tsp(graph, v, currPos, n, count, cost, path, best_path):
    if count == n and graph[currPos][0]:
        total_cost = cost + graph[currPos][0]
        if total_cost < best_path[0]:
            best_path[0] = total_cost
            best_path[1] = path + [0] 
        return


    for i in range(n):
        if not v[i] and graph[currPos][i]:
            v[i] = True
            tsp(graph, v, i, n, count + 1, cost + graph[currPos][i], path + [i], best_path)
            v[i] = False

# Driver code
if __name__ == '__main__':
    n = 4
    graph = [[0, 10, 15, 20],
             [10, 0, 35, 25],
             [15, 35, 0, 30],
             [20, 25, 30, 0]]

    v = [False for _ in range(n)]
    v[0] = True  

    best_path = [float('inf'), []] 

    # Find the minimum weight Hamiltonian Cycle
    tsp(graph, v, 0, n, 1, 0, [0], best_path)

    print(f"Minimum cost: {best_path[0]}")
    print(f"Path taken: {' -> '.join(map(str, best_path[1]))}")
