# CDEVPROB38

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Declaring Multiple Variables

You are required to declare multiple variables of different data types in C. The task is to declare the variables of these following types:

- An int to store the age and height (in cm) of a person.
- A long to store the person's contact number and PIN code of his city.

Once declared, you need to assign values to these variables and display them.

 **Expected Output:** 

```
Age: 25
Height: 168 cm
Contact Number: 9876543210
PIN Code: 111111

```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-20T15:37:51.798Z  

```c_cpp
#include <stdio.h>

int main() {
    // Declare variables of different types in a single line
    int age=25,height=168;   // Declare an integer for age(25) and height(168) and assign a value
    long num=9876543210,code=111111;   // Declare a long for contact number(9876543210) and PIN(111111) Code of a person and assign a value

    // Print the values of the variables
    printf("Age: %d\n", age);      // Print age
    printf("Height: %d cm\n", height);   // Print height 
    printf("Contact Number: %ld\n", num);      // Print contact number
    printf("PIN Code: %ld\n", code);     // Print PIN Code

    return 0;
}
```

---

[View on CodeChef](https://www.codechef.com/problems/CDEVPROB38)