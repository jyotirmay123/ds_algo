class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        return x >= 0 and x_str == x_str[::-1]