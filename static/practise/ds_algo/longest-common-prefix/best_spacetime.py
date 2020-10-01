
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        arranged = list(zip(*strs))
        for chars in arranged:
            print(chars)
            if chars.count(chars[0]) == len(chars):
                prefix = "".join([prefix, chars[0]])
            else:
                break

        return prefix