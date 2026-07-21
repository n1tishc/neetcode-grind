class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # Classic backtracking problem
        # Base case
        if len(nums) < 1:
            return []
        if len(nums) == 1:
            return [[], nums]
        
        # Backtracking
        res = [[]]

        for num in nums:
            res += [subset + [num] for subset in res]
        # print(res)
        return res

        