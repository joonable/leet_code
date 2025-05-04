# A company is planning to interview 2n people. Given the array costs where 
# costs[i] = [aCosti, bCosti], the cost of flying the iᵗʰ person to city a is aCosti, 
# and the cost of flying the iᵗʰ person to city b is bCosti. 
# 
#  Return the minimum cost to fly every person to a city such that exactly n 
# people arrive in each city. 
# 
#  
#  Example 1: 
# 
#  
# Input: costs = [[10,20],[30,200],[400,50],[30,20]]
# Output: 110
# Explanation: 
# The first person goes to city A for a cost of 10.
# The second person goes to city A for a cost of 30.
# The third person goes to city B for a cost of 50.
# The fourth person goes to city B for a cost of 20.
# 
# The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people 
# interviewing in each city.
#  
# 
#  Example 2: 
# 
#  
# Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
# Output: 1859
#  
# 
#  Example 3: 
# 
#  
# Input: costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[65
# 0,359],[631,42]]
# Output: 3086
#  
# 
#  
#  Constraints: 
# 
#  
#  2 * n == costs.length 
#  2 <= costs.length <= 100 
#  costs.length is even. 
#  1 <= aCosti, bCosti <= 1000 
#  
# 
#  Related Topics Array Greedy Sorting 👍 4799 👎 359


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Problem
        # input: costs: List[List[int]] -> [aCost, bCost] -> cost to a and b respectively
        # output: min_cost
        # such that len(costs) == 2n, n -> a + n -> b

        # Approach Greedy (sorting costs by diff(cost_a - cost_b))
        # first half -> a, last half -> b
        # [[259,770],[184,139],[577,469],[926,667],[448,54],[840,118]]
        # [259 + 184 + 577 + 667 + 54 + 118]
        # [443 + 1244 + 172] = 1859

        half = len(costs) // 2
        costs.sort(key=lambda x: x[0] - x[1])  # sort by diff

        total_cost = 0
        for i, (a, b) in enumerate(costs):
            cost = a if i < half else b
            total_cost += cost
        return total_cost


# class Solution:
#     def twoCitySchedCost(self, costs: List[List[int]]) -> int:
#         costs.sort(key=lambda x: x[0] - x[1])
#
#         half = len(costs) // 2
#         result = 0
#
#         for i, (a, b) in enumerate(costs):
#             result += a if i < half else b
#
#         return result
        
# leetcode submit region end(Prohibit modification and deletion)
