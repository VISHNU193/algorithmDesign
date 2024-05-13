
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

color = {
    1: "",
    2: "",
    3: "",
    4: "",
    5: "",
    6: "",
    7: "",
    8: "",
    9: "",
    10: "",
}
def bfs(graph,s):
    visited = [False] * (len(graph)+3)
    queue = []
    if s in graph.keys():
        print(f"Visited {s}")
        queue.append(s)
        visited[s] = True
        color[s] = "red"
        current_color = "blue"

        while queue:
            current_node = queue.pop(0)
            if color[current_node] == "red":
                current_color = "blue"
            else:
                current_color = "red"

            for neighbour in graph[current_node]:
                if not visited[neighbour]:
                    color[neighbour] = current_color
                    print(f"Visited {neighbour} ")
                    queue.append(neighbour)
                    visited[neighbour] = True


    else:
        print(f"Vertex {s} is not present in graph")

bfs(graph_queston,1)
print(color)

rc = 0
bc = 0
for x in color.values():
    if x== "red":
      rc +=1
    else:
        bc +=1

print(rc)
print(bc)