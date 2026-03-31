class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Works but the issues is the sort function being used, it 
        # increasesc complexity
        # res = defaultdict(list)

        # for s in strs:
        #     sorted_dict = ''.join(sorted(s))
        #     res[sorted_dict].append(s)
        # return list(res.values())

        # Better approach
        # For each string in the list
        # Get the character frequency of the letters, anagrams will have same char frequency
        # Have a dict that stores tuple(char_freq): [list of strs]
        # Finally return string of values 
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # Character Frequency

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            res[tuple(count)].append(s)
        
        return list(res.values())
