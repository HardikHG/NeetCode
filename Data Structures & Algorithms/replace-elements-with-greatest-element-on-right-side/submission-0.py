class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        '''l=arr[0]
        for i in range(len(arr)):
            if arr[i]>l:
                l=arr[i]
            if arr[i-1]<
                arr[i-1]=l
        return arr'''            
        n = len(arr)
        ans = [0] * n
        for i in range(n):
            rightMax = -1
            for j in range(i + 1, n):
                rightMax = max(rightMax, arr[j])
            ans[i] = rightMax
        return ans