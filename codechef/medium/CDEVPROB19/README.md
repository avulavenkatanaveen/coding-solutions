# CDEVPROB19

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Discounted Price

You are given the original price of a product and the discounted price. Your task is to declare the appropriate data types for both of them using `float` and `double`.

 **When executed, the code will show:** 

```
Original Price: 1678.991233
Discounted Price: 1600.000000

```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-06T02:55:48.713Z  

```c_cpp
#include <stdio.h>

int main() {
    // Declare double variable for the original price 
    double originalPrice = 1678.99123340;
    
    // Declare float varaible for the discounted price
    float discountedPrice = 1600.00f;

    // Print the original price
    printf("Original Price: %lf\n", originalPrice);
    
    // Print the discounted price
    printf("Discounted Price: %f\n", discountedPrice);

    return 0;
}
```

---

[View on CodeChef](https://www.codechef.com/problems/CDEVPROB19)