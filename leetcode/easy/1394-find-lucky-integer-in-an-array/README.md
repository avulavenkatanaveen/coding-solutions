# Find Lucky Integer in an Array

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an array of integers `arr`, a  **lucky integer**  is an integer that has a frequency in the array equal to its value.

Return  *the largest  **lucky integer**  in the array*. If there is no  **lucky integer**  return `-1`.

 

 **Example 1:** 

```
Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.

```

 **Example 2:** 

```
Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

```

 **Example 3:** 

```
Input: arr = [2,2,2,3,3]
Output: -1
Explanation: There are no lucky numbers in the array.

```

 

 **Constraints:** 

- 1 <= arr.length <= 500
- 1 <= arr[i] <= 500

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.3 MB (beats 67.42%)  
**Submitted:** 2026-08-17T04:35:32.016Z  

```py
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dict={}
        for i in arr:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        lucky_num=-1
        for i,freq in dict.items():
            if i==freq:
                if i>lucky_num:
                    lucky_num=i
        return lucky_num
        
```

---

[View on LeetCode](https://leetcode.com/problems/find-lucky-integer-in-an-array/)