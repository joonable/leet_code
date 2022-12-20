# Given two strings s and t, determine if they are isomorphic. 
# 
#  Two strings s and t are isomorphic if the characters in s can be replaced to 
# get t. 
# 
#  All occurrences of a character must be replaced with another character while 
# preserving the order of characters. No two characters may map to the same 
# character, but a character may map to itself. 
# 
#  
#  Example 1: 
#  Input: s = "egg", t = "add"
# Output: true
#  
#  Example 2: 
#  Input: s = "foo", t = "bar"
# Output: false
#  
#  Example 3: 
#  Input: s = "paper", t = "title"
# Output: true
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 5 * 10⁴ 
#  t.length == s.length 
#  s and t consist of any valid ascii character. 
#  
# 
#  Related Topics Hash Table String 👍 5618 👎 1091


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # list_s = list(s)
        if len(set(s)) != len(set(t)):
            return False

        dict_s_t = {}
        for i, (_s, _t) in enumerate(zip(list(s), list(t))):
            if _s in dict_s_t.keys():
                if dict_s_t[_s] != _t:
                    return False
            else:
                dict_s_t[_s] = _t

        if len(dict_s_t.values()) != len(dict_s_t.values()):
            return False

        return True

# leetcode submit region end(Prohibit modification and deletion)
