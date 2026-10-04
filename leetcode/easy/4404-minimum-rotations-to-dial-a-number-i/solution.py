class Solution:
    def minRotations(self, s: str) -> int:
        c=0
        r=0
        for char in s:
            t=int(char)
            d=abs(c-t)
            r+=min(d,10-d)
            c=t
        return r
        
        