class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows, cols = len(board), len(board[0])
        
        def recur(row, col, idx):

            # base case
            if idx == len(word):
                return True
            if (row < 0 or col < 0 or row >= rows or col >= cols or word[idx] != board[row][col] or board[row][col] == '#') :
                return False
            
            # Go in all 4 directions 
            board[row][col] = '#'
            res = (
                recur(row + 1, col, idx + 1) or
                recur(row - 1, col, idx + 1) or
                recur(row, col + 1, idx + 1) or
                recur(row, col - 1, idx + 1)
            )
            # Word not found, reset board
            board[row][col] = word[idx]
            return res
        
        for row in range(rows):
            for col in range(cols):
                if recur(row, col, 0):
                    return True
        return False