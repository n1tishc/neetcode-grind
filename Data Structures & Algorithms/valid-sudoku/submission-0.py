class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Hashset might increase the complexity fro space, the bets TC => O(n^2)
        # Best SC, if hashset => O(n^2), as the max for rows and cols is 9, 
        # we can use brute force and it will not exceed n
        # Brute force TC => O(3 x n^2) => O(n^2)

        for row in range(9):
            seen = set()
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])
        
        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])
        
        for sub in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (sub // 3) * 3 + i
                    col = (sub % 3) * 3 + j

                    if board[row][col] == ".":
                        continue 
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        
        return True



        