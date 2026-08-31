class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        for x in nums1:
            for y in nums2:
                if x==y:
                    return x
                elif y>x:
                    break
        return -1

        