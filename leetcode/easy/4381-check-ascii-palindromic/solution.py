class Solution:
    def isPalindromic(self, s: str) -> bool:
        binary_str ="".join(f"{ord(char):08b}"for char in s)
        return binary_str == binary_str[::-1]