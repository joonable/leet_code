# There are n children standing in a line. Each child is assigned a rating 
# value given in the integer array ratings. 
# 
#  You are giving candies to these children subjected to the following 
# requirements: 
# 
#  
#  Each child must have at least one candy. 
#  Children with a higher rating get more candies than their neighbors. 
#  
# 
#  Return the minimum number of candies you need to have to distribute the 
# candies to the children. 
# 
#  
#  Example 1: 
# 
#  
# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 
# 2 candies respectively.
#  
# 
#  Example 2: 
# 
#  
# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 
# 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two conditions.
#  
# 
#  
#  Constraints: 
# 
#  
#  n == ratings.length 
#  1 <= n <= 2 * 10⁴ 
#  0 <= ratings[i] <= 2 * 10⁴ 
#  
# 
#  Related Topics Array Greedy 👍 8418 👎 747


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        result = [1] * n
        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                result[i] = result[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                result[i] = max(result[i], result[i + 1] + 1)

        return sum(result)
        
# leetcode submit region end(Prohibit modification and deletion)
