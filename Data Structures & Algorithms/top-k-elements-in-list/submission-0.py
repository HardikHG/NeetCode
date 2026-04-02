class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h=Counter(nums)
        freqq=[]
        for num,freq in h.items():
            freqq.append([freq,num])
        freqq.sort()

        ans=[]
        for i in range(k):
            ans.append(freqq.pop()[1])
        
        return ans