class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # recuresive

        # def dfs(node):
        #     if node >= len(cost):
        #         return 0
        #     return min(dfs(node + 1), dfs(node + 2)) + cost[node]
        
        # return min(dfs(0), dfs(1))

        # Dp
        n = len(cost)
        dp = [0] * (n+1)

        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        
        return dp[n]