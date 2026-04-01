class Solution:

    def encode(self, strs: List[str]) -> str:
        # Append the len(string) and strings with a delimiter
        res = ""
        for val in strs:
            res += str(len(val)) + "#" + val
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            # Find the index of length
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        
        return res
            

    
# test = Solution()
# print(test.encode(["Hello", "World"]))
# exp = test.encode(["Hello", "World"])