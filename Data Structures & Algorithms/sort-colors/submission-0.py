class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a,l,r=0,0,len(nums)-1
        while l<=r:
            if nums[l]==0:
                nums[a],nums[l]=nums[l],nums[a]
                a+=1
                l+=1
            elif nums[l]==1:
                l+=1
            else:
                nums[l],nums[r]=nums[r],nums[l]
                r-=1
        return nums
        