class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # left = 0
        # zeros = 0 # Gives idea on flips to be made
        # res = 0

        # for right in range(len(nums)):
        #     # If we get zero, increase the zero counter
        #     if nums[right] == 0:
        #         zeros += 1
            
        #     # When the size of zeros is greater than the limit k
        #     while zeros > k: 
        #         if nums[left] == 0:
        #             zeros -= 1
        #         left += 1
        #     res = max(res, right - left + 1)
        # return res

        l = res = 0
        for r in range(len(nums)):
            k -= (1 if nums[r] == 0 else 0)
            while k < 0:
                k += (1 if nums[l] == 0 else 0)
                l += 1
            res = max(res, r - l + 1)
        return res