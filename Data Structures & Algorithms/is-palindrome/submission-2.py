class Solution:
    def isPalindrome(self, s: str) -> bool:
        # SLICING METHOD
        filtered_chars = [char.lower() for char in s if char.isalnum()]

        if filtered_chars == filtered_chars[::-1]:
            return True
        
        return False
       