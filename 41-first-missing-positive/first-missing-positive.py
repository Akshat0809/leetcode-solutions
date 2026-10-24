class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        mod = n + 1
        
        # Step 1: Sabhi useless numbers (<= 0 ya > n) ko 0 bana do
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 0
                
        # Step 2: Har valid number x ke liye, index (x - 1) par 'mod' add kar do
        # '% mod' se humein hamesha original number milta rahega!
        for i in range(n):
            val = nums[i] % mod
            if val > 0:
                nums[val - 1] += mod
                
        # Step 3: Jis index par value 'mod' se choti reh gayi, wahi number missing hai
        for i in range(n):
            if nums[i] < mod:
                return i + 1
                
        return n + 1