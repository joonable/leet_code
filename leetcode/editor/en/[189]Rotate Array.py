class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # list_nums = list(nums)
        i = k % len(nums)
        if len(nums) > 1 and i > 0:
            nums[:i], nums[i:] = nums[-i:], nums[:-i]
        # print(nums)

        # list_nums = list(nums)
        # nums = list(nums[-k:] + nums[:-k])
        # print(nums)
