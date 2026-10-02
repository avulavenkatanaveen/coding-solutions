# CDEVPROB15

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Displaying Bank Balance with long

In this problem, you are tasked with handling large numerical values representing a bank balance. The goal is to demonstrate how both `int` and `long` data types can be used to manage values of different magnitudes.

 **Expected Output:** 

```
Balance in millions: 500 million
Total Bank Balance: 10000000 millions

```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-02T16:07:34.957Z  

```c_cpp
#include <stdio.h>

int main() {
    // Declare an int variable for a portion of the balance (in millions)
    // Represent 500 million 
    int x=500;
    int y=10000000;
    // Declare a long variable for the total bank balance and assign it the value 10000000
    
    printf("Balance in millions: %d million",x);
    // Print the value of millions portion
    printf("Total Bank Balance: %d millions",y);
    
    // Print the total bank balance
    
    
    return 0;
}
```

---

[View on CodeChef](https://www.codechef.com/problems/CDEVPROB15)