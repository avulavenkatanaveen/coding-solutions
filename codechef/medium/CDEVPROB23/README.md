# CDEVPROB23

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Worked Example - Displaying Student Details

In this example, we display a student's gender and academic grade using the `char` data type, which is ideal for storing single characters like letters or symbols.

 **When executed, the code will show:** 

```
Gender: M  
Grade: B

```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-08T18:27:14.498Z  

```c_cpp
#include <stdio.h>

int main() {
    char gender = 'M';     // M for Male
    char grade = 'B';      // B grade for performance

    printf("Gender: %c\n", gender); // format specifier '%c' is used to print a single character
    printf("Grade: %c", grade);

    return 0;
}

```

---

[View on CodeChef](https://www.codechef.com/problems/CDEVPROB23)