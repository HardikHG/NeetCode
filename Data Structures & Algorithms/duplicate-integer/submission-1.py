class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        c=0
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                c+=1
            if c>=1:
                return True
        return False