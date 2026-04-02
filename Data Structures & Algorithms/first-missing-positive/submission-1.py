class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        a={}
        for i in nums:
            if i>(-1):
                a[i]=a.get(i,0)+1
        for i in range(1,len(nums)+2):
            if i not in a:
                return i
            