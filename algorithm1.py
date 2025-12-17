

def has_path_dfs(adj, current, target, visited):
    if current == target:
        return True
    visited.add(current)
    for neighbor in adj.get(current, []):
        if neighbor not in visited:
            if has_path_dfs(adj, neighbor, target, visited):
                return True
    return False

def run_naive_mst(num_buildings, all_edges):
    sorted_edges = sorted(all_edges, key=lambda x: x[2])
    
    mst_edges = []
    mst_cost = 0
    adj = {i: [] for i in range(num_buildings)}
    count = 0
    
    for u, v, w in sorted_edges:
        if count == num_buildings - 1:
            break
        
        visited = set()
        if not has_path_dfs(adj, u, v, visited):
            mst_edges.append((u, v, w))
            mst_cost += w
            adj[u].append(v)
            adj[v].append(u)
            count += 1
            
    return mst_edges, mst_cost
