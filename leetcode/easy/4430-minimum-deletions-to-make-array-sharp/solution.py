class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        res=[]
        d=0
        for num in nums:
            if res and res[-1] == num:
                d+=1
            else:
                res.append(num)
        return d
            
        