# CDEV016

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Choose the Correct Code

Which of the following snippets correctly use comments in C?

 **A.** 

```
// Display the months
printf("January February March April");

```

 **B.** 

```
/ *Display the months* /
printf("January February March April");

```

 **C.** 

```
// Single-line
/ *Multi-line comment* /
printf("January February March April");

```

 **D.** 

```
/ Display the months /
printf("January February March April");

```

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-29T16:11:31.206Z  

```cpp
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

[View on CodeChef](https://www.codechef.com/problems/CDEV016)