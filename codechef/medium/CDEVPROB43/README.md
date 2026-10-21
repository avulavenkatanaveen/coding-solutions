# CDEVPROB43

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Tracking Visitor Entry

You are given the first character (`V`) of a visitor's name. Use  **implicit conversion**  to convert it into a `float`.
 **Remember:**  Since `char` is a smaller data type than `float`, it can be automatically converted.
ASCII Table Reference

 **Expected Output:** 

```
The converted float value is 86.000000

```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-21T15:50:01.433Z  

```c_cpp
#include <stdio.h>

int main() {
    char firstChar = 'V';               // Name of the daily visitor stored as char

    
    float convertedCount =firstChar;     // Complete the code


    printf("The converted float value is %f\n", convertedCount); // Complete the code

    return 0;
}


```

---

[View on CodeChef](https://www.codechef.com/problems/CDEVPROB43)