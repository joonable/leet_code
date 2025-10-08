def solution(nums):
    n = len(nums) // 2
    nums = set(nums)
    return min(len(nums), n)