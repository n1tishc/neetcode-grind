class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            val = ord(c) - ord('a') # Convert char to range b/w ( 0 to 26)
            if cur.children[val] == None:
                cur.children[val] = TrieNode()
            cur = cur.children[val]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            val = ord(c) - ord('a')
            if cur.children[val] == None:
                return False
            cur = cur.children[val]
        return cur.endOfWord        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            val = ord(c) - ord('a')
            if cur.children[val] == None:
                return False
            cur = cur.children[val]
        # return cur.endOfWord
        return True
        
        