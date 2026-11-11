class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros = 0 # Gives idea on flips to be made
        res = 0

        for right in range(len(nums)):
            # If we get zero, increase the zero counter
            if nums[right] == 0:
                zeros += 1
            
            # When the size of zeros is greater than the limit k
            while zeros > k: 
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            res = max(res, right - left + 1)
        return res