# Given an array of strings strs, group the anagrams together. You can return 
# the answer in any order. 
# 
#  An Anagram is a word or phrase formed by rearranging the letters of a 
# different word or phrase, typically using all the original letters exactly once. 
# 
#  
#  Example 1: 
#  Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#  
#  Example 2: 
#  Input: strs = [""]
# Output: [[""]]
#  
#  Example 3: 
#  Input: strs = ["a"]
# Output: [["a"]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= strs.length <= 10⁴ 
#  0 <= strs[i].length <= 100 
#  strs[i] consists of lowercase English letters. 
#  
# 
#  Related Topics Array Hash Table String Sorting 👍 18880 👎 601


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Runtime:85 ms, faster than 78.17% of Python3 online submissions.
        Memory Usage:19.4 MB, less than 88.89% of Python3 online submissions.
        """
        # O(n * k) 방식
        dict_str = {}
        for _str in strs:
            sorted_str = "".join(sorted(_str))
            dict_str[sorted_str] = dict_str.get(sorted_str, []) + [_str]
        list_result = list(dict_str.values())
        return list_result

# leetcode submit region end(Prohibit modification and deletion)
