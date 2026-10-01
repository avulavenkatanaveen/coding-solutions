# CDEVPROB13

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Worked Example - Demonstrating the Use of long

In this example, we demonstrate how to declare and use a `long` variable to store a large integer value such as a bank account number, which exceeds the typical range of an `int`.

 **When executed, the code will show:** 

```
Bank Account Number: 9876543210

```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-01T16:53:16.601Z  

```c_cpp
#include <stdio.h>

int main() {
    // Declare a long variable to store a large bank account number
    long accountNumber = 9876543210;

    // Print the value of the bank account number
    printf("Bank Account Number: %ld", accountNumber);

    return 0;
}

```

---

[View on CodeChef](https://www.codechef.com/problems/CDEVPROB13)