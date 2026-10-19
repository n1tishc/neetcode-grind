class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        freq = [
            [] for _ in range(len(nums) + 1)
        ]

        # fill the counts map
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        
        # Fill the frequency of elmets that occur 

        for key, val in counts.items():
            freq[val].append(key)
        

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res