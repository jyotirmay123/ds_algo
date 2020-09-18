
class Solution:
    def romanToInt(self, s: str) -> int:
        dictt={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        prev=0
        ans=0
        for i in range(len(s)-1,-1,-1):
            if prev<=dictt[s[i]]:
                prev=dictt[s[i]]
                ans+=prev
            else:
                prev-=dictt[s[i]]
                ans-=dictt[s[i]]
        #print(ans)
        return ans