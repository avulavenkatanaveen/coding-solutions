class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n=len(s)
        c=0
        for i in range(n):
            t=s[i:]+s[:i]
            score=0
            for j in range(n-1):
                if t[j]==t[j+1]:
                    score+=1
            if score==k:
                c+=1
        return c
            
            
        