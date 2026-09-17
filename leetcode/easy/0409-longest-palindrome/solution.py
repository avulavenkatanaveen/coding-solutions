class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd_chars=set()
        length=0
        for char in s:
            if char in odd_chars:
                odd_chars.remove(char)
                length += 2
            else:
                odd_chars.add(char)
        return length+(1 if odd_chars else 0)
        