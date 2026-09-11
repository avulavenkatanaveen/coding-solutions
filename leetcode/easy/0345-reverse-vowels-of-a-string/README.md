# Reverse Vowels of a String

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string `s`, reverse only all the vowels in the string and return it.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in both lower and upper cases, more than once.

 

 **Example 1:** 

 **Input:**  s = "IceCreAm"

 **Output:**  "AceCreIm"

 **Explanation:** 

The vowels in `s` are `['I', 'e', 'e', 'A']`. On reversing the vowels, s becomes `"AceCreIm"`.

 **Example 2:** 

 **Input:**  s = "leetcode"

 **Output:**  "leotcede"

 

 **Constraints:** 

- 1 <= s.length <= 3 * 105
- s consist of printable ASCII characters.

## Solution

**Language:** Python  
**Runtime:** 10 ms (beats 54.64%)  
**Memory:** 20.5 MB (beats 52.14%)  
**Submitted:** 2026-09-11T14:38:06.764Z  

```py
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=set("aeiouAEIOU")
        char=list(s)
        left=0
        right=len(char)-1
        while left<right:
            while left<right and char[left] not in vowels:
                left+=1
            while left<right and char[right] not in vowels:
                right-=1

            char[left],char[right]=char[right],char[left]
            left+=1
            right-=1

        return "".join(char)
            

```

---

[View on LeetCode](https://leetcode.com/problems/reverse-vowels-of-a-string/)