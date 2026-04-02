class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count=Counter(nums)
        ope=0
        for freq in count.values():
            if freq<2:
                return -1
            ope+=(freq+2)//3
            '''elif freq%3==0:
                ope+=(freq//3)
            elif freq%2==0:
                ope+=(freq//2)'''
            
        return ope