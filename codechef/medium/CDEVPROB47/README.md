# CDEVPROB47

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Fill in the Blanks - Explicit Type Conversion

You are given the task of converting the total price of the product in a warehouse to int, such that the total price could be rounded off to an integer value.

 **Task to Complete:** 

- Declare a double variable for the total price of the box.
- Declare an int variable to store the total price of the box.
- Perform explicit type conversion from double to int to show the result by rounding off the total price.
- Display the desired result.

 **Expected Output:** 

```
Converted Total Price (int): 9999

```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-23T15:54:06.982Z  

```c_cpp
#include <stdio.h>

int main() {
    // Declare double variable for total price of the box
    double total_price = 9999.9999;

    // Declare an int variable to store the total price of the box
    int converted_price;

    // Perform explicit type conversion to int for rounding off
    converted_price = (int) total_price;;

    // Print the total price in int
    printf("Converted Total Price (int): %d", converted_price);

    return 0;
}
```

---

[View on CodeChef](https://www.codechef.com/problems/CDEVPROB47)