class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        s=sorted(nums)
        a=s[1]*s[0]
        b=s[-1]*s[-2]
        return b-a