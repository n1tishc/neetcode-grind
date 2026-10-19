class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Brute force : TC: O(n * k) 

        res = []
        q = deque()

        for idx, num in enumerate(nums):

            while q and nums[q[-1]] < num:
                q.pop()
            
            q.append(idx)

            # pop first element
            if q[0] == idx - k:
                q.popleft()
            
            if idx >= k - 1:
                res.append(nums[q[0]])
        return res