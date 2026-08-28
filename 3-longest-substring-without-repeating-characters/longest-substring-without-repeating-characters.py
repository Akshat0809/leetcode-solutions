class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # Character aur uska last seen index store karne ke liye
        left = 0       # Window ka starting pointer
        max_length = 0 # Longest substring ki length store karne ke liye
        
        for right in range(len(s)):
            current_char = s[right]
            
            # Agar character pehle dekha gaya hai aur wo current window ke andar hai
            if current_char in char_map and char_map[current_char] >= left:
                # Left pointer ko duplicate character ke just aage shift kar do
                left = char_map[current_char] + 1
            
            # Character ka current index update karo
            char_map[current_char] = right
            
            # Maximum length update karo
            max_length = max(max_length, right - left + 1)
            
        return max_length