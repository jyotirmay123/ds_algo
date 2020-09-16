
class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        a =  int('-' + x[-1:0:-1]) if x[0] == '-' else int(x[::-1])
        if a >= -2147483648 and a<= 2147483647: return a
        else: return 0