class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        a=0
        h=sorted(heights)
        if heights==h:
            return a
        for i in range(len(h)):
            if heights[i]!=h[i]:
                a+=1
        return a