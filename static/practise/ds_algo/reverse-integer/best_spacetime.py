
class Solution:
    def reverse(self, x: int) -> int:

        reversed = 0
        if x == 0:
            return 0

        num = x
        x = abs(x)
        while x != 0:
            reversed = (reversed * 10) + (x % 10)
            x //= 10
        if (reversed > ((2 ** 31) - 1) or reversed < -1 * (2 ** 31)):
            return 0

        if num < 0:
            return -reversed
        else:
            return reversed