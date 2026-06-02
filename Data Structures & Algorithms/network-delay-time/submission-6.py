import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Generate adjacencyy list
        graph = defaultdict(list)

        for u, v, time in times:
            graph[u].append((v, time))
        
        # print(graph)
        min_times = {}
        min_heap = [(0, k)] # k -> source node

        while min_heap:
            k_to_i, i = heapq.heappop(min_heap)
            if i in min_times:
                continue
            
            min_times[i] = k_to_i

            for nei, n_time in graph[i]:
                if nei not in min_times:
                    heapq.heappush(min_heap, (n_time + k_to_i, nei))
        
        print(min_times)
        print(len(min_times))
        
        return max(min_times.values()) if len(min_times) == n else -1