# Contains Duplicate II

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer array `nums` and an integer `k`, return `true`  *if there are two  **distinct indices*** `i` *and* `j` *in the array such that* `nums[i] == nums[j]` *and* `abs(i - j) <= k`.

 

 **Example 1:** 

```
Input: nums = [1,2,3,1], k = 3
Output: true

```

 **Example 2:** 

```
Input: nums = [1,0,1,1], k = 1
Output: true

```

 **Example 3:** 

```
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

```

 

 **Constraints:** 

- 1 <= nums.length <= 105
- -109 <= nums[i] <= 109
- 0 <= k <= 105

## Solution

**Language:** Python  
**Runtime:** 51 ms (beats 48.73%)  
**Memory:** 39.3 MB (beats 51.77%)  
**Submitted:** 2026-10-03T06:14:14.405Z  

```py
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        hset={}
        for i in range(len(nums)):
            if nums[i] in hset and abs(i-hset[nums[i]])<=k:
                return True
            hset[nums[i]]=i
        return False
        
        
        

        
        
```

---

[View on LeetCode](https://leetcode.com/problems/contains-duplicate-ii/)