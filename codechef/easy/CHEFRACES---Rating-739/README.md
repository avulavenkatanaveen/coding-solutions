# CHEFRACES - Rating 739

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-04T11:12:13.051Z  

```py
# cook your dish here
t=int(input())
for _ in range(t):
    a,b,x,y=map(int,input().split())
    if (a/x)>(b/y):
        print("Chefina")
    elif (a/x)==(b/y):
        print("Both")
    else:
        print("Chef")
```

---

[View on CodeChef](https://www.codechef.com/problems/CHEFRACES)