# Most Common Word

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string `paragraph` and a string array of the banned words `banned`, return  *the most frequent word that is not banned*. It is  **guaranteed**  there is  **at least one word**  that is not banned, and that the answer is  **unique**.

The words in `paragraph` are  **case-insensitive**  and the answer should be returned in  **lowercase**.

 **Note**  that words can not contain punctuation symbols.

 

 **Example 1:** 

```
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.

```

 **Example 2:** 

```
Input: paragraph = "a.", banned = []
Output: "a"

```

 

 **Constraints:** 

- 1 <= paragraph.length <= 1000
- paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
- 0 <= banned.length <= 100
- 1 <= banned[i].length <= 10
- banned[i] consists of only lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 13 ms (beats 7.75%)  
**Memory:** 19.4 MB (beats 24.11%)  
**Submitted:** 2026-10-10T15:50:27.900Z  

```py
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        l = []
        w = ""
        for i in paragraph:
            if i.isalpha():
                w += i.lower()
            else:
                if w != "":
                    l.append(w)
                    w = ""
        if w != "":
            l.append(w)
            
        max_count = 0
        res = ""
        for word in l:
            if word in banned:
                continue
                
            c = 0
            for item in l:
                if item == word:
                    c += 1
                    
            if c > max_count:
                max_count = c
                res = word
                
        return res
```

---

[View on LeetCode](https://leetcode.com/problems/most-common-word/)