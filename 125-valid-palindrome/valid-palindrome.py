class Solution:
    def isPalindrome(self, s: str) -> bool:
        if(len(s) == 0):
            return True
        cleaned_s = "".join(ch.lower() for ch in s if ch.isalnum())
        left = 0
        right = len(cleaned_s) - 1
        while(left<right):
            if(cleaned_s[left] == cleaned_s[right]):
                left += 1
                right -= 1
            else:
                return False
        return True
            