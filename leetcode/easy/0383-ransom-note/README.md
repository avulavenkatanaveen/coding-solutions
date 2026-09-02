# Ransom Note

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two strings `ransomNote` and `magazine`, return `true` *if* `ransomNote` *can be constructed by using the letters from* `magazine` *and* `false` *otherwise*.

Each letter in `magazine` can only be used once in `ransomNote`.

 

 **Example 1:** 

```
Input: ransomNote = "a", magazine = "b"
Output: false

```

 **Example 2:** 

```
Input: ransomNote = "aa", magazine = "ab"
Output: false

```

 **Example 3:** 

```
Input: ransomNote = "aa", magazine = "aab"
Output: true

```

 

 **Constraints:** 

- 1 <= ransomNote.length, magazine.length <= 105
- ransomNote and magazine consist of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 31 ms (beats 12.08%)  
**Memory:** 19.5 MB (beats 94.12%)  
**Submitted:** 2026-09-02T06:30:50.750Z  

```py
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq={}
        for i in magazine:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for i in ransomNote:
            if i in freq and freq[i]>0:
                freq[i]-=1
            else:
                return False
        return True

        
```

---

[View on LeetCode](https://leetcode.com/problems/ransom-note/)