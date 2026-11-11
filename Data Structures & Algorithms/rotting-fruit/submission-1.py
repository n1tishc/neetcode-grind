from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Keep track of time and fresh
        time, fresh = 0, 0

        rows, cols = len(grid), len(grid[0])

        # queue to keep track of all rotten fruits
        q = deque()

        # get track of rotten roanges and fresh orange
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        dirs = [[0,1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1