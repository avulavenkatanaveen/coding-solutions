class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i,x in enumerate(nums):
            s=0
            while x>0:
                x,r=divmod(x,10)
                s+=r
            if s==i:
                return i
        return -1

        