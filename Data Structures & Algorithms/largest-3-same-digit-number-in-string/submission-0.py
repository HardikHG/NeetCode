class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9,-1,-1):
            g_str=str(i)*3
            if g_str in num:
                return g_str
        return ''
        
                