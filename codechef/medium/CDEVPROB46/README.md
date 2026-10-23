# CDEVPROB46

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Worked Example - int to char

In this example, we demonstrate how to use explicit type casting to convert a precise int value into a char. (Use ASCII table for reference)

 **When executed, the code will show:** 

```
Original int value: 120
Converted char value: x

```

 **Relevant ASCII Table (Integer to Character)** 

Uppercase	ASCII	Lowercase	ASCII
A	65	a	97
B	66	b	98
C	67	c	99
D	68	d	100
E	69	e	101
F	70	f	102
G	71	g	103
H	72	h	104
I	73	i	105
J	74	j	106
K	75	k	107
L	76	l	108
M	77	m	109
N	78	n	110
O	79	o	111
P	80	p	112
Q	81	q	113
R	82	r	114
S	83	s	115
T	84	t	116
U	85	u	117
V	86	v	118
W	87	w	119
X	88	x	120
Y	89	y	121
Z	90	z	122

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-23T15:52:13.877Z  

```c_cpp
#include <stdio.h>

int main() {
    // Declare and initialize an int variable with a value that is outside the range of char
    int largeValue = 120;  

    // Narrowing conversion from int to char
    char smallValue = largeValue;  

    // Output the values
    printf("Original int value: %d\n", largeValue);  // Prints the original int value (120)
    printf("Converted char value: %c", smallValue);  // Prints the corresponding char value from ASCII table

    return 0;
}
```

---

[View on CodeChef](https://www.codechef.com/problems/CDEVPROB46)