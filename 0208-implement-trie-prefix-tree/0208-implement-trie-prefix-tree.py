class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.endWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        
        for ch in word:
            if ch not in cur.children: # current char hasn't been created yet in map
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.endWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        
        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return cur.endWord # reached end word set in insert function

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        
        for ch in prefix:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)