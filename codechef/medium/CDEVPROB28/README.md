# CDEVPROB28

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Worked Example - Storing and Displaying Boolean

In this example, we demonstrate how to use the `_Bool` data type to store simple boolean values (true or false) in C, and display them.

 **When executed, the code will show:** 

```
isAvailable: 1
isClosed: 0

```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-10T15:43:20.836Z  

```c_cpp
#include <stdio.h>

int main() {
    // Declare a _Bool variable for availability and set it to true (1)
    _Bool isAvailable = 1;

    // Declare a _Bool variable for closed status and set it to false (0)
    _Bool isClosed = 0;

    // Print the values of isAvailable and isClosed
    printf("isAvailable: %d\n", isAvailable);  // 1 represents true
    printf("isClosed: %d", isClosed);        // 0 represents false

    return 0;
}

```

---

[View on CodeChef](https://www.codechef.com/problems/CDEVPROB28)