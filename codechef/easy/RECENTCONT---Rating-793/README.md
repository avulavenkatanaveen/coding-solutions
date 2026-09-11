# RECENTCONT - Rating 793

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-11T14:19:19.600Z  

```py
# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(n - 1, -1, -1):
        if a[i] != 0:
            print(i)
            break
    
```

---

[View on CodeChef](https://www.codechef.com/problems/RECENTCONT)