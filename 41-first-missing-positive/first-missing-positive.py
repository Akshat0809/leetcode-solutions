
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        i = 0

        while i < n:
            x = nums[i]
            if 1 <= x <= n and nums[x - 1] != x:
                nums[i], nums[x - 1] = nums[x - 1], x
            else:
                i += 1

        for i, x in enumerate(nums):
            if x != i + 1:
                return i + 1

        return n + 1
