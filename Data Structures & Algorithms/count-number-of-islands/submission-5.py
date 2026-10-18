class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # I dont need it to return any true or false
        # Just fill the 1's as 0's when visited 

        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            # Break condition

            if (
                r < 0 or c < 0 or r >= rows or c >= cols or 
                grid[r][c] == '0'
            ):
                return 
            
            # Move in all 4 possible directions
            grid[r][c] = "0"
            for dr, dc in dirs:
                dfs(r + dr, c + dc)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    islands += 1
        # print(grid)
        return islands