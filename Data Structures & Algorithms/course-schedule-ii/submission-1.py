class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Use Khan's algo to find the best one

        inDegree = [0] * numCourses
        # Adj List rep if the prerequisites
        adj = [
            [] for _ in range(numCourses)
        ]

        for crs, pre in prerequisites:
            inDegree[pre] += 1
            adj[crs].append(pre)
        
        # Add all the nodes with just outgoign edges to queue
        q = deque()
        for node in range(numCourses):
            if inDegree[node] == 0:
                q.append(node)
        
        res = []

        while q:
            node = q.popleft()
            res.append(node)

            for newNode in adj[node]:
                inDegree[newNode] -= 1
                if inDegree[newNode] == 0:
                    q.append(newNode)
        
        return res[::-1] if len(res) == numCourses else []