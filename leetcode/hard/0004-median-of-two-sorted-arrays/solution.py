class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list=nums1+nums2
        merged_list.sort()
        n=len(merged_list)
        if n%2==1:
            median=merged_list[n//2]
        else:
            median=(merged_list[n//2-1]+merged_list[n//2])/2
        return median

        