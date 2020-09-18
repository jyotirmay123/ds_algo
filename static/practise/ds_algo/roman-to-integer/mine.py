
class Solution:
    def romanToInt(self, s: str) -> int:
        priority = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        num = 0
        for idx, si in enumerate(s):
            if idx == 0:
                num += priority[si]
                continue

            temp_num = priority[si]
            prev_num = priority[s[idx - 1]]
            if temp_num <= prev_num:
                num += priority[si]
            else:
                num += priority[si] - (2 * prev_num)

        return num

