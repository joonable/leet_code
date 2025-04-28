# You are given a string s, and an array of pairs of indices in the string 
# pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string. 
# 
#  You can swap the characters at any pair of indices in the given pairs any 
# number of times. 
# 
#  Return the lexicographically smallest string that s can be changed to after 
# using the swaps. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "dcab", pairs = [[0,3],[1,2]]
# Output: "bacd"
# Explaination: 
# Swap s[0] and s[3], s = "bcad"
# Swap s[1] and s[2], s = "bacd"
#  
# 
#  Example 2: 
# 
#  
# Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
# Output: "abcd"
# Explaination: 
# Swap s[0] and s[3], s = "bcad"
# Swap s[0] and s[2], s = "acbd"
# Swap s[1] and s[2], s = "abcd" 
# 
#  Example 3: 
# 
#  
# Input: s = "cba", pairs = [[0,1],[1,2]]
# Output: "abc"
# Explaination: 
# Swap s[0] and s[1], s = "bca"
# Swap s[1] and s[2], s = "bac"
# Swap s[0] and s[1], s = "abc"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10^5 
#  0 <= pairs.length <= 10^5 
#  0 <= pairs[i][0], pairs[i][1] < s.length 
#  s only contains lower case English letters. 
#  
# 
#  Related Topics Array Hash Table String Depth-First Search Breadth-First 
# Search Union Find Sorting 👍 3812 👎 153


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path Compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)

        # Step 1: Union indices according to pairs
        for x, y in pairs:
            uf.union(x, y)

        # Step 2: Group characters by their root
        char_group = defaultdict(list)
        for i, c in enumerate(s):
            char_group[uf.find(i)].append(c)

        # Step 3: Sort each group's characters in descending order
        for chars in char_group.values():
            chars.sort(reverse=True)

        # Step 4: Build the result by popping the smallest available character
        return "".join(char_group[uf.find(i)].pop() for i in range(n))

# leetcode submit region end(Prohibit modification and deletion)
