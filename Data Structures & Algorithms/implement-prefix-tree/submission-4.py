class Node:
    def __init__(self , key):
        self.key = key
        self.children ={}
        self.end = False


class PrefixTree:

    def __init__(self):
        self.root = Node("")

    def insert(self, word: str) -> None:
        root = self.root
        for w in word:
            if w not in root.children:
                new_node = Node(w)
                root.children[w] = new_node
            root = root.children[w]
        root.end = True

    def search(self, word: str) -> bool:
        root = self.root
        for w in word:
            if w not in root.children:
                return False
            root = root.children[w]
        return root.end

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for w in prefix:
            if w not in root.children:
                return False
            root = root.children[w]
        return True
        