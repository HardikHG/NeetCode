class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count={}
        n=len(nums)//3
        for i in nums:
            count[i]=count.get(i,0)+1
        ans=[]
        for num,freq in count.items():
            if freq>n:
                ans.append(num)
        return ans