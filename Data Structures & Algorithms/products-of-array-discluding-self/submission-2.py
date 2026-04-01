class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # # Brute Force => TC: O(n^2), SC: O(n)
        # res = [0] * len(nums)
        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         prod *= nums[j]
        #     res[i] = prod
        # return res

        # Prefix and Suffix
        # n = len(nums)
        # res = [0] * n
        # prefix = [0] * n
        # suffix = [0] * n

        # # Base case
        # prefix[0] = suffix[n-1] = 1

        # for i in range(1, n):
        #     prefix[i] = nums[i-1] * prefix[i-1]

        # for i in range(n-2, -1, -1):
        #     suffix[i] = nums[i+1] * suffix[i+1]
        
        # for i in range(n):
        #     res[i] = prefix[i] * suffix[i]
        
        # return res

        n = len(nums)
        res, prefix, sufix = [0] * n, [0] * n, [0] * n

        # Base Cases
        prefix[0] = sufix[n-1] = -1

        # First find all prefix values
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        # Sufix prods values
        for j in range(n-2, -1, -1):
            sufix[j] = sufix[j+1] * nums[j+1]
        
        # Fill res values
        for i in range(n):
            res[i] = prefix[i] * sufix[i]
        
        return res