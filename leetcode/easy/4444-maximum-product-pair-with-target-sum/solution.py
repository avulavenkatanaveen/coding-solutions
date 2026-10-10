class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        m=float('-inf')
        pair=[-1,-1]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and nums[i]+nums[j]==target and nums[i]>nums[j]:
                    c=nums[i]*nums[j]
                    if c>m:
                        m=c
                        pair=[i,j]
        return pair
        
                    
                    
        
        