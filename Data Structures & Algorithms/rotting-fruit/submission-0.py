class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        fresh = 0
        time = 0

        # get count of fresh and rotten fruits
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    queue.append((row, col))
        
        directions = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0]
        ]
        while fresh > 0 and queue:

            qlen = len(queue)

            for val in range(qlen):
                row, col = queue.popleft()

                for r, c in directions:
                    nrow, ncol = row + r, col + c

                    if (nrow in range(len(grid)) and ncol in range(len(grid[0])) and grid[nrow][ncol] == 1):
                        grid[nrow][ncol] = 2
                        queue.append((nrow, ncol))
                        fresh -= 1
            time += 1
            print(fresh, time)
        
        return time if fresh == 0 else -1
