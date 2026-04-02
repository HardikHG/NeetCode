class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=[]
        c=[0]*26
        if len(s)!=len(t):
            return False
        else:
            for i in s:
                c[ord(i)-ord('a')]+=1
            for i in t:
                c[ord(i)-ord('a')]-=1
            for i in c:
                if i!=0:
                    return False
            '''for i in range(len(s)):
                if s[i] not in a:
                    a.append(s[i])
            for i in range(len(t)):
                if t[i] not in a:
                    return False'''
            return True
