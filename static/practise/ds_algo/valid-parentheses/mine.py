
# In Progress
class Solution:
    def isValid(self, s: str) -> bool:
        b1 = 0
        b2 = 0
        b3 = 0
        for i, si in enumerate(s):

            # b1 = si
            # last = isValid(s[i:])
            if si == '(':
                b1 += 1
            elif si == '{':
                b2 += 1
            elif si == '[':
                b3 += 1
            elif si == ')':
                b1 -= 1
            elif si == '}':
                b2 -= 1
            elif si == ']':
                b3 -= 1
            else:
                pass

        print(b1, b2, b3)
        if (b1 != 0) or (b2 != 0) or (b3 != 0):
            return False
        else:
            return True