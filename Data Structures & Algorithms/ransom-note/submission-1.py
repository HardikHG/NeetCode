class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        h=[0]*26
        for i in magazine:
            h[ord(i)-ord('a')]+=1
        for i in ransomNote:
            h[ord(i)-ord('a')]-=1
            if h[ord(i)-ord('a')]<0:
                return False
        return True