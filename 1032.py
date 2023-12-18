class Node:
    def __init__(self):
        self.word_ends = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root_node = Node()


    def add_word(self,word):
        current_node = self.root_node
        for c in word:
            if c not in current_node.children.keys():
                current_node.children[c] = Node()
            current_node = current_node.children[c]

        current_node.word_ends = True

    def search_word(self,dq): 
        current_node = self.root_node

        for c in dq:
            if c not in current_node.children.keys():
                return False
           
            current_node = current_node.children[c]
            if current_node.word_ends:
                return True

        return False 

class StreamChecker:

    def __init__(self, words: List[str]):
        self.max_len = 0
        self.trie = Trie()
        
        for w in words:
            self.trie.add_word(w[::-1])
            self.max_len = max(self.max_len, len(w))

        self.current_collection = deque([])

    def query(self, letter: str) -> bool:
        if len(self.current_collection) >= self.max_len:
            self.current_collection.pop()
        self.current_collection.appendleft(letter)
        return self.trie.search_word(self.current_collection)


        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
