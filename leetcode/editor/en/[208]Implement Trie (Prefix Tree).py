from collections import defaultdict

class Node:
    def __init__(self):
        self.is_end = False
        self.children = defaultdict(Node)

class Trie():
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.is_end = True

    def _starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def start_with(self, prefix):
        node = self._starts_with(prefix)
        return node is not None

    def search(self, word):
        node = self._starts_with(word)
        return node.is_end if node else False

# class Trie:
#     def __init__(self):
#         self.head = Node()
#
#     def insert(self, word: str) -> None:
#         node = self.head
#         for ch in word:
#             node = node.children[ch]
#         node.is_end = True
#
#     def search(self, word: str) -> bool:
#         node = self._startsWith(self.head, word)
#         return node.is_end if node is not None else False
#
#     def startsWith(self, prefix: str) -> bool:
#         node = self._startsWith(self.head, prefix)
#         return True if node is not None else False
#
#     def _startsWith(self, node, prefix: str):
#         for ch in prefix:
#             if ch not in node.children:
#                 return None
#             node = node.children[ch]
#         return node

# class Trie:
#     def __init__(self):
#         self.head = Node()

#     def insert(self, word: str) -> None:
#         def dfs_insert(node, word):
#             ch = word[0]

#             is_end = True if len(word) == 1 else False
#             if ch in node.children:
#                 node.children[ch].is_end = is_end or node.children[ch].is_end
#             else:
#                 node.children[ch] = Node(is_end)

#             if not is_end:
#                 dfs_insert(node.children[ch], word[1:])

#         dfs_insert(self.head, word)

#     def search(self, word: str) -> bool:
#         def dfs_search(node, word):
#             if not word:
#                 return node.is_end

#             ch = word[0]
#             if ch not in node.children:
#                 return False

#             return dfs_search(node.children[ch], word[1:])

#         return dfs_search(self.head, word)

#     def startsWith(self, prefix: str) -> bool:
#         def dfs_startsWith(node, word):
#             if not word:
#                 return True

#             ch = word[0]
#             if ch not in node.children:
#                 return False

#             return dfs_startsWith(node.children[ch], word[1:])
#         return dfs_startsWith(self.head, prefix)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)