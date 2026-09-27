class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans=[]
        while nums:
            dist=sorted(list(set(nums)))
            for val in dist:
                ans.append(val)
                nums.remove(val)
        return ans
        