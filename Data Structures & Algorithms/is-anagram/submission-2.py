class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26

        # If theya re anagrams then the logic saying
        # Add ord(s[i]) - ord('a'), then subtract ord([t[i]]) - ord('a')
        # If they are anagrams the array will be all 0's

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for val in count:
            if val != 0:
                return False
        return True