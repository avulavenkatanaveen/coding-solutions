# CDEVPROB24

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Display day of the week

You are asked to create a program that displays the day of the week based on the first letter of the day. The program should use a `char` variable to store the first letter of a day (such as 'M' for Monday, 'T' for Tuesday, etc.), and based on the stored char, it should display the full name of the day.

 **When executed, the code will show:** 

```
The letter is W and the day is Wednesday

```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-08T18:28:30.386Z  

```c_cpp
#include <stdio.h>

int main() {
    // Declare a char variable to store the first letter of a day
    char day='w'; // For example, 'W' for Wednesday
    
    printf("The letter is %c and the day is Wednesday",day); // Print the name of the day
    
    return 0;
}
```

---

[View on CodeChef](https://www.codechef.com/problems/CDEVPROB24)