# CDEV015

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Print Different Seasons

In this example, we demonstrate how comments in C help improve code readability by explaining different parts of the program.

Comments are used to describe a list of seasons being printed.

 **When executed, the code will display,** 

```
Spring Summer Autumn Winter

```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-29T16:10:50.351Z  

```c_cpp
#include <stdio.h> // For input and output functions

int main() {
    // Print the name of a season
    printf("Spring ");  // This is the first season

    /* The next lines print
       the remaining seasons */
    printf("Summer ");  // Warmest season
    printf("Autumn ");  // Also called Fall
    printf("Winter");   // Coldest season

    return 0; // Program ends here
}
```

---

[View on CodeChef](https://www.codechef.com/problems/CDEV015)