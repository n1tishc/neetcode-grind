class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Multiple BFS approach
        rows, cols = len(grid), len(grid[0])
        visited = set()
        queue = deque()

        def addCell(r, c):
            if (
                min(r, c) < 0 or r == rows or c == cols or
                (r, c) in visited or grid[r][c] == -1
            ):
                return
            
            visited.add((r, c))
            queue.append([r, c])

        # Get all the treasure chests location
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append([r, c])
                    visited.add((r, c))
        
        # Multi-BFS

        dist = 0
        dirs = [
            [-1, 0],
            [1, 0],
            [0, -1],
            [0, 1]
        ]
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist

                # Explore all 4 directions
                for x, y in dirs:
                    addCell(r + x, c + y)
            
            dist += 1

