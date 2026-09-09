# Sort Array By Parity II

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an array of integers `nums`, half of the integers in `nums` are  **odd**, and the other half are  **even**.

Sort the array so that whenever `nums[i]` is odd, `i` is  **odd**, and whenever `nums[i]` is even, `i` is  **even**.

Return  *any answer array that satisfies this condition*.

 

 **Example 1:** 

```
Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

```

 **Example 2:** 

```
Input: nums = [2,3]
Output: [2,3]

```

 

 **Constraints:** 

- 2 <= nums.length <= 2 * 104
- nums.length is even.
- Half of the integers in nums are even.
- 0 <= nums[i] <= 1000

 

 **Follow Up:**  Could you solve it in-place?

## Solution

**Language:** Python  
**Runtime:** 9 ms (beats 41.03%)  
**Memory:** 20.8 MB (beats 55.26%)  
**Submitted:** 2026-09-09T05:02:08.902Z  

```py
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i=0
        j=1
        n=len(nums)
        while i<n and j<n:
            if nums[i]%2==1 and nums[j]%2==0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=2
                j+=2
            elif nums[i]%2==0:
                i+=2
            else:
                j+=2
        return nums

        
```

---

[View on LeetCode](https://leetcode.com/problems/sort-array-by-parity-ii/)