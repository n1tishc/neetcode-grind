class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort the array to traverse in order 
        res = []
        candidates.sort()

        def recur(index, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or index == len(candidates):
                return 
            
            curr.append(candidates[index])
            recur(index + 1, curr, total + candidates[index])
            curr.pop()

            while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1
            recur(index + 1, curr, total)
        
        recur(0, [], 0)
        return res