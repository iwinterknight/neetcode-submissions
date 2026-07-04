class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminal = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()        

    def insert(self, word: str) -> None:
        ptr = self.root
        for c in word:
            if c not in ptr.children:
                ptr.children[c] = TrieNode()
            ptr = ptr.children[c]
        ptr.terminal = True

    def search(self, word: str) -> bool:
        if not self.root:
            return False
        ptr = self.root
        for c in word:
            if c not in ptr.children:
                return False
            ptr = ptr.children[c]
        if ptr.terminal:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        if not self.root:
            return False
        ptr = self.root
        for c in prefix:
            if c not in ptr.children:
                return False
            ptr = ptr.children[c]
        return True
        