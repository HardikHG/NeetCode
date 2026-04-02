class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        for i,x in enumerate(numbers):
            if (y:=target-x) in d:
                return [d[y]+1,i+1]
            d[x]=i