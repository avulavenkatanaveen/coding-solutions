class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        s=[num*num for num in nums]
        s.sort()
        return s
            

        