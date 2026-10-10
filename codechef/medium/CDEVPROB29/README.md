# CDEVPROB29

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Working with _Bool Data Type

What will be the output of the following C program?

```
#include <stdio.h>

int main() {
    _Bool isReady = 1;    // true
    _Bool isCompleted = 0; // false

    printf("isReady: %d\n", isReady);
    printf("isCompleted: %d\n", isCompleted);

    return 0;
}

```

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-10T15:44:05.080Z  

```cpp
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

[View on CodeChef](https://www.codechef.com/problems/CDEVPROB29)