# PASSORFAIL - Rating 730

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-02T04:45:46.217Z  

```py
# cook your dish here
t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    if (a>=b and a<=c) or (a<=b and a>=c):
        second=a
    elif (b>=a and b<=c) or (b<=a and b>=c):
        second=b
    else:
        second=c
    print(second)
        
```

---

[View on CodeChef](https://www.codechef.com/problems/PASSORFAIL)