# Write a function to find the longest common prefix string amongst an array of 
# strings. 
# 
#  If there is no common prefix, return an empty string "". 
# 
#  
#  Example 1: 
# 
#  
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#  
# 
#  Example 2: 
# 
#  
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= strs.length <= 200 
#  0 <= strs[i].length <= 200 
#  strs[i] consists of only lowercase English letters. 
#  
# 
#  Related Topics String Trie 👍 16365 👎 4302


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Success:
            Runtime:32 ms, faster than 95.52% of Python3 online submissions.
            Memory Usage:16.4 MB, less than 9.54% of Python3 online submissions.
        """
        len_strs = len(strs)
        max_len = 0
        ground_truth = strs[0]

        for i, ch in enumerate(ground_truth):
            for j in range(1, len_strs):
                strs_j = strs[j]
                if len(strs_j) == max_len + 1 or strs_j[j][i] != ch:
                    return strs_j[:max_len+1]
                max_len += 1



    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     """
    #     Success:
    #         Runtime:32 ms, faster than 95.52% of Python3 online submissions.
    #         Memory Usage:16.4 MB, less than 9.54% of Python3 online submissions.
    #     """
    #     if len(strs) == 1:
    #         return strs[0]
    #
    #     min_len = len(min(strs, key=len))
    #
    #     lcm_idx = -1
    #     repre_str = strs[0]
    #     del strs[0]
    #
    #     for idx in range(min_len):
    #         cur_char = repre_str[idx]
    #         for str in strs:
    #             if cur_char != str[idx]:
    #                 return repre_str[:lcm_idx+1]
    #         lcm_idx = idx
    #
    #     return "" if lcm_idx == -1 else repre_str[:lcm_idx+1]

# leetcode submit region end(Prohibit modification and deletion)
