class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        i=0
        j=0
        s=0
        ans=float('inf')
        for j in range(len(nums)):
            s=s+nums[j]
            while s>=target:
                s=s-nums[i]
                ans=min(ans,j-i+1)
                i+=1
        if ans==float('inf'):
            return 0
        else:
            return ans

                  
        
        

        