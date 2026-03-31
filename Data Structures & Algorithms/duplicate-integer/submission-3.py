class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_values = set(nums)

        if len(nums) > len(set_values):
            return True
        else:
            return False