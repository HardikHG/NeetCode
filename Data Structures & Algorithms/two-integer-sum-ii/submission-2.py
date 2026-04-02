class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=(len(numbers)-1)
        while l<r:
            c_sum=numbers[l]+numbers[r]
            if c_sum==target:
                return [l+1,r+1]
            else:
                if c_sum<target:
                    l+=1
                else:
                    r-=1
        return []