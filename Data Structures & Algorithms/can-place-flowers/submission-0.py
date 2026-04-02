class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        fl=[0]+flowerbed+[0]
        for i in range(1,len(fl)-1):
            if fl[i-1]==0 and fl[i]==0 and fl[i+1]==0:
                fl[i]=1
                n-=1
        return n<=0