# Find K Closest Elements

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a  **sorted**  integer array `arr`, two integers `k` and `x`, return the `k` closest integers to `x` in the array. The result should also be sorted in ascending order.

An integer `a` is closer to `x` than an integer `b` if:

- |a - x| < |b - x|, or
- |a - x| == |b - x| and a < b

 

 **Example 1:** 

 **Input:**  arr = [1,2,3,4,5], k = 4, x = 3

 **Output:**  [1,2,3,4]

 **Example 2:** 

 **Input:**  arr = [1,1,2,3,4,5], k = 4, x = -1

 **Output:**  [1,1,2,3]

 

 **Constraints:** 

- 1 <= k <= arr.length
- 1 <= arr.length <= 104
- arr is sorted in ascending order.
- -104 <= arr[i], x <= 104

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 20.6 MB (beats 85.25%)  
**Submitted:** 2026-09-07T08:37:29.434Z  

```py
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low=0
        high=len(arr)-k
        while low<high:
            mid=(high+low)//2
            if x-arr[mid]>arr[mid+k]-x:
                low=mid+1
            else:
                high=mid
        return arr[low:low+k]
        
```

---

[View on LeetCode](https://leetcode.com/problems/find-k-closest-elements/)