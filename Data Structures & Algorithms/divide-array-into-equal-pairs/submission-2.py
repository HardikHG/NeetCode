class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        h={}
        if len(nums)%2!=0:
            return False
        for num in nums:
            h[num]=h.get(num,0)+1
        
        for cnt in h.values():
            if cnt%2!=0:
                return False
        return True