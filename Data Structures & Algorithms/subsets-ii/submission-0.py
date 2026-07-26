class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # For duplicates in the array, we can skip consecutive elements
        res = []

        def recur(index, temp):
            res.append(temp[::])

            for j in range(index, len(nums)):
                if j > index and nums[j] == nums[j-1]:
                    continue
                temp.append(nums[j])
                recur(j + 1, temp)
                temp.pop()
        
        recur(0, [])
        # print(res)
        return res