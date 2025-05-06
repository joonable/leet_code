# Design a data structure that supports adding new words and finding if a 
# string matches any previously added string. 
# 
#  Implement the WordDictionary class: 
# 
#  
#  WordDictionary() Initializes the object. 
#  void addWord(word) Adds word to the data structure, it can be matched later. 
# 
#  bool search(word) Returns true if there is any string in the data structure 
# that matches word or false otherwise. word may contain dots '.' where dots can 
# be matched with any letter. 
#  
# 
#  
#  Example: 
# 
#  
# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search",
# "search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]
# 
# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= word.length <= 25 
#  word in addWord consists of lowercase English letters. 
#  word in search consist of '.' or lowercase English letters. 
#  There will be at most 2 dots in word for search queries. 
#  At most 10⁴ calls will be made to addWord and search. 
#  
# 
#  Related Topics String Depth-First Search Design Trie 👍 7838 👎 474


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


class Node:     # important
    def __init__(self, is_end=False):
        self.is_end = is_end
        self.children = defaultdict(Node)

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.is_end = True  # important

    def search(self, word: str) -> bool:
        node = self.root
        n = len(word)

        def dfs(node, i):
            if i >= n:
                return node.is_end

            ch = word[i]
            if ch != ".":
                if ch in node.children:
                    return dfs(node.children[ch], i + 1)
            else:
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
            return False

        return dfs(node, 0)

    # def search(self, word: str) -> bool:
    #     def _dfs(word: str, node: Node) -> bool:
    #         if not word:
    #             return node.is_end  # important
    #
    #         ch = word[0]
    #         if ch != '.':
    #             if ch not in node.children:
    #                 return False
    #             return _dfs(word[1:], node.children[ch])
    #         else:
    #             for child in node.children.values():    # important
    #                 if _dfs(word[1:], child):   # important
    #                     return True
    #             return False
    #
    #     return _dfs(word, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# leetcode submit region end(Prohibit modification and deletion)
