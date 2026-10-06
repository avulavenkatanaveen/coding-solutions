# Arranging Coins

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You have `n` coins and you want to build a staircase with these coins. The staircase consists of `k` rows where the `ith` row has exactly `i` coins. The last row of the staircase  **may be**  incomplete.

Given the integer `n`, return  *the number of  **complete rows**  of the staircase you will build*.

 

 **Example 1:** 

```
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.

```

 **Example 2:** 

```
Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.

```

 

 **Constraints:** 

- 1 <= n <= 231 - 1

## Solution

**Language:** Python  
**Runtime:** 1 ms (beats 81.65%)  
**Memory:** 19.4 MB (beats 27.37%)  
**Submitted:** 2026-10-06T15:40:03.552Z  

```py
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((-1+((1+(n*8))**0.5))/2)
        
```

---

[View on LeetCode](https://leetcode.com/problems/arranging-coins/)