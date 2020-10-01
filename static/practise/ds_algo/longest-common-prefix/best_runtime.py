
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        l = min(len(x) for x in strs)
        lcp = strs[0][:l]

        for i in range(1, len(strs)):
            while l >= 0 and lcp != strs[i][:l]:
                l = l - 1
                lcp = strs[0][:l]

        return lcp