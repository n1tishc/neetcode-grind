class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph, indegree, finish = {}, {}, {}

        for i in range(n):
            graph[i] = []
            indegree[i] = 0
            finish[i] = time[i]
        
        for task, before in relations:
            graph[before-1].append(task-1)
            indegree[task-1] += 1
        
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        
        done = 0
        while q:
            node = q.popleft()
            done += 1

            for nxt in graph[node]:
                finish[nxt] = max(
                    finish[nxt],
                    finish[node] + time[nxt]
                )
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        return max(finish.values()) if done == n else -1