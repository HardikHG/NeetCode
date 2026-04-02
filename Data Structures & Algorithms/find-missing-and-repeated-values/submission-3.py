
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        a=[]
        h=[0]*(len(grid)*len(grid)+1)
        ans=[]
        for n in grid:
            a=a+n
        for i in a:
            h[i]+=1
            if h[i]>1:
                ans.append(i)
        for i in range(1,len(a)+1):
            if h[i]==0:
                ans.append(i)
        return ans