class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        # C-level hashing: poora list ek jhatke mein C-memory set mein convert hota hai
        num_set = set(nums)
        
        # range() iterator C mein increment karta hai (while loop ke 'i += 1' se fast)
        for i in range(1, len(nums) + 2):
            if i not in num_set:
                return i