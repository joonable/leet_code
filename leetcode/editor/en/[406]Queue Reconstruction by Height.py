# You are given an array of people, people, which are the attributes of some 
# people in a queue (not necessarily in order). Each people[i] = [hi, ki] represents 
# the iᵗʰ person of height hi with exactly ki other people in front who have a 
# height greater than or equal to hi. 
# 
#  Reconstruct and return the queue that is represented by the input array 
# people. The returned queue should be formatted as an array queue, where queue[j] = [
# hj, kj] is the attributes of the jᵗʰ person in the queue (queue[0] is the person 
# at the front of the queue). 
# 
#  
#  Example 1: 
# 
#  
# Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
# Explanation:
# Person 0 has height 5 with no other people taller or the same height in front.
# 
# Person 1 has height 7 with no other people taller or the same height in front.
# 
# Person 2 has height 5 with two persons taller or the same height in front, 
# which is person 0 and 1.
# Person 3 has height 6 with one person taller or the same height in front, 
# which is person 1.
# Person 4 has height 4 with four people taller or the same height in front, 
# which are people 0, 1, 2, and 3.
# Person 5 has height 7 with one person taller or the same height in front, 
# which is person 1.
# Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.
#  
# 
#  Example 2: 
# 
#  
# Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
# Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= people.length <= 2000 
#  0 <= hi <= 10⁶ 
#  0 <= ki < people.length 
#  It is guaranteed that the queue can be reconstructed. 
#  
# 
#  Related Topics Array Binary Indexed Tree Segment Tree Sorting 👍 7154 👎 736


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 키는 큰 순으로, k는 작은 순으로 정렬
        people.sort(key=lambda x: (-x[0], x[1]))

        result = []
        for person in people:
            result.insert(person[1], person)  # k 위치에 삽입
        return result
        
# leetcode submit region end(Prohibit modification and deletion)
