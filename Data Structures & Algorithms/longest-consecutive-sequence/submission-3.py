class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
            Brute Force:
                Sorting all the elements and check for continous elements
            TC:
                O(nlogn)?
        """

        if not nums:
            return 0
        
        numSet = set(nums)

        longest = 1

        for num in numSet:
            if (num + 1) in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        # print(longest)
        return longest





