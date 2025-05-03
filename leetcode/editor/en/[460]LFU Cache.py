# Design and implement a data structure for a Least Frequently Used (LFU) cache.
#  
# 
#  Implement the LFUCache class: 
# 
#  
#  LFUCache(int capacity) Initializes the object with the capacity of the data 
# structure. 
#  int get(int key) Gets the value of the key if the key exists in the cache. 
# Otherwise, returns -1. 
#  void put(int key, int value) Update the value of the key if present, or 
# inserts the key if not already present. When the cache reaches its capacity, it 
# should invalidate and remove the least frequently used key before inserting a new 
# item. For this problem, when there is a tie (i.e., two or more keys with the same 
# frequency), the least recently used key would be invalidated. 
#  
# 
#  To determine the least frequently used key, a use counter is maintained for 
# each key in the cache. The key with the smallest use counter is the least 
# frequently used key. 
# 
#  When a key is first inserted into the cache, its use counter is set to 1 (
# due to the put operation). The use counter for a key in the cache is incremented 
# either a get or put operation is called on it. 
# 
#  The functions get and put must each run in O(1) average time complexity. 
# 
#  
#  Example 1: 
# 
#  
# Input
# ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", 
# "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
# 
# Explanation
# // cnt(x) = the use counter for key x
# // cache=[] will show the last used order for tiebreakers (leftmost element 
# is  most recent)
# LFUCache lfu = new LFUCache(2);
# lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
# lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
# lfu.get(1);      // return 1
#                  // cache=[1,2], cnt(2)=1, cnt(1)=2
# lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, 
# invalidate 2.
#                  // cache=[3,1], cnt(3)=1, cnt(1)=2
# lfu.get(2);      // return -1 (not found)
# lfu.get(3);      // return 3
#                  // cache=[3,1], cnt(3)=2, cnt(1)=2
# lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1
# .
#                  // cache=[4,3], cnt(4)=1, cnt(3)=2
# lfu.get(1);      // return -1 (not found)
# lfu.get(3);      // return 3
#                  // cache=[3,4], cnt(4)=1, cnt(3)=3
# lfu.get(4);      // return 4
#                  // cache=[4,3], cnt(4)=2, cnt(3)=3
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= capacity <= 10⁴ 
#  0 <= key <= 10⁵ 
#  0 <= value <= 10⁹ 
#  At most 2 * 10⁵ calls will be made to get and put. 
#  
# 
#  
#  
# 
#  Related Topics Hash Table Linked List Design Doubly-Linked List 👍 5956 👎 33
# 8


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_val_freq = {}   # key → [value, frequency]
        self.freq_to_keys = defaultdict(OrderedDict) # frequency → OrderedDict of keys (for LRU within same freq)
        self.min_freq = 0  # 현재 캐시에 존재하는 최소 frequency

    def _update_freq(self, key):
        freq = self.key_to_val_freq[key][1]  # 현재 frequency
        del self.freq_to_keys[freq][key]     # 이전 freq 그룹에서 제거

        # freq 그룹이 비었으면 제거하고, min_freq 갱신
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        # freq + 1 그룹에 추가
        self.key_to_val_freq[key][1] += 1
        self.freq_to_keys[freq + 1][key] = None  # OrderedDict에 삽입 (맨 뒤로 → 최신)

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1
        self._update_freq(key)  # 사용했으니 freq 증가
        return self.key_to_val_freq[key][0]  # value 반환

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_val_freq:
            self.key_to_val_freq[key][0] = value  # value 갱신
            self._update_freq(key)  # freq 업데이트
        else:
            # 캐시가 꽉 찼으면 LFU + LRU 기준으로 제거
            if len(self.key_to_val_freq) >= self.capacity:
                key_rmv, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
                del self.key_to_val_freq[key_rmv]

            # 새 key 추가: value=..., freq=1
            self.key_to_val_freq[key] = [value, 1]
            self.freq_to_keys[1][key] = None
            self.min_freq = 1  # 새로운 key는 freq 1 → 최소 freq 리셋

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)
