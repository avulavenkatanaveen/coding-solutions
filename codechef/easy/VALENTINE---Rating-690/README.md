# VALENTINE - Rating 690

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-16T16:14:46.057Z  

```py
# cook your dish here
t=int(input())
for _ in range(t):
    x1,x2,y1,y2=map(int,input().split())
    a=abs(x1-y1)
    b=abs(x2-y2)
    print(max(a,b))
    
```

---

[View on CodeChef](https://www.codechef.com/problems/VALENTINE)