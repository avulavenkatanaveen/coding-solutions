class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans=[]
        prefix=[0]*len(nums)
        prefix[0]=nums[0]
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]+nums[i]
        total=prefix[-1]
        for i in range(len(nums)):
            ls=prefix[i]-nums[i]
            rs=total-prefix[i]
            ans.append(abs(ls-rs))
        return ans


        