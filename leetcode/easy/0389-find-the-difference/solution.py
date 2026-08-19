class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t1=list(t)
        for i in range(len(s)):
            if s[i] in t:
                t1.remove(s[i])
        k=("".join(map(str,t1)))
        return k



       




        