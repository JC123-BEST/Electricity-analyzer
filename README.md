# Electricity Usage Analyzer

A beginner-level Python program that analyzes seven days of electricity consumption readings and provides basic usage statistics.

## About the Project

The Electricity Usage Analyzer was built to practice problem-solving, control flow, lists, loops, input validation, and defensive programming in Python.

The user enters one electricity reading for each day of the week. The program validates the input and then analyzes the readings to find useful information about the week's electricity consumption.

## Features

The program can:

- Calculate total electricity consumption
- Calculate average daily consumption
- Find the highest consumption and the corresponding day
- Find the lowest consumption and the corresponding day
- Identify days with above-average consumption
- Validate that exactly seven readings are entered
- Reject negative readings
- Handle invalid non-integer input without crashing

## How It Works

The program follows this general process:

1. Creates a list containing the seven days of the week.
2. Accepts seven electricity readings from the user.
3. Splits the input into individual values.
4. Validates the number and type of readings.
5. Converts valid readings from strings to integers.
6. Calculates the total and average consumption.
7. Searches for the highest and lowest readings.
8. Identifies days whose consumption is above the average.
9. Displays the analysis.

## Example

```text
Enter the readings for 7 days: 12 15 9 18 14 21 17

Total consumption: 106
Average: 15.142857142857142
Highest day: Saturday
Highest consumption: 21
Lowest day: Wednesday
Lowest consumption: 9
Above average days: ['Thursday', 'Saturday', 'Sunday']
```

## Concepts Practiced

This project gave me practical experience with:

- Lists
- List indexing
- `for` loops
- `while` loops
- `enumerate()`
- `split()`
- `len()`
- Conditional statements
- `break` and `continue`
- `try/except`
- `ValueError`
- Input validation
- Accumulators
- Finding maximum and minimum values
- Working with corresponding data using indexes

## What I Learned

One of my biggest lessons from this project was to think carefully about the solution to a problem before writing the code.

I became more comfortable working with lists and no longer find them as difficult as I did before. I also practiced defensive programming with `try/except` and learned to consider edge cases when designing a program.

The most difficult part of the project was control flow. I sometimes struggled to decide how the program should repeat, skip an operation, or move forward. This showed me that control flow is an area I need to continue practicing.

## Project Scope

This is **Version 1** of the project.

The goal was to build a functional command-line analyzer while focusing on Python fundamentals rather than adding unnecessary complexity such as a graphical interface, database, external libraries, or artificial intelligence.

## Future Improvements

Possible future versions could include:

- More flexible input methods
- Better formatted output
- Data visualization
- Saving historical readings
- More detailed electricity usage analysis

These features are intentionally outside the scope of Version 1.

## Author

Built as part of my Python project portfolio and learning journey.