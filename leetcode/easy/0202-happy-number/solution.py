class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1 or n == 7:
            return True
        elif n < 10:
            return False

        next_sum = sum(int(digit) ** 2 for digit in str(n))
        return self.isHappy(next_sum)       