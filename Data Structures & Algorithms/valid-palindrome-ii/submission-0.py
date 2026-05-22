class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                # Skip left character
                skip_left = s[left + 1:right + 1]

                # Skip right character
                skip_right = s[left:right]

                # If either becomes palindrome
                return (
                    skip_left == skip_left[::-1]
                    or skip_right == skip_right[::-1]
                )

            left += 1
            right -= 1

        return True