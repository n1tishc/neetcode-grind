class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        # 4 Directions to move in teh grid
        directions = [[1,0], [-1,0], [0,1], [0, -1]]

        res = 0

        def dfs(r, c):
            # Break case
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0"):
                return 
            
            grid[r][c] = "0"
            for d1, d2 in directions:
                dfs(r + d1, c + d2)
        

        # Iteerate all rows and cols
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    res += 1
        
        return res