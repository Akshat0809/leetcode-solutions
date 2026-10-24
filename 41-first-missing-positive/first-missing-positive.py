class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        i = 0
        
        # Step 1: Local variable 'x' use karke redundant list lookups hataye
        while i < n:
            x = nums[i]
            if 1 <= x <= n and nums[x - 1] != x:
                nums[x - 1], nums[i] = x, nums[x - 1]
            else:
                i += 1
        
        # Step 2: enumerate(nums, 1) C-level par 1 se counting start karta hai
        for i, x in enumerate(nums, 1):
            if x != i:
                return i
                
        return n + 1