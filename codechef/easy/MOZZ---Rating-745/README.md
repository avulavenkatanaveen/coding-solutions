# MOZZ - Rating 745

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-04T11:22:10.045Z  

```py
# cook your dish here
t=int(input())
for _ in range(t):
    x,y,a,b=map(int,input().split())
    m=0
    if x!=a and x!=b:
        m+=1
    if y!=a and y!=b:
        m+=1
    print(m)
```

---

[View on CodeChef](https://www.codechef.com/problems/MOZZ)