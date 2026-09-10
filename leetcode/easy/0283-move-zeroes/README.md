# Move Zeroes

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

 **Note**  that you must do this in-place without making a copy of the array.

 

 **Example 1:** 

```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

```

 **Example 2:** 

```
Input: nums = [0]
Output: [0]

```

 

 **Constraints:** 

- 1 <= nums.length <= 104
- -231 <= nums[i] <= 231 - 1

 

 **Follow up:**  Could you minimize the total number of operations done?

## Solution

**Language:** Python  
**Runtime:** 5 ms (beats 48.96%)  
**Memory:** 20.4 MB (beats 62.52%)  
**Submitted:** 2026-09-10T08:29:38.357Z  

```py
class Solution:
    def moveZeroes(self, nums):
        l = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[l], nums[i] = nums[i], nums[l]
                l+= 1
        return l
```

---

[View on LeetCode](https://leetcode.com/problems/move-zeroes/)