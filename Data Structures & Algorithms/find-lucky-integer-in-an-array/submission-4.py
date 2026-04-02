class Solution:
    def findLucky(self, arr: List[int]) -> int:
        h=[0]*500
        for i in arr:
            h[i]+=1
        for i in range(len(arr)):
            if h[arr[i]]>=1:
                if h[arr[i]]==arr[i]:
                    return max(h)
        return -1