# CDEVPROB37

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Worked Example - OMR Sheet

In this example, we will declare multiple variables of the same type (`char`) in a single statement, assign values to them, and print the values to display the answers marked by a student in a competitive exam.

 **When executed, the code will show:** 

```
Question 1 has 'd' as an answer
Question 2 has 'a' as an answer
Question 3 has 'c' as an answer
Question 4 has 'a' as an answer

```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-20T15:34:04.353Z  

```c_cpp
#include <stdio.h> // Including the standard I/O library to use printf for output

int main() {
    // Declare multiple char variables in one statement and initialize them
    // q1, q2, q3, q4 are the variables representing answers to questions.
    char q1 = 'd', q2 = 'a', q3 = 'c', q4 = 'a';

    // Output the values of the answers marked
    // The format specifier '%c' is used to print a single character (the answer).
    printf("Question 1 has '%c' as an answer\n", q1);
    printf("Question 2 has '%c' as an answer\n", q2);
    printf("Question 3 has '%c' as an answer\n", q3);
    printf("Question 4 has '%c' as an answer", q4);
    return 0;
}
```

---

[View on CodeChef](https://www.codechef.com/problems/CDEVPROB37)