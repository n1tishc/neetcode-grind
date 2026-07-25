class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def back(perm, vals, picks):
            if len(perm) == len(vals):
                res.append(perm[:])
                return
            for i in range(len(vals)):
                if not picks[i]:
                    perm.append(vals[i])
                    picks[i] = True
                    back(perm, vals, picks)
                    perm.pop()
                    picks[i] = False
        
        back([], nums, [False] * len(nums))
        # print(res)
        return res