class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, parts = [], []

        def backtrack(i):
            # Base case for the problem
            if i >= len(s):
                res.append(parts.copy())
                return
            
            # Check all possible partitions
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    parts.append(s[i:j + 1])
                    backtrack(j + 1)
                    parts.pop()
            
        backtrack(0)
        return res
    
    def isPalindrome(self, s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True