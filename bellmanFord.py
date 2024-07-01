
graph = {
    "A":[("B",5),("C",10)],
    "B":[("A",5),("C",4),("D",11)],
    "C":[("A",10),("B",4),("D",5)],
    "D":[("B",11),("C",5)]
}

class BellmanFord:
    def __init__(self,v):
        self.v = v
        self.graph=[]

    def addEdge(self,u,v,w):
        self.graph.append((u,v,w))

    def shortestDist(self,src):
        dist = [float("Inf")]*(self.v)
        dist[src] = 0

        for _ in range(self.v - 1):
            for u,v,w in self.graph:
                if dist[u] != float("Inf") and dist[u]+w<dist[v]:
                    dist[v] = dist[u] + w

        for u,v,w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Negative edge cycle exists")
                return

        print("Shortest distances : ", dist)

g = BellmanFord(4)
g.addEdge(0,1,5)
g.addEdge(0,2,5)
g.addEdge(1,2,5)
g.addEdge(2,3,5)
g.addEdge(3,1,-10)
g.shortestDist(0)