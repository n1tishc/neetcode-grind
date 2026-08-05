class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        maxArea = 0

        def dfs(r, c):
            # Base case
            if (
                r < 0 or c < 0 or r >= rows or c >= cols or
                grid[r][c] != 1
            ):
                # print(area)
                return 0
            
            grid[r][c] = 0
            
            # Traverse in all 4 possible directions
            area = 1
            for dr, dc in dirs:
                area += dfs(r + dr, c + dc)
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))
        # print(maxArea)
        return maxArea