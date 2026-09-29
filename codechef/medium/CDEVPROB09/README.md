# CDEVPROB09

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Choosing the Correct Output

Look at the given code:

```
#include <stdio.h>

int main() {
    int value = 500;
    printf("The value is: %d\n", value);
    return 0;
}

```

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-29T16:15:00.117Z  

```cpp
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

[View on CodeChef](https://www.codechef.com/problems/CDEVPROB09)