# DATAS01

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Exam Marks Statistics Project

 **Hello developers!**  Welcome to the  **Exam Marks Statistics Project!**  📊✏️

Chef is building an analytics tool to understand  **student exam performance**  using numerical data. Schools often collect exam marks, but raw numbers alone don’t provide meaningful insights.

Chef wants to analyze exam scores to:

- Understand overall class performance
- Identify high-performing students
- Detect failing students
- Find the highest and lowest scores

Your task is to use the  **NumPy Library**  to transform raw exam marks into useful statistical insights.

 **What’s Already Provided** 
You are given a single file: `main.py`

- All required function names are already defined.
- The program flow is already set up.
- You only need to fill in the missing logic (__________) using the NumPy Library.
- Do NOT change function names or print statements.

 **Dataset** 
You will work with the following exam marks dataset:

```
78, 85, 33, 66, 15, 88, 90, 59, 29, 70

```

Each value represents a student’s exam score

### Your Tasks
- Load Exam Marks Inside the function load_data(): Create a NumPy array containing the given exam marks. We are returning the NumPy array so that it can be reused in other functions. Docs: np.array() function
- Compute Class Statistics Inside the function compute_statistics(): Compute: Average marks Median marks Standard deviation (rounded to 2 decimal places) Docs: np.mean() function, np.median() function, np.std() function, round() function
- Analyze Student Performance Inside the function analyze_performance(): Using the exam marks and average marks: Identify students who scored above average Count how many students scored above average Identify students who failed (marks < 35) Count the number of failed students Docs: len() function
- Find Highest and Lowest Scores Inside the function find_extremes(): Determine: Highest exam score Lowest exam score Docs: np.argmax() function, np.argmin() function

 **Expected Output:** 

```
Exam Marks Statistics Analysis...

Exam Marks:  [78 85 33 66 15 88 90 59 29 70]

--- Class Statistics ---
Average Marks:  61.3
Median Marks:  68.0
Standard Deviation:  25.43

--- Performance Insights ---
Students scoring above average:  [78 85 66 88 90 70]
Number of students above average:  6

Students who failed (marks < 35):  [33 15 29]
Number of failed students:  3

--- Extremes ---
Highest Score:  90
Lowest Score:  15

```

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-11T04:26:08.690Z  

```cpp

    return average, median, std_deviation
    # Returning all three values as a tuple
    print("Standard Deviation: ", std_deviation)

    print("Median Marks: ", median)
    print("Average Marks: ", average)

    print("\n--- Class Statistics ---")
    std_deviation = round(np.std(marks),2)
    # TODO: Calculate the standard deviation
    median =np.median(marks)
    
    # TODO: Calculate the median marks
    
    average =np.mean(marks)
    # TODO: Calculate the average (mean) marks
    """
def compute_statistics(marks):
    """
    Compute and print basic statistical measures using NumPy.
# 2. Compute and print basic statistics

```

---

[View on CodeChef](https://www.codechef.com/problems/DATAS01)