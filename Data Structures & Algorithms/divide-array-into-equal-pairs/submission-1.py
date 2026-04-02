class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        h={}
        for num in nums:
            if num not in h:
                h[num]=0
            h[num]+=1
        
        for cnt in h.values():
            if cnt%2!=0:
                return False
        return True