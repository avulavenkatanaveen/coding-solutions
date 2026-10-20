# CDEVPROB41

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Worked Example - Converting Char to Int

In this example, we will store a character value and observe how C automatically converts it to an integer when assigned to a larger data type.

ASCII Table Reference

 **When executed, the code will show:** 

```
Character: A
Converted to ASCII (int): 65

```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-20T15:38:14.489Z  

```c_cpp
#include <stdio.h>

int main() {
    // Declare and initialize a character variable
    char letter = 'A';

    // Implicit type conversion to int
    int asciiValue = letter;

    // Output the values
    printf("Character: %c\n", letter); // The char 'A' is automatically converted to its ASCII integer value (65)
    
    printf("Converted to ASCII (int): %d", asciiValue);

    return 0;
}

```

---

[View on CodeChef](https://www.codechef.com/problems/CDEVPROB41)