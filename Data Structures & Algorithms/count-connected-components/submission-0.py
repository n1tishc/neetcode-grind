class UnionFind:

    # Initialzie the parent and rank for union find algo
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, node):
        cur = node
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur
    
    def union(self, u, v):
        nodeu = self.find(u)
        nodev = self.find(v)

        if nodeu == nodev:
            return False
        
        if self.rank[nodev] > self.rank[nodeu]:
            nodev, nodeu = nodeu, nodev
        
        self.parent[nodev] = nodeu
        self.rank[nodeu] += self.rank[nodev]
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Union find method
        unionfind = UnionFind(n)
        res = n

        for u, v in edges:
            if unionfind.union(u, v):
                res -= 1
        
        return res
