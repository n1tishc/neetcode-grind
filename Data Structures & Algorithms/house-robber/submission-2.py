class Solution:
    def rob(self, nums: List[int]) -> int:
        # Max of values at odd positions and even positions

        # odd, even = 0, 0

        # for i in range(len(nums)):
        #     if i % 2 == 0:
        #         even += nums[i]
        #     else:
        #         odd += nums[i]
        
        # return max(odd, even)

        # Each step we havet two options, skip the curr house or rob this house
        # and skip the next house

        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        return dp[-1]