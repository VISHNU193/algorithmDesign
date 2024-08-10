
class Disjoin_set:

    def __init__(self,vertices):
        self.parent = {v:v for v in vertices}
        self.rank = {v:0 for v in vertices}

    def find(self,vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self,v1,v2):
        r1 = self.find(v1)
        r2 = self.find(v2)

        if r1 != r2:
            if self.rank[r1] > self.rank[r2]:
                self.parent[r2] = r1
            elif self.rank[r1] < self.rank[r2]:
                self.parent[r1] = r2
            else:
                self.parent[r2] = r1
                self.rank[r1] += 1


def kruskal(g:dict[str,dict]):
    mst =[]
    edges = [(w,u,v) for u in g for v,w in g[u].items()]
    edges.sort()
    disjoint_set = Disjoin_set(g.keys())
    total_cost =0
    for w,u,v in edges:
        if disjoint_set.find(u) != disjoint_set.find(v):

            disjoint_set.union(u, v)
            mst.append((u, v, w))
            total_cost += w
    return mst,total_cost


graph_q = {
    "A":{"B":5,"C":10},
    "B":{"A":5,"C":4,"D":1},
    "C":{"A":10,"B":4,"D":5},
    "D":{"B":1,"C":5}
}

mst, cost = kruskal(graph_q)
print(mst)
print(cost)