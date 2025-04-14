# Design a stack that supports push, pop, top, and retrieving the minimum 
# element in constant time. 
# 
#  Implement the MinStack class: 
# 
#  
#  MinStack() initializes the stack object. 
#  void push(int val) pushes the element val onto the stack. 
#  void pop() removes the element on the top of the stack. 
#  int top() gets the top element of the stack. 
#  int getMin() retrieves the minimum element in the stack. 
#  
# 
#  You must implement a solution with O(1) time complexity for each function. 
# 
#  
#  Example 1: 
# 
#  
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# 
# Output
# [null,null,null,null,-3,null,0,-2]
# 
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
#  
# 
#  
#  Constraints: 
# 
#  
#  -2³¹ <= val <= 2³¹ - 1 
#  Methods pop, top and getMin operations will always be called on non-empty 
# stacks. 
#  At most 3 * 10⁴ calls will be made to push, pop, top, and getMin. 
#  
# 
#  Related Topics Stack Design 👍 14713 👎 920


# leetcode submit region begin(Prohibit modification and deletion)
# TODO
from collections import deque
class MinStack:
    def __init__(self):
        self._stack = []
        self._min_stack = [float("inf")]    # important

    def push(self, val: int) -> None:
        self._stack.append(val)
        self._min_stack.append(min(val, self._min_stack[-1]))   # important

    def pop(self) -> None:
        self._stack.pop()
        self._min_stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min_stack[-1]  # important


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# leetcode submit region end(Prohibit modification and deletion)
