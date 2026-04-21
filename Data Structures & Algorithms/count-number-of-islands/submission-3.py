class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        # 4 Directions to move in teh grid
        
        res = 0

        def dfs(row, col):

            # Base condition

            if (
                row < 0 or col < 0 or row >= rows or col >= cols
                or grid[row][col] == "0"
            ):
                return
            
            grid[row][col] = "0"

            # dfs in all 4 directions

            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    res += 1
        
        return res