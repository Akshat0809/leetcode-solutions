
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)

        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        for x in nums:
            x = abs(x)
            if x <= n:
                nums[x - 1] = -abs(nums[x - 1])

        for i, x in enumerate(nums):
            if x > 0:
                return i + 1

        return n + 1
