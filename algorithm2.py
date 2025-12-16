# algorithm2.py
# Optimized Approach: Minimum Spanning Tree using Union-Find Data Structure

class UnionFind:
    """هيكل بيانات Union-Find لإدارة المجموعات المنفصلة بسرعة عالية"""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        # البحث عن الجذر مع ضغط المسار (Path Compression)
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        # دمج مجموعتين (Union by Rank)
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
            return True # تم الدمج بنجاح (لا توجد دائرة)
        return False # هما متصلان بالفعل (توجد دائرة)

def run_optimized_mst(num_buildings, all_edges):
    """
    تنفيذ الخوارزمية المحسنة.
    """
    # 1. ترتيب الكابلات تصاعدياً
    sorted_edges = sorted(all_edges, key=lambda x: x[2])
    
    mst_edges = []
    mst_cost = 0
    uf = UnionFind(num_buildings)
    count = 0
    
    for u, v, w in sorted_edges:
        if count == num_buildings - 1:
            break
            
        # 2. التحقق المحسن (Optimized Check) باستخدام Union-Find
        if uf.union(u, v):
            mst_edges.append((u, v, w))
            mst_cost += w
            count += 1
            
    return mst_edges, mst_cost