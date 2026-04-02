class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        h=[0]*10**6
        a=[]
        for i in nums:
            h[i]+=1
        for i in range(1,len(nums)+1):
            if h[i]==0:
                a.append(i)
        return a