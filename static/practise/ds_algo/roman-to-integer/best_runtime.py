
class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        prev = 0
        current = 0
        total = 0
        for i in range(len(s)):
            current = table[s[i]]
            if current > prev:
                total = total + current - 2 * prev
            else:
                total = total + current
            prev = current
        return total