
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        base = strs[0]
        for toMatch in strs[1:]:
            base = self.lcp(base, toMatch)

        return base

    def lcp(self, w1, w2):
        lcp = ''
        for l1, l2 in zip(w1, w2):
            if l1 == l2:
                lcp += l1
            else:
                break
        return lcp