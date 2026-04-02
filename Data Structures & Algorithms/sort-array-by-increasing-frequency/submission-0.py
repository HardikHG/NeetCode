class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        ans=[]
        s_count = sorted(count.items(), key=lambda item: (item[1], -item[0]))
        
        for i,x in s_count:
            ans.extend([i]*x)
        return ans
        '''count = Counter(nums)
        # Sort nums directly: frequency (count[x]) asc, then value (-x) desc
        nums.sort(key=lambda x: (count[x], -x))
        return nums'''