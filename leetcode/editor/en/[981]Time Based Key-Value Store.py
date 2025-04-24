# Design a time-based key-value data structure that can store multiple values 
# for the same key at different time stamps and retrieve the key's value at a 
# certain timestamp. 
# 
#  Implement the TimeMap class: 
# 
#  
#  TimeMap() Initializes the object of the data structure. 
#  void set(String key, String value, int timestamp) Stores the key key with 
# the value value at the given time timestamp. 
#  String get(String key, int timestamp) Returns a value such that set was 
# called previously, with timestamp_prev <= timestamp. If there are multiple such 
# values, it returns the value associated with the largest timestamp_prev. If there 
# are no values, it returns "". 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4]
# , ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]
# 
# Explanation
# TimeMap timeMap = new TimeMap();
# timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along 
# with timestamp = 1.
# timeMap.get("foo", 1);         // return "bar"
# timeMap.get("foo", 3);         // return "bar", since there is no value 
# corresponding to foo at timestamp 3 and timestamp 2, then the only value is at 
# timestamp 1 is "bar".
# timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along 
# with timestamp = 4.
# timeMap.get("foo", 4);         // return "bar2"
# timeMap.get("foo", 5);         // return "bar2"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= key.length, value.length <= 100 
#  key and value consist of lowercase English letters and digits. 
#  1 <= timestamp <= 10⁷ 
#  All the timestamps timestamp of set are strictly increasing. 
#  At most 2 * 10⁵ calls will be made to set and get. 
#  
# 
#  Related Topics Hash Table String Binary Search Design 👍 4987 👎 669


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
from bisect import bisect_right
"""
For each key, I store a sorted list of (timestamp, value) pairs. All the timestamps of set are strictly increasing.
When calling get, I use binary search to find the closest timestamp which is less than or equal to the target.
"""
class TimeMap:

    def __init__(self):
        self.key_to_time_values = defaultdict(list) # important

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_to_time_values[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_to_time_values:
            return ""
        time_value_pairs = self.key_to_time_values[key]
        # bisect_right: return the rightmost index just after the target timestamp.
        index = bisect_right(time_value_pairs, (timestamp, chr(127)))   # important
        return time_value_pairs[index - 1][1] if index != 0 else ''   # important


class TicTacToe:
    def __init__(self, n):
        self.board_size = n
        self.rows = [0] * self.board_size
        self.cols = [0] * self.board_size
        self.diagonal = 0
        self.anti_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        move_val = -1 if player == 1 else 1
        self.rows[row] += move_val
        self.cols[col] += move_val
        if row == col:
            self.diagonal += move_val
        if row + col == self.board_size - 1:
            self.anti_diagonal += move_val

        if abs(self.rows[row]) == self.board_size\
            or abs(self.cols[col]) == self.board_size \
            or abs(self.diagonal) == self.board_size \
            or abs(self.anti_diagonal) == self.board_size:
            return player
        return 0

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# leetcode submit region end(Prohibit modification and deletion)
