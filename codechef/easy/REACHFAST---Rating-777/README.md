# REACHFAST - Rating 777

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-04T12:10:21.040Z  

```py
# cook your dish here
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    values=list(map(int,input().split()))
    c=0
    for x in values:
        if (x+k)%7==0:
            c+=1
    print(c)
```

---

[View on CodeChef](https://www.codechef.com/problems/REACHFAST)