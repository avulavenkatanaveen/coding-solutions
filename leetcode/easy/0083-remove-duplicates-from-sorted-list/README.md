# Remove Duplicates from Sorted List

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given the `head` of a sorted linked list,  *delete all duplicates such that each element appears only once*. Return  *the linked list  **sorted**  as well*.

 

 **Example 1:** 

```
Input: head = [1,1,2]
Output: [1,2]

```

 **Example 2:** 

```
Input: head = [1,1,2,3,3]
Output: [1,2,3]

```

 

 **Constraints:** 

- The number of nodes in the list is in the range [0, 300].
- -100 <= Node.val <= 100
- The list is guaranteed to be sorted in ascending order.

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.2 MB (beats 70.18%)  
**Submitted:** 2026-08-18T15:01:28.580Z  

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=head
        while c and c.next:
            if c.val==c.next.val:
                c.next=c.next.next
            else:
                c=c.next
        return head
        
        
```

---

[View on LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)