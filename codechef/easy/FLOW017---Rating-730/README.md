# FLOW017 - Rating 730

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Second Largest

Three numbers  **A**,  **B**  and  **C**  are the inputs. Write a program to find second largest among them.

### Input Format

The first line contains an integer  **T**, the total number of testcases. Then  **T**  lines follow, each line contains three integers  **A**,  **B**  and  **C**.

### Output Format

For each test case, display the second largest among  **A**,  **B**  and  **C**, in a new line.

### Constraints
- 1 ≤ T ≤ 1000
- 1 ≤ A,B,C ≤ 1000000
### Sample 1:
Input
Output

```
3 
120 11 400
10213 312 10
10 3 450
```

```
120
312
10
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-02T04:45:43.161Z  

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

[View on CodeChef](https://www.codechef.com/problems/FLOW017)