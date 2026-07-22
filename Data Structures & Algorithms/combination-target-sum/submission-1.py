class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # Edge case:
        res = []
        
        def recur(index, curr, total):
            # base case
            if total == target:
                res.append(curr.copy())
                return 
            if index >= len(nums) or total > target:
                return
            
            # pick and no-pick condition 
            curr.append(nums[index])
            recur(index, curr, total + nums[index])
            curr.pop()
            recur(index + 1, curr, total)
        
        recur(0, [], 0)
        # print(res)
        return res
