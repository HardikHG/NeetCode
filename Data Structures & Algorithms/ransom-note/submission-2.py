class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        h=[0]*26
        for i in magazine:
            h[ord(i)-97]+=1
        for i in ransomNote:
            h[ord(i)-97]-=1
            if h[ord(i)-97]<0:
                return False
        return True