# algorithm1.py
# Naive Approach: Minimum Spanning Tree using DFS for Cycle Detection
import sys

# زيادة حد التكرار لتجنب الخطأ مع الشبكات الكبيرة
sys.setrecursionlimit(20000)

def has_path_dfs(adj, current, target, visited):
    """
    دالة DFS للتأكد من وجود مسار بين نقطتين.
    ترجع True إذا وجد مسار (يعني إضافة الكابل ستصنع دائرة).
    """
    if current == target:
        return True
    visited.add(current)
    for neighbor in adj.get(current, []):
        if neighbor not in visited:
            if has_path_dfs(adj, neighbor, target, visited):
                return True
    return False

def run_naive_mst(num_buildings, all_edges):
    """
    تنفيذ الخوارزمية الساذجة.
    Input: عدد المباني، قائمة بكل الكابلات الممكنة (u, v, weight)
    Output: الكابلات المختارة، التكلفة الكلية
    """
    # 1. ترتيب الكابلات تصاعدياً حسب الوزن
    sorted_edges = sorted(all_edges, key=lambda x: x[2])
    
    mst_edges = []
    mst_cost = 0
    adj = {i: [] for i in range(num_buildings)}
    count = 0
    
    for u, v, w in sorted_edges:
        if count == num_buildings - 1:
            break
        
        # 2. التحقق الساذج (Naive Check) باستخدام DFS
        visited = set()
        if not has_path_dfs(adj, u, v, visited):
            mst_edges.append((u, v, w))
            mst_cost += w
            adj[u].append(v)
            adj[v].append(u)
            count += 1
            
    return mst_edges, mst_cost