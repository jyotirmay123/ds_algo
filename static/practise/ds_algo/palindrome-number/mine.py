
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_arr = []
        x_orig = x
        while (x > 0):
            x_arr.append(x % 10)
            x = x // 10

        x_len = len(x_arr)
        p_num = 0
        for idx, x_r in enumerate(x_arr):
            p_num += x_r * 10 ** (x_len - idx - 1)

        return True if x_orig == p_num else False