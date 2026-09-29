# CDEVPROB08

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Demonstrating Use of short and int in C

In this example, we demonstrate how to declare and initialize variables using the `short` and `int` data types in C. This allows you to store different ranges of integer values depending on the memory and size requirements.

 **When executed, the code will show:** 

```
Year of Birth: 2005
Student ID: 102345

```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-29T16:14:43.637Z  

```c_cpp
#include <stdio.h>

int main() {
    // Declare and initialize a short variable for year of birth
    short birthYear = 2005;

    // Declare and initialize an int variable for student ID
    int studentID = 102345;

    // Display the values
    printf("Year of Birth: %hd\n", birthYear);
    printf("Student ID: %d", studentID);

    return 0;
}

```

---

[View on CodeChef](https://www.codechef.com/problems/CDEVPROB08)