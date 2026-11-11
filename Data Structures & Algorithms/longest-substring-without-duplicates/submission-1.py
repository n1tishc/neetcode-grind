class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        left, ans = 0, 0

        for right in range(len(s)):
            if s[right] in mp:
                left = max(mp[s[right]] + 1, left)
            mp[s[right]] = right
            ans = max(ans, right - left + 1)
        return ans