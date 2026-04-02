class Solution:
    def firstUniqChar(self, s: str) -> int:
        count=Counter(s)
        for i, x in count.items():
            if x==1:
                return s.index(i)
        return -1