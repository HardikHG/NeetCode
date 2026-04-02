class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #OPTIMAL
        t_sum=sum(nums)
        l_sum=0
        for i,x in enumerate(nums):
            if l_sum==(t_sum-l_sum-x):
                return i
            l_sum+=x
        return -1
        
        #BRUTE FORCE
        '''for i in range(len(nums)):
            l_sum=0
            r_sum=0
            for j in range(i):
                l_sum+=nums[j]
            for k in range(i+1,len(nums)):
                r_sum+=nums[k]
            if l_sum==r_sum:
                return i
        return -1'''