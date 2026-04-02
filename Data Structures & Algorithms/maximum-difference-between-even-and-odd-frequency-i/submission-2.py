class Solution:
    def maxDifference(self, s: str) -> int:
        h=[0]*26
        a1,a2=0,len(s)
        for i in range(len(s)):
            h[ord(s[i])-ord('a')]+=1
        for i in range(len(h)):
            if h[i]>=1:
                if h[i]%2 !=0:
                    if a1<h[i]:
                        a1=h[i]
                else:
                    if h[i]<a2:
                        a2=h[i]
        return (a1-a2)