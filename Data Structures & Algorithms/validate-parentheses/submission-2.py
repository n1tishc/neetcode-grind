class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracMap = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for ch in s:
            if ch in bracMap:
                if stack and stack[-1] == bracMap[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        return True if not stack else False