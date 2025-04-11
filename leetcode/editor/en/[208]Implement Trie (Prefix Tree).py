# A trie (pronounced as "try") or prefix tree is a tree data structure used to 
# efficiently store and retrieve keys in a dataset of strings. There are various 
# applications of this data structure, such as autocomplete and spellchecker. 
# 
#  Implement the Trie class: 
# 
#  
#  Trie() Initializes the trie object. 
#  void insert(String word) Inserts the string word into the trie. 
#  boolean search(String word) Returns true if the string word is in the trie (
# i.e., was inserted before), and false otherwise. 
#  boolean startsWith(String prefix) Returns true if there is a previously 
# inserted string word that has the prefix prefix, and false otherwise. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]
# 
# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= word.length, prefix.length <= 2000 
#  word and prefix consist only of lowercase English letters. 
#  At most 3 * 10⁴ calls in total will be made to insert, search, and 
# startsWith. 
#  
# 
#  Related Topics Hash Table String Design Trie 👍 11972 👎 148


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


class Node:
    def __init__(self, is_end=False):
        # important: key == value 이므로 value 불필요
        self.is_end = is_end
        self.children = defaultdict(lambda: Node())


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        node = self.head
        for ch in word:
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self._startsWith(self.head, word)
        return node.is_end if node is not None else False

    def startsWith(self, prefix: str) -> bool:
        node = self._startsWith(self.head, prefix)
        return True if node is not None else False

    def _startsWith(self, node, prefix: str):
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

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


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# leetcode submit region end(Prohibit modification and deletion)
