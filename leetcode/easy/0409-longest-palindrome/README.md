# Longest Palindrome

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string `s` which consists of lowercase or uppercase letters, return the length of the  **longest palindrome**  that can be built with those letters.

Letters are  **case sensitive**, for example, `"Aa"` is not considered a palindrome.

 

 **Example 1:** 

```
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

```

 **Example 2:** 

```
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

```

 

 **Constraints:** 

- 1 <= s.length <= 2000
- s consists of lowercase and/or uppercase English letters only.

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 46.47%)  
**Memory:** 19.3 MB (beats 67.74%)  
**Submitted:** 2026-09-17T14:47:08.045Z  

```py
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
        
```

---

[View on LeetCode](https://leetcode.com/problems/longest-palindrome/)