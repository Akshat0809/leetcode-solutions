class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Step 1: Har valid number x (1 <= x <= n) ko uske correct index (x - 1) par bhejo
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        
        # Step 2: Pehla index dhoondo jahan uska sahi number (i + 1) nahi baitha hai
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # Step 3: Agar 1 se n tak saare numbers sahi jagah hain, toh answer n + 1 hoga
        return n + 1