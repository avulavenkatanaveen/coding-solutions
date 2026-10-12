class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a=2  
        b=1
        current = 0
        for i in range(3, n + 1):
            current = a+b
            b=a
            a=current
            
        return current