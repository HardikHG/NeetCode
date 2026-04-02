class Solution:
    def check(self, nums: List[int]) -> bool:
        num=sorted(nums)
        for i in range(len(num)):
            if num[len(num)-i:]+num[:len(num)-i]==nums:
                return True
        return False
        
