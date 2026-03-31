class Solution:
    def rob(self, nums: List[int]) -> int:
        # Run the robber problem twice, thats it
        # One run from start, and one run from end
        def robber_func(nums):
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
        
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(robber_func(nums[1:]), robber_func(nums[:-1]))