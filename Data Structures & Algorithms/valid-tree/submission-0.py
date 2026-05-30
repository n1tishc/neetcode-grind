class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Base case

        if len(edges) > (n-1):
            return False
        
        # build adjacencey list
        adj = [[] for i in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        # print(adj)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)

            for child in adj[node]:
                if child == parent:
                    continue
                if not dfs(child, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n
