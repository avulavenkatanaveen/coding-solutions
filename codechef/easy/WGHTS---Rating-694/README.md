# WGHTS - Rating 694

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-20T16:26:07.920Z  

```py
# cook your dish here
t = int(input())
for _ in range(t):
    a,b,x,y = map(int, input().split())
    if a <= b and (b - a) <= x:
        print("YES")
    elif a > b and (a - b) <= y:
        print("YES")
    else:
        print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/WGHTS)