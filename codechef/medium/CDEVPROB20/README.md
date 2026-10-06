# CDEVPROB20

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Calculating the Area of a Circle

You are working as a developer in a scientific research organization. Write a program to correctly assign the datatypes for radius and area of a circle, using `float` for the radius and `double` for the area.

 **Steps to complete:** 

- The radius of the circle must be stored as a floating-point number.
- The area needs to be stored in a double for higher precision.
- Print the radius and the area of the circle.

 **Expected Output:** 

```
Radius: 5.345000
Area: 89.752232

```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-06T04:24:26.243Z  

```c_cpp
#include <stdio.h>

int main() {
    // Declare a float variable for the radius and initialize it with 5.345
    float r=5.345000;
    // Declare a double variable for the area and initialize it with 89.752232
    double a=89.752232;

    // Print the radius of the circle
    printf("Radius: %f\n",r);

    // Print the area of the circle
    printf("Area: %lf\n",a);


    return 0;
}

```

---

[View on CodeChef](https://www.codechef.com/problems/CDEVPROB20)