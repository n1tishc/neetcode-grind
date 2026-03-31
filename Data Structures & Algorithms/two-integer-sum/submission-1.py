class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We store num:index in a dict
        # For each iteration we store curr_num:i
        # Then we find the diff with target
        # IF difference exists in the dict, we return indexes

        count = {}

        for index, val in enumerate(nums):
            diff = target - val

            if diff in count:
                return [count[diff], index]
            count[val] = index
            