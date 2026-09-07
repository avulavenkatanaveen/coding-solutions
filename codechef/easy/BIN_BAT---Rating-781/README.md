# BIN_BAT - Rating 781

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-07T14:12:39.150Z  

```py
# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if n%2!=0:
        print(-1)
    else:
        c=a.count(1)
        ans=abs(n//2-c)
        print(ans)
```

---

[View on CodeChef](https://www.codechef.com/problems/BIN_BAT)