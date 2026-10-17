class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course ot its prereq

        # premap = {i: [] for i in range(numCourses)}

        # for src, dest in prerequisites:
        #     premap[src].append(dest)
        
        # # set to keep track of cycles
        # visited = set()

        # def dfs(crs):
        #     if crs in visited:
        #         # cycle 
        #         return False 
            
        #     if premap[crs] == []:
        #         return True
            
        #     visited.add(crs)
        #     for pre in premap[crs]:
        #         if not dfs(pre):
        #             return False
        #     visited.remove(crs)
        #     premap[crs] = []
        #     return True 
        
        # for i in range(numCourses):
        #     if not dfs(i):
        #         return False
        # return True

        # Khan's Algo 

        # Uses BFS instead of DFS
        freqMap = [0] * numCourses

        adj = [
            [] for _ in range(numCourses)
        ]

        for src, dest in prerequisites:
            freqMap[dest] += 1
            adj[src].append(dest)
        

        q = deque()
        for n in range(numCourses):
            if freqMap[n] == 0:
                q.append(n)
        

        res = 0

        while q:
            node = q.popleft()
            res += 1
            for new in adj[node]:
                freqMap[new] -= 1
                if freqMap[new] == 0:
                    q.append(new)
        
        return res == numCourses
