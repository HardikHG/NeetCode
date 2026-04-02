class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d={}
        used_t=set()
        for st,ts in zip(s,t):
            if st in d:
                if d[st]!=ts:
                    return False
            else:
                if ts in used_t:
                    return False
                d[st]=ts
                used_t.add(ts)
        return True