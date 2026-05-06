class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        # if len(s) != len(t):
        #     return False

        # for i in s:
        #     if i != t:
        #         return False
        #     else:
        #         return True
