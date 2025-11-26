📘 README.md
GradeBook Analyzer

A Python-based command-line application that helps automate the analysis and reporting of student marks.
This tool reads student data (manual input or CSV), computes statistics, assigns grades, and displays a formatted results table.

This project is created as part of the Programming for Problem Solving using Python mini project.

📂 Project Overview

Lecturers often need a fast and accurate way to analyze student marks. Doing it manually is time-consuming and error-prone.
The GradeBook Analyzer solves this problem by automating:

Data entry

Statistical calculations

Grade assignments

Pass/fail evaluation

Tabular reporting

🎯 Features
✔ 1. Data Input

Manual entry of student names and marks

CSV file import using Python's csv module

✔ 2. Statistical Analysis

Average score

Median score

Highest scorer (name + score)

Lowest scorer (name + score)

✔ 3. Grade Assignment

Grades are assigned based on the following scale:

A: 90+

B: 80–89

C: 70–79

D: 60–69

F: <60

✔ 4. Grade Distribution

Counts number of students in each grade category (A–F).

✔ 5. Pass / Fail Detection

Using list comprehensions:

Passed: score ≥ 40

Failed: score < 40

✔ 6. Results Table

Formatted output showing:

Name        Marks      Grade
---------------------------------

✔ 7. CLI Loop

Allows the user to:

Perform new analysis

Exit program

📁 Project Structure
gradebook_analyzer/
│
├── gradebook.py       # Main program with all features
├── students.csv       # Sample CSV (for testing)
└── README.md          # Project documentation

📥 Sample CSV File

A sample students.csv used for testing:

Alice,78
Bob,92
Charlie,66
Disha,84
Farhan,39

▶️ How to Run the Program
Step 1: Open Terminal / Command Prompt

Navigate to the project folder:

cd gradebook_analyzer

Step 2: Run the Python Script
python gradebook.py

Step 3: Choose an Option

You will see:

1. Enter student data manually
2. Load data from CSV file
3. Exit


Follow the menu instructions to enter marks or load the CSV file.

🧪 Testing Requirements

This project has been tested with:

✔ At least 5 manual entries

✔ At least 1 CSV file

✨ Conclusion

The GradeBook Analyzer is a simple, efficient, and modular Python tool that demonstrates core programming skills including:

Control flow

Dictionaries & lists

File handling

Functions

List comprehensions

Loops

CLI application design

This project fulfills all the requirements of the Mini Project assignment.
