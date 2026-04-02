class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            l_sum=0
            r_sum=0
            for j in range(i):
                l_sum+=nums[j]
            for k in range(i+1,len(nums)):
                r_sum+=nums[k]
            if l_sum==r_sum:
                return i
        return -1