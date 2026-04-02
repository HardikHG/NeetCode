class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans={}
        for i in strs:
            h=[0]*26
            for a in i:
                h[ord(a)-ord('a')]+=1
            if tuple(h) not in ans:
                ans[tuple(h)]=[]
            ans[tuple(h)].append(i)
        return list(ans.values())