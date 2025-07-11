graph = { 
    'A': ['B', 'C'], 
    'B': ['D', 'E'], 
    'C': ['F'], 
    'D': [], 
    'E': ['F'], 
    'F': [] 
} 
def dfs(graph, start, visited=None): 
    if visited is None: 
        visited = set() 
    visited.add(start)  
    for neighbor in graph[start]: 
        if neighbor not in visited: 
            dfs(graph, neighbor, visited)  
    return visited 
print("DFS traversal from node A:", dfs(graph, 'A'))
