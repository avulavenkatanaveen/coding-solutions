class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if nums[i]>nums[i+1]:
                return i
        