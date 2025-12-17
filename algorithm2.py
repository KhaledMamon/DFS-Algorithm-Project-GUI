

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        
        if root_i != root_j:
            if self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            elif self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True 
        return False 

def run_optimized_mst(num_buildings, all_edges):
    sorted_edges = sorted(all_edges, key=lambda x: x[2])
    
    mst_edges = []
    mst_cost = 0
    uf = UnionFind(num_buildings)
    count = 0
    
    for u, v, w in sorted_edges:
        if count == num_buildings - 1:
            break
            
        if uf.union(u, v):
            mst_edges.append((u, v, w))
            mst_cost += w
            count += 1
            
    return mst_edges, mst_cost
