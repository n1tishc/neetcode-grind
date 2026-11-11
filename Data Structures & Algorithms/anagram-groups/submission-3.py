class Solution:
    # Key will be a tuple of char frequency in the word
    def make_key(self, word):
        key = [0] * 26
        for ch in word:
            key[ord(ch) - ord('a')] += 1
        return tuple(key)
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            key = self.make_key(word)
            groups[key].append(word)
        # print(groups)
        return list(groups.values())
