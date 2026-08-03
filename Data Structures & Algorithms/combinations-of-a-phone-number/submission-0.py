class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # Hash map containing all pairr

        keypad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def backtrack(index, curr):
            if len(curr) == len(digits):
                res.append(curr)
                return
            
            for c in keypad[digits[index]]:
                backtrack(index + 1, curr + c)
        
        if digits:
            backtrack(0, "")
        
        return res
            
        