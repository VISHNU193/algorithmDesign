import heapq

graph_q = {
    "A":[("B",5),("C",10)],
    "B":[("A",5),("C",4),("D",11)],
    "C":[("A",10),("B",4),("D",5)],
    "D":[("B",11),("C",5)]
}


def prim(graph:dict,start):
    mst =[]
    visited = set()
    pq=[(0,start,None)]
    total_cost=0
    while pq:
        w,curr_node,prev_node = heapq.heappop(pq)
        if curr_node in visited:
            continue

        visited.add(curr_node)
        total_cost += w

        if prev_node is not None:
            mst.append((prev_node,curr_node,w))

        for neighbor,edge_weight in graph[curr_node]:
            if neighbor not in visited:
                heapq.heappush(pq,(edge_weight,neighbor,curr_node))
    return mst,total_cost


start_node = "A"
mst, cost = prim(graph_q,start_node)
print(mst)
print(cost)