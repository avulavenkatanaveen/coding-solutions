# Convert Sorted Array to Binary Search Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer array `nums` where the elements are sorted in  **ascending order**, convert  *it to a   height-balanced binary search tree*.

 

 **Example 1:** 

```
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

```

 **Example 2:** 

```
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

```

 

 **Constraints:** 

- 1 <= nums.length <= 104
- -104 <= nums[i] <= 104
- nums is sorted in a strictly increasing order.

## Solution

**Language:** C++  
**Runtime:** 5 ms (beats 15.79%)  
**Memory:** 22.9 MB (beats 56.08%)  
**Submitted:** 2026-08-31T09:01:20.691Z  

```cpp
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        if (nums.empty()) return nullptr;
        return createBST(nums, 0, static_cast<int>(nums.size()) - 1);
    }

    TreeNode* createBST(vector<int>& nums, int low, int high) {
        if (low>high) return nullptr;

        int mid=(low+high)/2;
        TreeNode*root=new TreeNode(nums[mid]);

        root->left=createBST(nums,low,mid-1);
        root->right=createBST(nums,mid+1,high);

        return root;
    }
};
```

---

[View on LeetCode](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)