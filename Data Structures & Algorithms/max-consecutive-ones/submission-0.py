class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx=0
        for i in range (len(nums)):
            cnt=0
            for j in range(i,len(nums)):
                if nums[j]==0:
                    break
                cnt+=1
            maxx=max(maxx,cnt)
        return maxx