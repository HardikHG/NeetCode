class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        i,j=0,len(nums)-1
        num=sorted(nums)
        nu=sorted(nums)[::-1]
        while i<=j:
            if nums==num:
                if nums[i]<=nums[j]:
                    i+=1
                    j-=1
            else:
                if nu!=nums:
                    return False
                if nums[i]>=nums[j]:
                    i+=1
                    j-=1
                else:
                    return False
        return True