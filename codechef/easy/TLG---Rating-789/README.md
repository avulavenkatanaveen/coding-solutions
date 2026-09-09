# TLG - Rating 789

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-09T02:03:12.123Z  

```py
# cook your dish here
t=int(input())
for _ in range(t):
    a1,a2,a3,b1,b2,b3=map(int,input().split())
    c=min(a1,a2,a3)
    d=min(b1,b2,b3)
    a=a1+a2+a3-c
    b=b1+b2+b3-d
    if a>b:
        print("Alice")
    elif a==b:
        print("Tie")
    else:
        print("Bob")
```

---

[View on CodeChef](https://www.codechef.com/problems/TLG)