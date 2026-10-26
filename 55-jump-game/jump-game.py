class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0
        n = len(nums)
        
        for i in range(n):
            # Agar hum current index tak pahunch hi nahi sakte
            if i > max_reach:
                return False
            
            # Furthest point reach karne ki capacity update karein
            max_reach = max(max_reach, i + nums[i])
            
            # Agar last index reach ho gaya ya cross ho gaya
            if max_reach >= n - 1:
                return True
                
        return True