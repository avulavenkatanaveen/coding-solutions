class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        n=len(intervals)
        c=0
        for i in range(n):
            for j in range(i+1,n):
                s1,e1=intervals[i]
                s2,e2=intervals[j]
                if max(s1,s2)<=min(e1,e2):
                    c+=1
        return c
        