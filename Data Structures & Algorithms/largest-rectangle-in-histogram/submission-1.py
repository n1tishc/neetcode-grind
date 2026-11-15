class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [-1] * n
        right = [n] * n

        for i in range(n):
            idx = i - 1

            while idx >= 0 and heights[idx] >= heights[i]:
                idx = left[idx]
            
            left[i] = idx
        
        for i in range(n -1, -1, -1):
            idx = i + 1

            while idx < n and heights[idx] >= heights[i]:
                idx = right[idx]
            
            right[i] = idx
        
        # print(left, right)

        maxArea = 0
        for i in range(n):
            maxArea = max(
                maxArea,
                heights[i] * ((right[i] - 1) - (left[i] + 1) + 1 )
            )
        return maxArea