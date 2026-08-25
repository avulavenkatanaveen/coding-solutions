# SELFDEF - Rating 712

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-25T16:09:00.964Z  

```py
# cook your dish here
import math
t=int(input())
for _ in range(t):
    x,n=map(int,input().split())
    p=math.ceil(n/100)
    ans=max(0,p-x)
    print(ans)
```

---

[View on CodeChef](https://www.codechef.com/problems/SELFDEF)