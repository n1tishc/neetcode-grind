class Solution:
    def solve(self, board: List[List[str]]) -> None:

        # We can do the problem in 3 passes

        rows, cols = len(board), len(board[0])

        # First we caheck for unsurrounded regions, basically the regions that dont satusfy
        # the condition mentioned

        def dfs(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != "O":
                return
            
            board[r][c] = "T" #Temp place holder to mark unsurrounded

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        
        # Next we mark all the un-surrounded regions aka the dfs from "O" in the border
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][cols-1] == "O":
                dfs(r, cols-1)
        
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rows-1][c] == "O":
                dfs(rows-1, c)
        
        # print(board)
        # Last pass where we just convert the 
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"