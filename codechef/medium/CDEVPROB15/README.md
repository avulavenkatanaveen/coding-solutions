# CDEVPROB15

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Storing Large Integer Values with long

Complete the code where you are tasked with declaring a `long` variable to store the total distance traveled by a car during a road trip.

 **Expected Output:** 

```
Total distance traveled: 360590000 km

```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-01T16:56:01.189Z  

```c_cpp
#include <stdio.h>

int main() {
    // Declare a long variable to store the total distance
    int total_distance=360590000; // Variable declaration and assignment

    // Print the total distance traveled
    printf("Total distance traveled:%d km", total_distance); // Use %ld to print long variable

    return 0;
}
```

---

[View on CodeChef](https://www.codechef.com/problems/CDEVPROB15)