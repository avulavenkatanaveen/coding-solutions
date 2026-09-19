# ADJSUMPAR - Rating 1018

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-19T16:36:08.298Z  

```py
from collections import Counter

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        freq = Counter(a)
        if max(freq.values()) >= 3:
            print("No")
        else:
            print("Yes")

if __name__ == '__main__':
    solve()
```

---

[View on CodeChef](https://www.codechef.com/problems/ADJSUMPAR)