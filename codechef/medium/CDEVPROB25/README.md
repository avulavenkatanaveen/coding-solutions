# CDEVPROB25

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Student Grade Tracker

In this program, you're building a simple system to track a student's academic information using C. You will use three different primitive data types: a `char` to represent grades, an `int` to store the student's unique ID and a `short` to store the class section number

 **Steps to complete:** 

- Declare and initialize all three variables. Set the grade as 'B'. Set the student ID as 20231. Set the section number as 12.
- Print these values.

 **Expected Output:** 

```
Student Grade: B  
Student ID: 20231  
Section Number: 12

```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-09T15:44:19.370Z  

```c_cpp
#include <stdio.h>

int main() {
    // Declare and initialize student details
    char grade='B';
    int student_id=20231;
    short section_number=12;
    

    // Print student details
    printf("Student Grade: %c\n",grade);
    printf("Student ID: %d\n",student_id);
    printf("Section Number: %hd\n",section_number);

    return 0;
}

```

---

[View on CodeChef](https://www.codechef.com/problems/CDEVPROB25)