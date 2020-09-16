class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        n = len(x)
        for i in range(n//2):
            if x[i] != x[-(i+1)]:
                return False
        return True